# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_make_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Product Feature',
                'verbose_name_plural': 'Product Features',
            },
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', sorl.thumbnail.fields.ImageField(upload_to='product_pictures', blank=True, null=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'verbose_name': 'Product Picture',
                'verbose_name_plural': 'ProductPicturess',
            },
        ),
        migrations.RemoveField(
            model_name='productpictures',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductPictures',
        ),
    ]
