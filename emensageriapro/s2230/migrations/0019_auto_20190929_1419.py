# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-29 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2230', '0018_auto_20190620_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2230infoatestado',
            options={'managed': True, 'ordering': ['s2230_iniafastamento'], 'permissions': (('can_see_list_s2230infoAtestado', 'Pode ver listagem do modelo S2230INFOATESTADO'), ('can_see_data_s2230infoAtestado', 'Pode visualizar o conte\xfado do modelo S2230INFOATESTADO'), ('can_see_menu_s2230infoAtestado', 'Pode visualizar no menu o modelo S2230INFOATESTADO'), ('can_print_list_s2230infoAtestado', 'Pode imprimir listagem do modelo S2230INFOATESTADO'), ('can_print_data_s2230infoAtestado', 'Pode imprimir o conte\xfado do modelo S2230INFOATESTADO'))},
        ),
        migrations.AlterField(
            model_name='s2230infoatestado',
            name='qtddiasafast',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
