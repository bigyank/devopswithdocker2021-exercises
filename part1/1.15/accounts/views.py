from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sessions.models import Session
from django.views.generic.base import TemplateView
from .forms import AmbulanceForm, NewUserForm, DoctorAppointmentForm
from ecom.settings import EMAIL_HOST_USER
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.models import Group
# from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .util import cookieCart, cartData, guestOrder


@unauthenticated_user
def register_request(request):
    # if request.user.is_authenticated:
    # 	return redirect('home')    pachi loged in  user lai yesma access nadina ho yo
    # else":
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            user = form.save()

            if User.objects.filter(username-username).exists():
                messages.info(request, 'Sorry! Username already taken')
                return redirect('home')

            if len(username) < 10:
                messages.error(
                    request, " Your user name must be under 10 characters")
                return redirect('register')

            if (password1 != password2):
                messages.error(request, " Passwords do not match")
                return redirect('register')

            username = form.cleaned_data.get('username')
            login(request, user)
            messages.info(request, "You are now successfully registered.")
            return render(request, 'accounts/home.html')
    form = NewUserForm
    context = {"register_form": form, 'items': items,
               'order': order, 'cartItems': cartItems, 'shipping': False, }
    return render(request, "accounts/login&register/register.html", context)


@unauthenticated_user
def login_request(request):
    # if request.user.is_authenticated:
    # 	return redirect('home')    pachi loged in  user lai yesma access nadina ho yo
    # else":
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, "Welcome, " + username)

                # return render(request, "accounts/home.html")
                return redirect(home)
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False, 'login_form': form}
    return render(request, 'accounts/login&register/login.html', context)


def logout_request(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    logout(request)

    messages.info(request, "You are now sucessfully logged out!!")
    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False, }
    return render(request, "accounts/home.html", context)


def password_reset_request(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password/password_reset_email.txt"
                    cred = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'E-Pharma',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, cred)
                    try:
                        send_mail(subject, email, 'bhatta.abishek11@gmail.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    # return render(request,' password_reset/done/')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    context = {" password_reset_form": password_reset_form, 'items': items,
               'order': order, 'cartItems': cartItems, 'shipping': False, }
    return render(request, "accounts/password/password_reset.html/", context)


# def password_reset_request_de(request):
#     if request.method == "POST":
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data['email']
#             associated_users = User.objects.filter(Q(email=data))
#             if associated_users.exists():
#                 subject = request.POST.get('subject', 'Password reset')
#                 messages = request.POST.get('message', 'Hey')
#                 recepient = str(sub['Email'].value())
#                 send_mail (subject, messages, EMAIL_HOST_USER, [recepient], fail_silently= False )
#                 return  redirect("/password_reset/done/")
#     password_reset_form = PasswordResetForm()
#     return render(request, "accounts/password/password_reset.html/", context={"password_reset_form": password_reset_form})


def home(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'accounts/home.html', context)


# @login_required(login_url='login')
def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order,  'cartItems': cartItems}
    return render(request, 'accounts/cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False}
    return render(request, 'accounts/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    # get and create cause i need to update if item already exist
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item has been added", safe=False)


def processOrder(request):
    transcation_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transcation_id = transcation_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            province=data['shipping']['province'],
            # phonenumber=data['shipping']['phonenumber'],


        )
    return JsonResponse("Process Complete! Item deleivered soon", safe=False)


def product(request, id):
    item = Product.objects.all()
    pro_id = Product.objects.get(id=id)
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False, 'pro_id': pro_id, 'products_item': item}  # 'products': products
    return render(request, 'accounts/products/product.html', context)


def ambulance(request):
    ambulanceform = AmbulanceForm()

    if request.method == 'POST':
        print(request.POST)
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'ambulanceform': ambulanceform, 'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False}
    return render(request, 'accounts/ambulance.html', context)


def doctor(request):
    doctors = Doctor.objects.all()

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False, 'doctors': doctors, }
    return render(request, 'accounts/doctor/doctor.html', context)


def doctorprofile(request, id):
    doctor_id = Doctor.objects.get(id=id)
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.method == 'POST':
        print(request.POST)
        form = DoctorAppointmentForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False, 'doctor': doctor_id, 'DoctorAppointmentForm': DoctorAppointmentForm}
    return render(request, 'accounts/doctor/doctor-profile.html', context)


# def searchpage(request):
#     search=request.GET['query']
#     products = product.objects.filter(name__icontains= search)

#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']


#     context = {'items': items, 'order': order,
#                'cartItems': cartItems, 'shipping': False, 'products':products ,'search':search }
#     return render(request, 'searchpage.html', context)

class SearchResultsView(TemplateView):
    template_name = 'accounts/searchpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # the bigger GET is the method whereas the small get is the function avaibale in python for dictionary objects.
        kword = self.request.GET.get('keyword')
        results = Product.objects.filter(Q(name__icontains= kword))  
        # Q lay chai it makes the search easier as name ra desciptions bata ni seach garna micha it acts like the or statment
        # the Q object is used ti make complex queries with simple code 
        # the icontains search the product whose name contain any of the kword
        context= {'results':results}
        
        return context

