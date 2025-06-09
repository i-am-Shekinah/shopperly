# from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class UserRegisterView(CreateView):
  form_class = CustomUserCreationForm
  template_name = 'accounts/register.html'
  success_url = reverse_lazy('login')


class UserLoginView(LoginView):
  template_name = 'accounts/login.html'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('home')  
  
class UserLogoutView(LogoutView):
  next_page = reverse_lazy('home')
  