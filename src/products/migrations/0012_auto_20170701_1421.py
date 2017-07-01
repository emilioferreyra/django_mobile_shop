# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_offer_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model',
            field=smart_selects.db_fields.ChainedForeignKey(to='products.Model', chained_field='make', chained_model_field='make'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('make', 'model')]),
        ),
    ]
