# Generated by Django 4.2 on 2023-05-25 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mkart', '0008_trending_kids_trending_man_trending_woman'),
    ]

    operations = [
        migrations.DeleteModel(
            name='trending_kids',
        ),
        migrations.DeleteModel(
            name='trending_man',
        ),
        migrations.DeleteModel(
            name='trending_woman',
        ),
    ]
