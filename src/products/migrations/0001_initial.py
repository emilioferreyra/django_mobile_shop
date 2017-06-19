# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import audit_log.models.fields
from django.conf import settings
import sorl.thumbnail.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Makes',
                'verbose_name': 'Make',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('make', models.ForeignKey(to='products.Make')),
            ],
            options={
                'verbose_name_plural': 'Models',
                'verbose_name': 'Model',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, max_length=40, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, max_length=40, editable=False)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(verbose_name='created by', editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='created_products_product_set')),
                ('make', models.ForeignKey(to='products.Make')),
                ('model', models.ForeignKey(to='products.Model')),
                ('modified_by', audit_log.models.fields.LastUserField(verbose_name='modified by', editable=False, null=True, to=settings.AUTH_USER_MODEL, related_name='modified_products_product_set')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'verbose_name': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductPictures',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('picture', sorl.thumbnail.fields.ImageField(null=True, blank=True, upload_to='product_pictures')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'verbose_name_plural': 'ProductPicturess',
                'verbose_name': 'ProductPictures',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'ProductTypes',
                'verbose_name': 'ProductType',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(to='products.ProductType'),
        ),
    ]
