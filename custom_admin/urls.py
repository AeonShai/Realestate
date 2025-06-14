# custom_admin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ilan_list, name='ilan_list'),  # İlanlar listelenecek
    path('add/', views.ilan_add, name='ilan_add'),  # İlan ekleme
    path('edit/<int:pk>/', views.ilan_edit, name='ilan_edit'),  # İlan düzenleme
    path('delete/<int:pk>/', views.ilan_delete, name='ilan_delete'),  # İlan silme
]
