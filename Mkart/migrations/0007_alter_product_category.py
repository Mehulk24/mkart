# Generated by Django 4.2 on 2023-05-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mkart', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Man_tending_page', 'treding_man'), ('Woman_tending_page', 'treding_woman'), ('Kids_tending_page', 'treding_kids'), ('Man', 'man'), ('Woman', 'woman'), ('Kids', 'kids')], default=' ', max_length=50),
        ),
    ]
