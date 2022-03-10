from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    products_type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    price =models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            return getattr(self.image, 'url', None)
        return None


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)

    @property
    def get_cart_items(self):
        cart_items = self.cartitem_set.all()
        return sum([item.quantity for item in cart_items])

    @property
    def get_cart_total(self):
        return sum([item.get_item_total for item in self.cartitem_set.all()])


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_item_total(self):
        return self.quantity * self.product.price


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=200)
    estate = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)