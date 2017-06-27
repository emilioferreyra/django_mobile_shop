# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20170623_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='comment',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='reviews',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='stars',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
