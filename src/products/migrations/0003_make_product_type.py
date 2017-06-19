# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='make',
            name='product_type',
            field=models.ForeignKey(default=1, to='products.ProductType'),
        ),
    ]
