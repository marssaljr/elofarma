from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pills as Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

def home(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category = request.GET.getlist('category')
    search = request.GET.get('q')
    if search:
        search = search.capitalize() 
        medicines = Product.objects.filter(name__icontains=search)    
    else:
        medicines = Product.objects.all()
    return render(request, 'home.html', {'medicines': medicines})

@login_required(login_url="/auth/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/auth/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/auth/login")
def cart(request, id):
    cart = Cart(request)
    if(cart):
        return redirect("item_increment", id=id)
    else:
        return redirect("cart_add", id=id)


@login_required(login_url="/auth/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/auth/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/auth/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="/auth/login")
def cart_detail(request):
    return render(request, 'cart.html')