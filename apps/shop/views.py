from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Product
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login

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


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
  model = Product
  template_name = 'shop/product_form.html'
  fields = ['name', 'description', 'price', 'category', 'image', 'stock', 'is_available']
  success_url = '/shop/products/'

  def test_func(self):
    return self.request.user.is_authenticated and ((self.request.user.is_staff) or (self.request.user.role == 'seller'))
  
  def handle_no_permission(self):
    if self.request.user.is_authenticated:
      return super().handle_no_permission()
    else:
      return redirect_to_login(self.request.get_full_path())

  def form_valid(self, form):
    form.instance.is_available = True
    form.instance.seller = self.request.user
    return super().form_valid(form)
  

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Product
  template_name = 'shop/product_form.html'
  fields = ['name', 'description', 'price', 'category', 'image', 'stock', 'is_available']

  def get_success_url(self):
    return reverse('shop:product_detail', kwargs={
      'id': self.object.id,
      'slug': self.object.slug
    })
  
  def test_func(self):
    return self.request.user.is_authenticated and ((self.request.user == self.get_object().seller) or self.request.user.is_staff)
  
  def handle_no_permission(self):
    if self.request.user.is_authenticated:
      return super().handle_no_permission()
    else:
      return redirect_to_login(self.request.get_full_path())
  

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Product
  template_name = 'shop/product_confirm_delete.html'
  
  def get_success_url(self):
    return reverse('shop:product_list')
  
  def test_func(self):
    return self.request.user.is_authenticated and ((self.request.user == self.get_object().seller) or self.request.user.is_staff)
  
  def handle_no_permission(self):
    if self.request.user.is_authenticated:
      return super().handle_no_permission()
    else:
      return redirect_to_login(self.request.get_full_path())