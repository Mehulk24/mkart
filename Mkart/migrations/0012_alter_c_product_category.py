# Generated by Django 4.2 on 2023-06-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mkart', '0011_c_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_product',
            name='category',
            field=models.CharField(choices=[('Man', 'man'), ('Woman', 'woman'), ('Kids', 'kids')], default=' ', max_length=50),
        ),
    ]
