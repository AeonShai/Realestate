# custom_admin/forms.py

from django import forms
from .models import Ilan

class IlanForm(forms.ModelForm):
    class Meta:
        model = Ilan
        fields = ['title', 'description', 'price']
