from django.shortcuts import render


def home(request):

    return render(
        request,
        'home.html'
    )

from django.http import JsonResponse
from weasyprint import HTML

def check_weasyprint(request):
    return JsonResponse({
        "status": "WeasyPrint imported successfully"
    })

def test_pdf(request):
    pdf = HTML(string="<h1>Hello Render!</h1>").write_pdf()

    return HttpResponse(
        pdf,
        content_type="application/pdf"
    )