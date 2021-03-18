from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer


def customer_userprofile(sender,instance , created, **kwargs):
    if created:
        group = Group.objects.get(name = "customers")
        instance.groups.add(group)
        Customer.objects.create(
            user= instance,
            name= instance.username,
            email= instance.email,
        )
        print('Done')

post_save.connect(customer_userprofile, sender= User )
