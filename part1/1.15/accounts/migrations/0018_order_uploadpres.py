# Generated by Django 3.1.2 on 2021-02-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_doctor_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='uploadpres',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
