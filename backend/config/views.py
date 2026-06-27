from django.shortcuts import render


def home(request):

    return render(
        request,
        'home.html'
    )

from django.http import JsonResponse

from agreements.models import Agreement
from agreements.pdf import generate_agreement_pdf
from django.conf import settings
from django.http import HttpResponse
import os

def test_pdf(request):
    try:
        agreement = Agreement.objects.first()

        if agreement is None:
            return HttpResponse("No agreement found in database.")

        generate_agreement_pdf(agreement)

        pdf_path = os.path.join(
            settings.MEDIA_ROOT,
            "agreements",
            f"{agreement.id}.pdf"
        )

        with open(pdf_path, "rb") as f:
            return HttpResponse(
                f.read(),
                content_type="application/pdf"
            )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return HttpResponse(str(e), status=500)

def check_weasyprint(request):
    return JsonResponse({
        "status": "WeasyPrint imported successfully"
    })
