from django.contrib import admin

from shop.models import Product, Shop, Cart, CartItem

# Register your models here.
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)