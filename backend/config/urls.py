from django.contrib import admin
from django.urls import path, include
from django.conf import settings                        
from django.conf.urls.static import static            
from .views import home, check_weasyprint, test_pdf


urlpatterns = [
    path('', home),

    path('check-weasyprint/', check_weasyprint),
    path('test-pdf/', test_pdf),

    path('admin/', admin.site.urls),
    path('api/', include('agreements.urls')),
]