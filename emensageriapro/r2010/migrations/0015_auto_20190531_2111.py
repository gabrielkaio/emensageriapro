# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2010', '0014_auto_20190530_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2010infoprocretad',
            options={'managed': True, 'ordering': ['r2010_evtservtom', 'tpprocretadic', 'nrprocretadic', 'valoradic'], 'permissions': (('can_view_r2010infoProcRetAd', 'Can view R2010INFOPROCRETAD'), ('can_view_menu_r2010infoProcRetAd', 'Can view menu R2010INFOPROCRETAD'))},
        ),
        migrations.AlterModelOptions(
            name='r2010infoprocretpr',
            options={'managed': True, 'ordering': ['r2010_evtservtom', 'tpprocretprinc', 'nrprocretprinc', 'valorprinc'], 'permissions': (('can_view_r2010infoProcRetPr', 'Can view R2010INFOPROCRETPR'), ('can_view_menu_r2010infoProcRetPr', 'Can view menu R2010INFOPROCRETPR'))},
        ),
        migrations.AlterModelOptions(
            name='r2010infotpserv',
            options={'managed': True, 'ordering': ['r2010_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao'], 'permissions': (('can_view_r2010infoTpServ', 'Can view R2010INFOTPSERV'), ('can_view_menu_r2010infoTpServ', 'Can view menu R2010INFOTPSERV'))},
        ),
        migrations.AlterModelOptions(
            name='r2010nfs',
            options={'managed': True, 'ordering': ['r2010_evtservtom', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto'], 'permissions': (('can_view_r2010nfs', 'Can view R2010NFS'), ('can_view_menu_r2010nfs', 'Can view menu R2010NFS'))},
        ),
    ]