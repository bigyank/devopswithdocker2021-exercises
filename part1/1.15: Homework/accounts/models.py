from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.db.models.fields import DecimalField
# Create your models here.
PRODUCT_CATEGORIES = [('Personal Care', 'Personal Care'), ('Family Care', 'Family Care'),
                      ('Fitness and Suppliments', 'Fitness and Suppliments'), ('Pharmacy', 'Pharmacy')]

SEX = [('Male', 'male'), ('Female', 'female'), ('Other', 'other')]

DOCTOR_CATAGORIES = []

class Doctor(models.Model):
    docname = models.CharField(max_length=50, null=True, blank=True)
    docfield = models.CharField(
        max_length=50, null=True, blank=True)  # specializations
    experience = models.CharField(max_length=50, null=True, blank=True)
    images = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    research_journals = models.CharField(max_length=500, null=True, blank=True)
    awards = models.CharField(max_length=500, null=True, blank=True)
    study = models.CharField(max_length=500, null=True, blank=True)
    phone = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    websitelink = models.URLField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    facebook = models.URLField(max_length=50, null=True)

    def __str__(self):
        return self.docname + ' ' + str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url


class DoctorAppointment (models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=30, null=True)
    phone = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    sex = models.CharField(choices=SEX, max_length=6)
    descriptions = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.name


class Ambulance (models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=30, null=True)
    descriptions = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    # On_delete deletes user if user item is deleted
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=30, null=True)
    phone_number = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    descriptions = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=24, choices=PRODUCT_CATEGORIES)
    smalldescription = models.CharField(max_length=300, null=True)
    images = models.ImageField(null=True, blank=True)
    delivery_date = models.DateTimeField(auto_now_add=True, null=True)
    prescribedmed = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name + ' ' + str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    uploadpres = models.ImageField(null=True, blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transcation_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url

    # def __str__(self):
    #     return str(self.customer)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.prescribedmed == False:
                shipping = True
        return shipping


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL,  blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    # if order gets deleted then also the shipmnet info remains
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL,  blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=50, null=True)
    phonenumber = models.DecimalField(
        max_digits=10, decimal_places=0, null=True)
    added_date = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.address
