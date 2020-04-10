from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activity/', views.activity, name='activity'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('developers/', views.dev, name='dev'),
    path('downloads/', views.downloads, name='downloads'),
    path('facts/', views.facts, name='facts'),
    path('test/', views.test, name='test'),
] 
