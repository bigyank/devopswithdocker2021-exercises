# Generated by Django 3.1.2 on 2021-02-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20210220_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
