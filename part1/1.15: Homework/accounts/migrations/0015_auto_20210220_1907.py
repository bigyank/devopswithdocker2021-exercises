# Generated by Django 3.1.2 on 2021-02-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210218_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='SmallDescription',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='delivery_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='descriptions',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
