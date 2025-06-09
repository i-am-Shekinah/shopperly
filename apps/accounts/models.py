from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  ROLE_CHOICES = (
    ('buyer', 'Buyer'),
    ('seller', 'Seller'),
    ('admin', 'Admin')
  )
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField(unique=True)
  profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

  def __str__(self):
    return self.first_name