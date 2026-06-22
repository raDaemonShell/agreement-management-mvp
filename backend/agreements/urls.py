from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

from .views import (
    AgreementViewSet,
    dashboard_summary,
    partner_list,
)

router = DefaultRouter()

router.register(
    r'agreements',

    AgreementViewSet,

    basename='agreement'
)

urlpatterns = [

    path(
        'dashboard/',

        dashboard_summary
    ),

    path(
        'partners/',

        partner_list
    ),


]

urlpatterns += router.urls