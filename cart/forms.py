from django import forms
from django.db.models import fields
from .models import Shipping

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['f_name', 'l_name', 'address', 'city', 'state', 'zipcode', 'email', 'contact']