from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom User model """
    tg_chat_id = models.CharField(max_length=15, verbose_name="ID telegram chat", null=True, blank=True)
