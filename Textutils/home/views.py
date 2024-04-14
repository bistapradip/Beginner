from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def analyze(request):
    djtext = request.GET.get("text", "default")
    removepuc = request.GET.get("removepuc", "default")
    if removepuc == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params = {"purpose": "Remove Puncutation", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)
    else:
        return HttpResponse("Error")
            
def home(request):
    return render(request, "removepuc.html")


