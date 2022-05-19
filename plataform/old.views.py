from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pills
from cart.cart import Cart

# Create your views here.
def home(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category = request.GET.getlist('category')
    search = request.GET.get('q')


    if search:
        search = search.capitalize() 
        medicines = Pills.objects.filter(name__icontains=search)
    # # medicines = Pills.objects.all()
    # if min_price or max_price or category:
    #     if not min_price:
    #         min_price = 0
    #     if not max_price:
    #         max_price = 99999999
    #     if not category:
    #         category = ['G','S']


    #     medicines = Pills.objects.filter(price__gte=min_price)\
    #     .filter(price__lte=max_price)\
    #     .filter(category__in=category)
    else:
        medicines = Pills.objects.all()
    return render(request, 'home.html', {'medicines': medicines})

def product(request, id):
    product = get_object_or_404(Pills, id=id)
    suggestions = Pills.objects.filter(category=product.category).exclude(id=id)[:2]
    return render(request, 'product.html', {'product': product, 'suggestions': suggestions})

@login_required(login_url="/auth/login")
def add_to_cart(request, id):
    product = Pills.objects.get(id=id)
    cart = Cart(request)
    quantity = 1
    cart.add(product, product.price, quantity)

@login_required(login_url="/auth/login")
def remove_from_cart(request, product_id):
    product = Pills.objects.get(id=id)
    cart = Cart(request)
    cart.remove(product)

@login_required(login_url="/auth/login")
def get_cart(request):
    return render(request, 'cart.html', {'cart': Cart(request)})

# @login_required(login_url="/auth/login")
# def add_cart(request, id):
#     products = get_object_or_404(Pills, id=id)
#     order_item, created = OrderItem.objects.get_or_create(
#         user=request.user,
#         item=products,
#     )

#     cart = Cart.objects.filter(user=request.user, products=order_item, ordered=False)

#     if cart.exists():
#         order = cart[0]
#         if order.products.filter(item__id=products.id).exists():
#             order_item.quantity += 1
#             order_item.save()
#         else:
#             order.products.add(order_item)
#     else:
#         order = Cart.objects.create(
#             user=request.user,
#         )
#         order.products.add(order_item)
#         print("done")
#     return redirect('cart')

# @login_required(login_url="/auth/login")
# def remove_cart(request, id):
#     item = get_object_or_404(Pills, id=id)
#     order_item = get_object_or_404(OrderItem, user=request.user, item=item)
#     order_qs = Cart.objects.filter(user=request.user, ordered=False)
#     print('order_qs ',order_qs)
#     print('order_item ',order_item)
#     if order_qs.exists():
#         order = order_qs[0]
#         print('order now ',order)
#         if (order_item):
#             if order.products.filter(item__id=item.id).exists():                                    
#                 order_item.quantity -= 1
#                 if (order_item.quantity < 1):                    
#                     order_item.delete()
#                     order.products.filter(item__id=item.id).delete()
#                     print(f'order {order}, orderitem: {order_item}')
#                 order_item.save()
#                 print('-1')
#         else:
#             print('cu')
#     else:
#         order = Cart.objects.delete(user=request.user)
#         order.products.delete(order_item)
#         print("done")
#     return redirect('cart')

# @login_required(login_url='/auth/login')
# def cart(request):
#     order_item = OrderItem.objects.filter(
#         user_id=request.user.id
#     )
#     print(order_item)
#     items = []
#     nums = []
#     for ordered in order_item:
#         print(ordered.quantity)
#         if (ordered.quantity > 0):
#             if not(str(ordered.item_id) in nums):
#                 pill = Pills.objects.filter(id=ordered.item_id)
#                 print(pill)            
#                 if (len(pill) > 0):                
#                     items.append(pill)
#                     nums.append(str(ordered.item_id))
#                     print(nums)
#     return render(request, 'cart.html', {'items': items, 'order_item': order_item})

