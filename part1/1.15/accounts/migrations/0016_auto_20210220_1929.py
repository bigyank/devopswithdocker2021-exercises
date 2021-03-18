# Generated by Django 3.1.2 on 2021-02-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210220_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='doctor',
            new_name='docfield',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='SmallDescription',
            new_name='smalldescription',
        ),
        migrations.AddField(
            model_name='doctor',
            name='docname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
