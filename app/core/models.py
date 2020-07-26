from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, **extra_fields):

        '''create and save a new user with the given email'''

        if not email:
            raise ValueError('Email Field is Required!')

        if not name:
            raise ValueError('Name Field is Required!')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_super_user(self, email, name=None, password=None):

        '''create and save a new superuser with the given email'''
        if not name:
            name = email.split('@')[0]

        user = self.create_user(
            email=email,
            name=name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        max_length=255,
        unique=True
    )
    name = models.CharField(
        max_length=255
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
