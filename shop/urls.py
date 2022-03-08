from django.urls import path
from .views import (
    add_product, 
    cart, 
    home, 
    checkout, 
    user_shops_list, 
    shop_dashboard,
    delete_product,
    update_cart
)

urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('product/add/<str:shop_name>', add_product, name='add_product'),
    path('product/delete/<int:product_id>', delete_product, name='delete_product'),
    path('shops/', user_shops_list, name='shops'),
    path('shop/<str:shop_name>', shop_dashboard, name='shop_dashboard'),
    path('update_cart/', update_cart, name='update_cart'),
]