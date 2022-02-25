from django.urls import path
from .views import cart, home

urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart, name='cart')
]