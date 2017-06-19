# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20161118_2229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productpicture',
            options={'verbose_name_plural': 'Product Pictures', 'verbose_name': 'Product Picture'},
        ),
    ]
