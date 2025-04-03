from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('authorisation', views.authorisation, name='authorisation'),
    path('profile', views.profile, name='profile')
]