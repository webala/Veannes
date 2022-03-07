from django.urls import path
from .views import cart, home, checkout

urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout')
]