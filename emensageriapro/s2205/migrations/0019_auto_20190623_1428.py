# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-23 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2205', '0018_auto_20190620_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2205brasil',
            name='codmunic',
            field=models.IntegerField(null=True),
        ),
    ]
