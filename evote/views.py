from django.http import HttpResponse
from django.shortcuts import render


def landing(request):
    return render(request, 'landing.html')

def info(request):
    return render(request, 'info.html')