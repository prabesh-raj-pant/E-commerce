# Generated by Django 5.0 on 2024-01-04 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='store.order'),
            preserve_default=False,
        ),
    ]
