from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager 
from django.contrib.auth.hashers import make_password
# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
    


class User(AbstractUser):
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()