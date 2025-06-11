from django.urls import path
from .views import CategoryListView, CategoryDetailView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'shop'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:id>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:id>/<slug:slug>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:id>/<slug:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]