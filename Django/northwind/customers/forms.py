from django import forms
from .models import Customers

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'