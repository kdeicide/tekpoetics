from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html', {'title': 'Home'})

def releases(request):
    return render(request, 'core/releases.html', {'title': 'Releases'})
