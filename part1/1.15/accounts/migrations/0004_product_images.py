# Generated by Django 3.1.2 on 2021-02-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210213_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
