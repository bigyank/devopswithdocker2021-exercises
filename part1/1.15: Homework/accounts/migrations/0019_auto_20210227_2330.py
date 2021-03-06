# Generated by Django 3.1.2 on 2021-02-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_order_uploadpres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('p', 'Personal Care'), ('f', 'Family Care'), ('fs', 'Fitness and Suppliments'), ('p', 'Pharmacy')], max_length=2),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='phonenumber',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
