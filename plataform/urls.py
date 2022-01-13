from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<str:id>', views.product, name="product")
]
