# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='ini_date',
            new_name='start_date',
        ),
    ]
