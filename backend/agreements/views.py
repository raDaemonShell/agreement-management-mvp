from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Agreement, Partner
from .serializers import (
    AgreementSerializer,
    PartnerSerializer
)


@api_view(['GET'])
def partner_list(request):

    partners = Partner.objects.all()

    serializer = PartnerSerializer(
        partners,
        many=True
    )

    return Response(serializer.data)


class AgreementViewSet(viewsets.ModelViewSet):

    queryset = Agreement.objects.all().order_by(
        '-created_at'
    )

    serializer_class = AgreementSerializer


@api_view(['GET'])
def dashboard_summary(request):

    return Response({

        'draft': Agreement.objects.filter(
            status='DRAFT'
        ).count(),

        'awaiting_signature': Agreement.objects.filter(
            status='SENT'
        ).count(),

        'signed': Agreement.objects.filter(
            status='SIGNED'
        ).count(),

    })