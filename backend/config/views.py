from django.shortcuts import render


def home(request):

    return render(
        request,
        'home.html'
    )

from django.http import JsonResponse
from weasyprint import HTML
from django.http import HttpResponse

def test_pdf(request):
    print("===== TEST PDF VIEW EXECUTED =====")
    return HttpResponse("TEST PDF WORKS")

def check_weasyprint(request):
    return JsonResponse({
        "status": "WeasyPrint imported successfully"
    })

def test_pdf(request):
    print("===== TEST PDF VIEW EXECUTED =====")
    return HttpResponse("TEST PDF WORKS")