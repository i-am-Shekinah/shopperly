from django.urls import path, include

from .views import UserRegisterView, UserLoginView, UserLogoutView

app_name = 'accounts'

urlpatterns = [
  path('register/', UserRegisterView.as_view(), name='register'),
  path('login/', UserLoginView.as_view(), name='login'),
  path('logout/', UserLogoutView.as_view(), name='logout'),
]