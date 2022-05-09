from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField( max_length=11, verbose_name='Телефон')
    email = models.EmailField()
