from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'quantity', 'price')

# class OredrlineForm(forms.ModelForm):
#     class Meta:
#         model = OrderLine
#         fields = ('order','product', 'quantity', 'price')

