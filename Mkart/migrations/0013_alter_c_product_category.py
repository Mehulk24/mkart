# Generated by Django 4.2 on 2023-06-02 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mkart', '0012_alter_c_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_product',
            name='category',
            field=models.CharField(choices=[('Man', 'man-product'), ('Woman', 'woman-product'), ('Kids', 'kids-product')], default=' ', max_length=50),
        ),
    ]
