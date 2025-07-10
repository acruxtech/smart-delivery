from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy


class Role(models.TextChoices):
    CUSTOMER = 'customer', gettext_lazy('Customer')
    COURIER = 'courier', gettext_lazy('Courier')


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)                                  # for customer
    current_location = models.CharField(max_length=100, blank=True)         # for courier

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def is_courier(self):
        return self.role == Role.COURIER
