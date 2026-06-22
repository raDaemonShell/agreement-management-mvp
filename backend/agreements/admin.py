from django.contrib import admin

from .models import Agreement, Partner


@admin.register(Agreement)

class AgreementAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
    )


@admin.register(Partner)

class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        'company_name',
        'industry',
        'location'
    )

    list_filter = (
        'industry',
    )