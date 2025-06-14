# custom_admin/admin.py

from django.contrib import admin
from .models import Ilan

@admin.register(Ilan)
class IlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')  # Hangi alanların listeleneceğini belirleyelim
    search_fields = ('title', 'description')  # Hangi alanlarda arama yapılabileceğini belirleyelim
    list_filter = ('price', 'created_at')  # Filtreleme seçenekleri ekleyelim
