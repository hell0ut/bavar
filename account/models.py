from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class AccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, cellphone):

        if not email or not cellphone or not first_name or not last_name:
            raise ValueError('There`s an empty required field. Please, fill it and try again.')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            cellphone=cellphone,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password, cellphone):

        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            cellphone=cellphone,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save()

        return user


class Account(AbstractUser):
    username = None
    email = models.EmailField(unique=True)     # do we really need it??
    cellphone = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_joined = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'cellphone'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = AccountManager()

    def __str__(self):
        return f'Клиент {self.first_name} {self.last_name}. Телефон - {self.cellphone}'



