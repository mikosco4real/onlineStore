# Generated by Django 3.1.4 on 2020-12-19 03:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20201218_2207'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Profile',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
    ]
