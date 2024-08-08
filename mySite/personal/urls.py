# personal/urls.py
from django.urls import path
from . import views

app_name = 'personal'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
]
