# Generated by Django 5.1 on 2024-09-17 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_product_quantitity_product_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]