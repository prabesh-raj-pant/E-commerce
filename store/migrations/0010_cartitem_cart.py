# Generated by Django 5.0 on 2024-01-03 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_customer_first_name_customer_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.cart'),
            preserve_default=False,
        ),
    ]