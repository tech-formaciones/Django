from django import forms
from .models import Customer

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'CustomerID': forms.TextInput(attrs={'class': 'form-control'}),
            'CompanyName': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field in self.fields.values():
                field.widget.attrs.update({'class': 'form-control'})