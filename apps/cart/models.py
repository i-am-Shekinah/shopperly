from django.db import models
from django.conf import settings

class Cart(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user.username}'s Cart"

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
  product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  price = models.DecimalField(max_digits=10, decimal_places=2)

  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['cart', 'product'],
        name='unique_cart_item'
      )
    ]

  def __str__(self):
    return f"{self.product.name} x {self.quantity}"