from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=200)
    products_type = models.CharField(max_length=200)

    



    


