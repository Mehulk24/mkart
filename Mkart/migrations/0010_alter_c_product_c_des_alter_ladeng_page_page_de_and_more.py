# Generated by Django 4.2 on 2023-06-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mkart', '0009_delete_trending_kids_delete_trending_man_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_product',
            name='c_des',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='ladeng_page',
            name='page_de',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='des',
            field=models.TextField(max_length=300),
        ),
    ]
