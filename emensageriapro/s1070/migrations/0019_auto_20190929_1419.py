# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-29 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1070', '0018_auto_20190623_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1070exclusao',
            name='tpproc',
            field=models.IntegerField(choices=[(1, '1 - Administrativo'), (2, '2 - Judicial'), (3, '3 - N\xfamero de Benef\xedcio (NB) do INSS'), (4, '4 - Processo FAP.')], null=True),
        ),
    ]
