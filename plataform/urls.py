from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/add/<str:id>', views.cart, name='cart_add'),
    path('cart/inc/<str:id>', views.item_increment, name='item_increment'),
    path('cart/del/<str:id>', views.item_decrement, name='item_decrement'),
    path('cart/detail', views.cart_detail, name='cart_detail')
]
