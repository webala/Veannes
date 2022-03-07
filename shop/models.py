from django.db import models
from django.contrib.auth.models import User
from accounts.models import Vendor

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    products_type = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=200)
    estate = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)