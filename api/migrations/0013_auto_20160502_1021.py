# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_offer_accepted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='user',
            new_name='keeper',
        ),
    ]