# Generated by Django 3.1.2 on 2021-02-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210217_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='Phonenumber',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
