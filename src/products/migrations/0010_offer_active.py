# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170623_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
