# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2050', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2050infoproc',
            options={'managed': True, 'ordering': ['r2050_tipocom', 'tpproc', 'nrproc'], 'permissions': (('can_view_r2050infoProc', 'Can view R2050INFOPROC'), ('can_view_menu_r2050infoProc', 'Can view menu R2050INFOPROC'))},
        ),
        migrations.AlterModelOptions(
            name='r2050tipocom',
            options={'managed': True, 'ordering': ['r2050_evtcomprod', 'indcom', 'vlrrecbruta'], 'permissions': (('can_view_r2050tipoCom', 'Can view R2050TIPOCOM'), ('can_view_menu_r2050tipoCom', 'Can view menu R2050TIPOCOM'))},
        ),
    ]
