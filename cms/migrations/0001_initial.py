# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-02 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('publisher', models.CharField(blank=True, max_length=255, verbose_name=b'Publisher')),
                ('page', models.IntegerField(blank=True, default=0, verbose_name=b'PageNum')),
            ],
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name=b'Comment')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impressions', to='cms.Book', verbose_name=b'Book')),
            ],
        ),
    ]