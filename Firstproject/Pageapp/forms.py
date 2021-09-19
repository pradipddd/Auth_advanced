from django import forms
from django.forms import fields
from .models import Laptop

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'