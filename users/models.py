from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager, Role


class CustomUser(AbstractUser):

    email = models.EmailField(
        'email',
        unique=True
    )
    bio = models.TextField(
        max_length=500,
        blank=True
    )
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )
    objects = CustomUserManager()

    class Meta:
        ordering = ['username']

    @property
    def is_moderator(self):
        return self.role == Role.MODERATOR

    @property
    def is_admin(self):
        return self.role == Role.ADMIN
