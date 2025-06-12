from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'available_products', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    list_filter = ('created_at', 'updated_at')

  
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock', 'is_available', 'category', 'seller', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'category__name')
    list_filter = ('is_available', 'category', 'created_at', 'updated_at')
    list_editable = ('price', 'stock', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    # raw_id_fields = ('category',)
    date_hierarchy = 'created_at'
    autocomplete_fields = ('category',)