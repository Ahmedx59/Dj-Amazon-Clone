# Generated by Django 5.1 on 2024-10-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_after_coupon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
