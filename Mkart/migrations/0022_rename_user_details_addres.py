# Generated by Django 4.2.1 on 2023-08-25 06:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Mkart', '0021_alter_user_details_address_alter_user_details_city_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_details',
            new_name='addres',
        ),
    ]