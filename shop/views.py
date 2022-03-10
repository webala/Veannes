from urllib import request
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from PIL import Image
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import AddProductForm
from .models import CartItem, Product, Shop, Cart
from .serializers import UpdateCartSerializer
from .utils import cart_data
# Create your views here.


def home(request):

    if request.user.is_authenticated:
        isVendor = bool(Shop.objects.filter(owner=request.user))
    else:
        isVendor = False

    products = Product.objects.all()
    context = {
        'isVendor': isVendor,
        'products': products
    }
    return render(request, 'shop/store.html', context)




def cart(request):
    cart_items = cart_data(request)

    context = {
        'cart_items': cart_items['items'],
        'cart': cart_items['cart']
    }
    return render(request, 'shop/cart.html', context)

def checkout(request):
    cart_items = cart_data(request)

    context = {
        'cart_items': cart_items['items'],
        'cart': cart_items['cart']
    }

    return render(request, 'shop/checkout.html', context)

def add_product(request, shop_name):
    form = AddProductForm(request.POST or None, request.FILES or None)

    shop = Shop.objects.filter(name=shop_name).first()

    if form.is_valid():
        obj = form.save(commit=False)
        obj.shop = shop
        obj.save()
        form = AddProductForm()

    context = {
        'form': form
    }
    
    return render(request, 'shop/add_product.html', context)

def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return HttpResponseNotFound('Product does not exist')
    
    product.delete()
    return HttpResponse('Product deleted')


def user_shops_list(request):
    current_user = request.user
    shops = list(Shop.objects.filter(owner=current_user))

    context = {
        'shops': shops
    }

    return render(request, 'shop/user_shops.html', context)

def shop_dashboard (request, shop_name):
    shop = Shop.objects.filter(name=shop_name).first()

    products = list(Product.objects.filter(shop=shop))

    context = {
        'shop': shop,
        'logo': shop.name[0],
        'products': products
    }

    if shop:
        return render(request, 'shop/shop_dashboard.html', context)
    else:
        return HttpResponseNotFound('Shop does not exist')

@api_view(['POST'])
def update_cart(request):
    serializer = UpdateCartSerializer(data=request.data)
    user = request.user

    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        action = data.get('action')
        product_id = data.get('productId')

        print('action', action, 'id', product_id)

        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=user, complete=False)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if action == 'add':
            cart_item.quantity += 1
        elif action == 'remove':
            cart_item.quantity -= 1

        cart_item.save()

        if cart_item.quantity <= 0 or action == 'delete':
            cart_item.delete()
        

        return Response('Cart item updated', 200)
    
    return Response('Something went wrong somewhere', 400)

