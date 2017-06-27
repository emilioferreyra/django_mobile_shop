# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170619_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('ini_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'verbose_name_plural': 'Offers',
                'verbose_name': 'Offer',
            },
        ),
    ]
