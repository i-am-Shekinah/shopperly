from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  model = CustomUser
  add_form = CustomUserCreationForm
  list_display = ('first_name', 'last_name', 'email', 'username', 'is_staff', 'is_active', 'date_joined')
  list_filter = ('is_staff', 'is_active', 'role')
  search_fields = ('email', 'username', 'first_name', 'last_name')
  ordering = ('first_name',)

  fieldsets = (
    ('Personal Info', {
        'fields': ('first_name', 'last_name', 'email', 'username', 'profile_picture', 'bio', 'role'),
    }),
    ('Permissions', {
        'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
    }),
    ('Important Dates', {
        'fields': ('last_login', 'date_joined'),
    }),
  )

  add_fieldsets = (
      ('Personal Info', {
          'classes': ('wide',),
          'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'profile_picture', 'bio', 'role'),
      }),
      ('Permissions', {
        'classes': ('wide',),
        'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions'),
      })
  )

