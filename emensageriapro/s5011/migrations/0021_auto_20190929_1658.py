# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-29 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s5011', '0020_auto_20190620_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='tpinscprop',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF')], null=True),
        ),
    ]
