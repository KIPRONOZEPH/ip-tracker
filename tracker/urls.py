from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('track/', views.track_ip, name='track_ip'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]