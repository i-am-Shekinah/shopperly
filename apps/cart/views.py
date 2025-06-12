from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView
from .utils import add_item_to_cart
from .models import Cart, CartItem
from apps.shop.models import Product
from django.shortcuts import get_object_or_404

class AddToCartView(LoginRequiredMixin, View):
  def post(self, request, *args, **kwargs):
    product_id = kwargs.get('product_id')
    quantity = request.POST.get('quantity', 1)

    product = get_object_or_404(Product, id=product_id)
    add_item_to_cart(request.user, product_id, quantity, price=product.price)

    return redirect('cart:cart_detail')
    

class CartDetailView(LoginRequiredMixin, ListView):
  model = Cart
  template_name = 'cart/cart_detail.html'
  context_object_name = 'cart'
  
  
  def get_queryset(self):
    return Cart.objects.filter(user=self.request.user).prefetch_related('items__product')
  

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    
    cart = Cart.objects.filter(user=self.request.user).first()
    if cart:
      cart_items = cart.items.select_related('product')
      total_price = sum(item.price * item.quantity for item in cart_items)
    else:
      cart_items = []
      total_price = 0.0

    context['cart'] = cart
    context['cart_items'] = cart_items
    context['total_price'] = total_price
    return context