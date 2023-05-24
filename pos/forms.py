from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'quantity', 'price')

class OredrlineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ('order','product', 'quantity', 'price')
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('total_bill',)
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer','total_price',)

