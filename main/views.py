from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def authorisation(request):
    return render(request, 'main/authorisation.html')

def profile(request):
    return render(request, 'main/profile.html')