from django.shortcuts import render


def home(request):

    return render(
        request,
        'home.html'
    )

from agreements.models import Agreement
from agreements.pdf import generate_agreement_pdf
from django.http import HttpResponse
import traceback

def test_pdf(request):
    try:
        agreement = Agreement.objects.first()

        if agreement is None:
            return HttpResponse("No agreement found.")

        generate_agreement_pdf(agreement)

        return HttpResponse("PDF generated successfully.")

    except Exception:
        error = traceback.format_exc()
        print(error)           # Goes to Render logs
        return HttpResponse(f"<pre>{error}</pre>", status=500)

def check_weasyprint(request):
    return JsonResponse({
        "status": "WeasyPrint imported successfully"
    })
