# Create your views here.
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def products(request):
    products = Product.objects.raw('select * from pos_product')
    return render(request, 'pages/products.html', {'products':products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print('Is form Valid?', form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            product = form.save(commit=False)
            product.save()
            return redirect('/dashboard/products')
        # else:
        #     print(form.errors)
    else:
        form = ProductForm()

    return render(request, 'pages/add_product.html', {'form': form})


def dashboard(request):
    return render(request, 'pages/dashboard.html')



