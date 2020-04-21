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
    path('mis/', views.mis, name="mis"),
    path('mis/submitted/', views.mis_success, name="mis_success"),
    path('mis/list/', views.mis_list, name="mis_list"),
    path('mis/person/<int:pk>', views.mis_indi, name="mis_person")
] 
