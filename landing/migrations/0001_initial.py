# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-02 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('registrationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
