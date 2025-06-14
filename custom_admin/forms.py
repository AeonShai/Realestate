# custom_admin/forms.py

from django import forms
from .models import Ilan

class IlanForm(forms.ModelForm):
    class Meta:
        model = Ilan
        fields = ['title', 'description', 'price']
    
    # Custom validation (isteğe bağlı)
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Fiyat sıfırdan büyük olmalıdır.')
        return price
