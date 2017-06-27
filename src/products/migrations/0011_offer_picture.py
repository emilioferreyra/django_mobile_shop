# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_offer_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='product_pictures', null=True),
        ),
    ]
