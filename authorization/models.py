from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, default="")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
