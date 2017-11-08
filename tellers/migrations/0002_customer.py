# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('phone number', models.CharField(max_length=10)),
                ('account number', models.CharField(max_length=50)),
            ],
        ),
    ]
