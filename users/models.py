from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/%Y/%m', verbose_name='Аватар', null=True, blank=True)
    sub_to_newsletter = models.BooleanField(default=True, verbose_name='Подписаться на рассылку')
