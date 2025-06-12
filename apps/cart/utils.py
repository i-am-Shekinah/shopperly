from .models import Cart, CartItem
from apps.shop.models import Product
from django.shortcuts import get_object_or_404


def get_or_create_user_cart(user):
  cart, _ = Cart.objects.get_or_create(user=user)
  return cart

def add_item_to_cart(user, product_id, quantity=1, price=None):
  quantity = int(quantity)
  cart = get_or_create_user_cart(user)
  product = get_object_or_404(Product, id=product_id)
  cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity, 'price': price or product.price})
  
  if not created:
    cart_item.quantity += quantity
  else:
    cart_item.quantity = quantity
  
  if cart_item.quantity > product.stock:
    cart_item.quantity = product.stock 
  

  cart_item.save()
  return cart_item