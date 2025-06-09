from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product


class CategoryListView(ListView):
  model = Category
  template_name = 'shop/category_list.html'
  context_object_name = 'categories'

class CategoryDetailView(DetailView):
  model = Category
  template_name = 'shop/category_detail.html'
  context_object_name = 'category'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['products'] = Product.objects.filter(category=self.object, is_available=True).select_related('category')
    return context


class ProductListView(ListView):
  model = Product
  template_name = 'shop/product_list.html'
  context_object_name = 'products'
  paginate_by = 10

  def get_queryset(self):
    return Product.objects.filter(is_available=True).select_related('category')
  
class ProductDetailView(DetailView):
  model = Product
  template_name = 'shop/product_detail.html'
  context_object_name = 'product'

  def get_queryset(self):
    return Product.objects.filter(
      id=self.kwargs.get('id'),
      slug=self.kwargs.get('slug'),
      is_available=True
      ).select_related('category')
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['related_products'] = Product.objects.filter(category=self.object.category, is_available=True).exclude(id=self.object.id)[:4]
    return context