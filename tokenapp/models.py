from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.db.models.fields import IntegerField, TextField
from django.db.models.query_utils import PathInfo
from django.contrib.auth import authenticate

class MyUserManager(BaseUserManager):
    def create_user(self, username, password, email, phone_number, **extra_fields):
        use_in_migrations=True
        if not username:
            raise ValueError('Username is required here..!')

        if not email:
            raise ValueError('Email is required here..!')
        
        if not phone_number:
            raise ValueError('Phone number is required here..!')

        user = self.model(
            username = username,
            password = password,
            email=self.normalize_email(email),
            phone_number = phone_number,
        )

        user=MyUser.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, password,email,phone_number,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff True")

        return self.create_user(phone_number, password, **extra_fields)


class MyUser(AbstractUser):
    phone_number = models.CharField(max_length=12,unique=True)
    REQUIRED_FIELDS = ['phone_number','email']
