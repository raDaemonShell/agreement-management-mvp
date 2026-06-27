from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.conf import settings
from .models import Agreement, Partner
from .serializers import AgreementSerializer, PartnerSerializer
from .pdf_generator import generate_agreement_pdf
from django.utils import timezone
import os
from django.http import JsonResponse
import subprocess


@api_view(['GET'])
def partner_list(request):
    partners = Partner.objects.all()
    serializer = PartnerSerializer(partners, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def dashboard_summary(request):
    return Response({
        'draft': Agreement.objects.filter(status='DRAFT').count(),
        'awaiting_signature': Agreement.objects.filter(status='SENT').count(),
        'signed': Agreement.objects.filter(status='SIGNED').count(),
    })


class AgreementViewSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all().order_by('-created_at')
    serializer_class = AgreementSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        try:
            agreement = Agreement.objects.get(pk=response.data['id'])
            generate_agreement_pdf(agreement)
        except Exception as e:
            print(f'PDF generation error: {e}')
        return response

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        previous_status = instance.status
        response = super().partial_update(request, *args, **kwargs)
        instance.refresh_from_db()

        # Generate PDF when sections are saved
        if 'section_1' in request.data or 'initiator_signed_at' in request.data:
            try:
                generate_agreement_pdf(instance)
            except Exception as e:
                print(f'PDF generation error: {e}')

        # Send sent emails when status changes to SENT
        if previous_status != 'SENT' and instance.status == 'SENT':
            try:
                from .emails import send_agreement_emails
                send_agreement_emails(instance)
            except Exception as e:
                print(f'Email error: {e}')

        # Regenerate PDF and send signed emails when counterparty signs
        if previous_status != 'SIGNED' and instance.status == 'SIGNED':
            try:
                generate_agreement_pdf(instance)
            except Exception as e:
                print(f'PDF regeneration error: {e}')
            try:
                from .emails import send_signed_emails
                send_signed_emails(instance)
            except Exception as e:
                print(f'Signed email error: {e}')

        return response

    @action(detail=True, methods=['get'])
    def download_pdf(self, request, pk=None):
        agreement = self.get_object()
        pdf_path = os.path.join(settings.MEDIA_ROOT, 'agreements', f"{agreement.id}.pdf")
        if not os.path.exists(pdf_path):
            try:
                generate_agreement_pdf(agreement)
            except Exception as e:
                return Response({'error': str(e)}, status=500)
        pdf_url = request.build_absolute_uri(
            f"{settings.MEDIA_URL}agreements/{agreement.id}.pdf"
        )
        return Response({'url': pdf_url})
    
    @action(detail=True, methods=['post'])
    def send_otp(self, request, pk=None):
        agreement = self.get_object()
        try:
            from .emails import send_otp_email
            send_otp_email(agreement)
            return Response({'message': 'OTP sent'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @action(detail=True, methods=['post'])
    def verify_otp(self, request, pk=None):
        agreement = self.get_object()
        code = request.data.get('code', '')

        if not agreement.otp_code:
            return Response({'error': 'No OTP generated'}, status=400)

        if timezone.now() > agreement.otp_expires_at:
            return Response({'error': 'OTP expired'}, status=400)

        if code != agreement.otp_code:
            return Response({'error': 'Invalid code'}, status=400)

        # Clear OTP after successful verification
        agreement.otp_code = ''
        agreement.otp_expires_at = None
        agreement.save(update_fields=['otp_code', 'otp_expires_at'])

        return Response({'message': 'Verified'})
    
    @action(detail=True, methods=['post'])
    def sign(self, request, pk=None):
        from django.utils import timezone
        agreement = self.get_object()
        signature = request.data.get('signature', '')

        if not signature:
            return Response({'error': 'Signature required'}, status=400)

        agreement.counterparty_signature = signature
        agreement.counterparty_signed_at = timezone.now()
        agreement.status = 'SIGNED'
        agreement.save(update_fields=[
            'counterparty_signature',
            'counterparty_signed_at',
            'status'
        ])

        # Regenerate PDF with signature
        try:
            generate_agreement_pdf(agreement)
        except Exception as e:
            print(f'PDF error: {e}')

        # Send signed emails
        try:
            from .emails import send_signed_emails
            send_signed_emails(agreement)
        except Exception as e:
            print(f'Email error: {e}')

        serializer = self.get_serializer(agreement)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def email_copy(self, request, pk=None):
        agreement = self.get_object()
        email = request.data.get('email', agreement.contact_email)

        pdf_path = os.path.join(settings.MEDIA_ROOT, 'agreements', f"{agreement.id}.pdf")
        if not os.path.exists(pdf_path):
            return Response({'error': 'PDF not found'}, status=404)

        try:
            from .emails import send_pdf_copy_email
            send_pdf_copy_email(agreement, email, pdf_path)
            return Response({'message': 'Email sent'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)


    def check_weasyprint(request):
        packages = {}

        for cmd, name in [
            (["fc-list"], "Fonts"),
            (["ldd", "--version"], "GLIBC"),
            (["dpkg", "-l"], "Installed packages"),
        ]:
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                packages[name] = result.stdout[:3000]
            except Exception as e:
                packages[name] = str(e)

        return JsonResponse(packages)