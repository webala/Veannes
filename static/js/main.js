
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

        updateCart(action, productId);
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