# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2260', '0015_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2260localtrabinterm',
            options={'managed': True, 'ordering': ['s2260_evtconvinterm', 'tplograd', 'dsclograd', 'nrlograd', 'cep', 'codmunic', 'uf'], 'permissions': (('can_see_list_s2260localTrabInterm', 'Pode ver listagem do modelo S2260LOCALTRABINTERM'), ('can_see_data_s2260localTrabInterm', 'Pode visualizar o conte\xfado do modelo S2260LOCALTRABINTERM'), ('can_see_menu_s2260localTrabInterm', 'Pode visualizar no menu o modelo S2260LOCALTRABINTERM'), ('can_print_list_s2260localTrabInterm', 'Pode imprimir listagem do modelo S2260LOCALTRABINTERM'), ('can_print_data_s2260localTrabInterm', 'Pode imprimir o conte\xfado do modelo S2260LOCALTRABINTERM'))},
        ),
    ]