from rest_framework import viewsets

from .models import Agreement

from .serializers import AgreementSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mock_data import PARTNERS


@api_view(['GET'])
def partner_list(request):

    return Response(PARTNERS)



class AgreementViewSet(viewsets.ModelViewSet):

    queryset = Agreement.objects.all().order_by("-created_at")

    serializer_class = AgreementSerializer

@api_view(['GET'])
def dashboard_summary(request):

    return Response({

        "draft": Agreement.objects.filter(
            status='DRAFT'
        ).count(),

        "awaiting_signature": Agreement.objects.filter(
            status='SENT'
        ).count(),

        "signed": Agreement.objects.filter(
            status='SIGNED'
        ).count(),

    })