# Generated by Django 3.1.2 on 2021-02-17 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210217_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='Phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='Province',
            new_name='province',
        ),
    ]
