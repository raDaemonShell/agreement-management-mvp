from rest_framework import serializers
from .models import Agreement, Partner


class PartnerSerializer(serializers.ModelSerializer):
    av = serializers.CharField(source='avatar')
    bg = serializers.CharField(source='background')
    col = serializers.CharField(source='color')
    name = serializers.CharField(source='company_name')
    ind = serializers.CharField(source='industry')
    loc = serializers.CharField(source='location')

    class Meta:
        model = Partner
        fields = [
            'id',
            'av',
            'bg',
            'col',
            'name',
            'ind',
            'loc'
        ]


class AgreementSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer(read_only=True)
    partner_id = serializers.PrimaryKeyRelatedField(
        queryset=Partner.objects.all(),
        source='partner',
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Agreement
        fields = "__all__"