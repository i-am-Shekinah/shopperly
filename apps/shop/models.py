from django.db import models
from django.utils.text import slugify

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(max_length=100, unique=True)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'
    ordering = ['name']

  def __str__(self):
    return self.name
  
  @property
  def available_products(self):
    return self.products.filter(is_available=True).count()

class Product(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100, unique=True)
  description = models.TextField(blank=True, null=True)
  image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.PositiveIntegerField(default=0)
  is_available = models.BooleanField(default=True)
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'
    ordering = ['name']
    indexes = [
      models.Index(fields=['id', 'slug'], name='product_id_slug_idx'),
    ]

  def __str__(self):
    return self.name