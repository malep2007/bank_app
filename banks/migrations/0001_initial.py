# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('branch location', models.CharField(max_length=50)),
            ],
        ),
    ]
