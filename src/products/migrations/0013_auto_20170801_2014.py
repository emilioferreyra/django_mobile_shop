# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20170701_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='stars',
        ),
        migrations.AddField(
            model_name='offer',
            name='rating',
            field=models.PositiveSmallIntegerField(default=4, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=False,
        ),
    ]
