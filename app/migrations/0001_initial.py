# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-05 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name=b'Address')),
                ('tel', models.IntegerField(blank=True, default=0, verbose_name=b'Tel')),
            ],
        ),
    ]
