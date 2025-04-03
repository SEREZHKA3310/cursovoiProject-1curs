import profile

from django.urls import path
from . import views


urlpatterns = [
    path('', views.authorisation, name='authorisation'),
    path('registration', views.registration, name='registration')
]