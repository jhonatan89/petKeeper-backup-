# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 04:32
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20160502_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(default='', upload_to=api.models.upload_to_profile, verbose_name='logo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='picture',
            field=models.ImageField(default='', upload_to=api.models.upload_to_pet, verbose_name='logo'),
            preserve_default=False,
        ),
    ]
