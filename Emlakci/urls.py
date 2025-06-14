# Emlakci/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom_admin/', include('custom_admin.urls')),  # custom_admin'in URL'lerini dahil ettik
]
