# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2410', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2410homologtc',
            options={'managed': True, 'ordering': ['s2410_evtcdbenin', 'dthomol', 'nratolegal'], 'permissions': (('can_view_s2410homologTC', 'Can view S2410HOMOLOGTC'), ('can_view_menu_s2410homologTC', 'Can view menu S2410HOMOLOGTC'))},
        ),
        migrations.AlterModelOptions(
            name='s2410infopenmorte',
            options={'managed': True, 'ordering': ['s2410_evtcdbenin', 'tppenmorte'], 'permissions': (('can_view_s2410infoPenMorte', 'Can view S2410INFOPENMORTE'), ('can_view_menu_s2410infoPenMorte', 'Can view menu S2410INFOPENMORTE'))},
        ),
        migrations.AlterModelOptions(
            name='s2410instpenmorte',
            options={'managed': True, 'ordering': ['s2410_infopenmorte', 'cpfinst', 'dtinst', 'intaposentado'], 'permissions': (('can_view_s2410instPenMorte', 'Can view S2410INSTPENMORTE'), ('can_view_menu_s2410instPenMorte', 'Can view menu S2410INSTPENMORTE'))},
        ),
    ]