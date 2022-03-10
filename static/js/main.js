
// get csrf token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

//update cart for authenticated user



updateBtns = Array.from(document.getElementsByClassName('update-cart'))

updateBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        var action = btn.dataset.action;
        var productId = btn.dataset.product
        console.log(user)
        if (user == 'AnonymousUser') {
            addCookieItem(action, productId);
        } else {
            updateCart(action, productId);
        }
    })
})

const updateCart = (action, productId) => {
    const data = {'action': action, 'productId': productId}
    console.log(data)
    const url = '/update_cart/';
    fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": 'application/json',
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {
        location.reload()
    })
    .catch(error => console.log(error));
}

//update cart for unauthenticated user

const getCartCookie = () => {  //Get cart cookie item
    let name = 'cart';
    var cookieArray = document.cookie.split(';');

    for (var i = 0; i < cookieArray.length; i++) {
        var cookiePair = cookieArray[i].split('=');

        if (name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}

var cart = JSON.parse(getCartCookie());

if (cart == undefined) {
    cart = {};
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
}

const addCookieItem = (action, productId) => {

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = {'quantity': 1};
        } else {
            cart[productId]['quantity'] += 1;
        }
    } else if (action == 'remove') {
        cart[productId]['quantity'] -= 1;

        if (cart[productId]['quantity'] <= 0) {
            delete cart[productId];
        } 
    } else if (action == 'delete') {
        delete cart[productId];
    }

    console.log(cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
    location.reload()
}