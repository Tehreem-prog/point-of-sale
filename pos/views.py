# Create your views here.
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def products(request):
    products = Product.objects.raw('select * from pos_product')
    return render(request, 'pages/products.html', {'products':products})

def aboutus(request):
    return render(request, 'pages/aboutus.html')

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

def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        print('Is form Valid?', form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            product = form.save(commit=False)
            product.save()
            return redirect('/dashboard/products')
        # else:
        #     print(form.errors)
    else:
        form = ProductForm(instance=product)

    return render(request, 'pages/edit_product.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/dashboard/products')

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'pages/product_detail.html', {'product': product})

def product_add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + 1
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect('/dashboard/products')

def cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, 'pages/cart.html', {'products': products, 'cart': cart})

def cart_delete(request, id):
    cart = request.session.get('cart', {})
    del cart[str(id)]
    request.session['cart'] = cart
    return redirect('/dashboard/cart')

def cart_update(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = int(request.POST['quantity'])
    request.session['cart'] = cart
    return redirect('/dashboard/cart')

def cart_checkout(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, 'pages/checkout.html', {'products': products, 'cart': cart})

def cart_checkout_complete(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    for product in products:
        product.quantity = product.quantity - cart[str(product.id)]
        product.save()
    request.session['cart'] = {}
    return redirect('/dashboard/products')




