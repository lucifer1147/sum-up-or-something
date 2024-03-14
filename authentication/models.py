from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import CustomUserManager

def upload_to(instance, filename):
    return f'images/{filename}'

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    description = models.TextField(default="not-set")

    profile_photo = models.ImageField(default="Media/Generic-Profile-Image.png", upload_to=upload_to)

    first_name = models.CharField(max_length=20, default="not-set")
    last_name = models.CharField(max_length=20, default="not-set")

    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'description', 'is_staff', 'profile_photo']
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email
