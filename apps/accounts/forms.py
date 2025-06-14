from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'profile_picture', 'bio')