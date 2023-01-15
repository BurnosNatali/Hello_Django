from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 345 / 45
    return render(request, "about.html", {'getting':a})

def home(request):
    return HttpResponse("Здравствуйте!Ура,я дом!")
