from django.contrib.auth.models import AbstractUser 
from django.db import models


class CustomUser(AbstractUser):
  address = models.CharField(max_length=250, blank=True)
  city = models.CharField(max_length=250, blank=True)
  postCode = models.CharField(max_length=10, blank=True)
  country = models.CharField(max_length=200, blank=True)
  phone = models.IntegerField(blank=True, default=0)
  shippingName = models.CharField(max_length=250, blank=True)
  shippingAddress = models.CharField(max_length=250, blank=True)
  shippingCity = models.CharField(max_length=250, blank=True)
  shippingPostcode = models.CharField(max_length=10, blank=True)
  shippingCountry = models.CharField(max_length=200, blank=True)
  deliveryPhone = models.IntegerField(blank=True, default=0)
  monday = models.BooleanField(default=False)
  tuesday = models.BooleanField(default=False)
  wednesday = models.BooleanField(default=False)
  thursday = models.BooleanField(default=False)
  friday = models.BooleanField(default=False)
  saturday = models.BooleanField(default=False)
