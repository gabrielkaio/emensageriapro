# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1280', '0012_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1280infoativconcom',
            name='fator13',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1280infoativconcom',
            name='fatormes',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatr',
            name='indsubstpatr',
            field=models.IntegerField(choices=[(1, '1 - Integralmente substitu\xedda'), (2, '2 - Parcialmente substitu\xedda.')], null=True),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatr',
            name='percredcontrib',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1280infosubstpatropport',
            name='cnpjopportuario',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
