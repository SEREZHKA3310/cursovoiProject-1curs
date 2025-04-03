from django.shortcuts import render

# Create your views here.

def registration(request):
    value = {
        "values": ["email", "login", "password", "repeat the password", "weight", "height"]
    }
    return render(request, 'authorisation/registration.html', value)

def authorisation(request):
    value = {
        "values": ["email", "password"]
    }
    return render(request, 'authorisation/authorisation.html', value)

def profile(request):
    return render(request, 'main/profile.html')

