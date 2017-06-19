# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import audit_log.models.fields
import localflavor.us.models
from django.conf import settings
import sorl.thumbnail.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(null=True, max_length=40, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(null=True, max_length=40, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(null=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.EmailField(verbose_name='e-mail', blank=True, max_length=254)),
                ('phone_number', localflavor.us.models.PhoneNumberField(help_text='999-999-9999')),
                ('address', models.TextField(null=True, blank=True)),
                ('picture', sorl.thumbnail.fields.ImageField(null=True, upload_to='people_pictures', blank=True)),
                ('status_active', models.BooleanField(default=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_people_person_set', null=True, editable=False, verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_people_person_set', null=True, editable=False, verbose_name='modified by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Persons',
                'verbose_name': 'Person',
            },
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Person Types',
                'verbose_name': 'Person Type',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='person_type',
            field=models.ForeignKey(to='people.PersonType'),
        ),
    ]
