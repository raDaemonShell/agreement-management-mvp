from django.contrib import admin

from .models import Agreement


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "agreement_type",
        "status",
        "counterparty_company",
        "created_at",
    )

    search_fields = (
        "title",
        "counterparty_company",
    )

    list_filter = (
        "status",
        "agreement_type",
    )