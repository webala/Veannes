import json
from .models import Product, Cart

def cookieCart(request):
    try:
        cart_cookie = json.loads(request.COOKIES['cart'])
    except:
        cart_cookie = {}

    items = []
    cart = {'get_cart_items':0, 'get_cart_total': 0}

    
    for item in cart_cookie:
        product = Product.objects.get(id=item)
        total = product.price * cart_cookie[item]['quantity']

        cart['get_cart_items'] += cart_cookie[item]['quantity']
        cart['get_cart_total'] += total

        cart_item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'image_url': product.image_url
            },
            'quantity': cart_cookie[item]['quantity'],
            'get_item_total': total
        }

        items.append(cart_item)

    return {'cart': cart, 'items': items}


def cart_data(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, complete=False)
        items = cart.cartitem_set.all()
    else:
        cookieData = cookieCart(request)
        items = cookieData['items']
        cart = cookieData['cart']
    
    return {'cart': cart, 'items': items}