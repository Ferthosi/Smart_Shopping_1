from django.urls import path
from . import views
from .views import add_cart, cart

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
    #path('cart_error/', views.cart_error, name='cart_error'),
    path('checkout/', views.checkout, name='checkout'),
]
