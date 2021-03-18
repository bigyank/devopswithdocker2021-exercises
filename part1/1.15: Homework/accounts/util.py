import json

from django.http import request
from .models import *

# This file is made to make the views more clean


def cookieCart(request):   #store the cookie information of the guest user to add items to the cart
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print("Cart:", cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']
    for i in cart:
        try:  # let the user shop if the desired product is not in the cart
            cartItems += cart[i]["quantity"]
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {'product': {'id': product.id,
                                'name': product.name,
                                'price': product.price,
                                'imageURL': product.imageURL},
                    'quantity': cart[i]['quantity'], 
                    'get_total': total, 
                    }
            items.append(item)
            if product.prescribedmed == False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):  # handles the logic for authenticated and non authenticaed user  

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        # get all order item that  has the parent element order
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    print('User not logged in')

    print("cookies", request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )
    # seting the user in database
    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order
