from django.shortcuts import render


def home(request):

    return render(
        request,
        'home.html'
    )

from django.http import JsonResponse

from django.http import HttpResponse
from weasyprint import HTML
import traceback

def test_pdf(request):
    try:
        print("Starting WeasyPrint...")

        pdf = HTML(
            string="<h1>Hello Render!</h1>"
        ).write_pdf()

        print("PDF generated successfully.")

        return HttpResponse(
            pdf,
            content_type="application/pdf"
        )

    except Exception:
        traceback.print_exc()
        return HttpResponse(
            "WeasyPrint failed. Check Render logs.",
            status=500
        )

def check_weasyprint(request):
    return JsonResponse({
        "status": "WeasyPrint imported successfully"
    })

def test_pdf(request):
    print("===== TEST PDF VIEW EXECUTED =====")
    return HttpResponse("TEST PDF WORKS")