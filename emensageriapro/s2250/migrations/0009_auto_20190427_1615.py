# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2250', '0008_auto_20190204_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2250cancavprevio',
            name='dtcancavprv',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2250cancavprevio',
            name='mtvcancavprevio',
            field=models.IntegerField(choices=[(1, '1 - Reconsidera\xe7\xe3o prevista no artigo 489 da CLT'), (2, '2 - Determina\xe7\xe3o Judicial'), (3, '3 - Cumprimento de norma legal'), (9, '9 - Outros')], default=0),
        ),
        migrations.AlterField(
            model_name='s2250cancavprevio',
            name='s2250_evtavprevio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2250cancavprevio_s2250_evtavprevio', to='esocial.s2250evtAvPrevio'),
        ),
        migrations.AlterField(
            model_name='s2250detavprevio',
            name='dtavprv',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2250detavprevio',
            name='dtprevdeslig',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2250detavprevio',
            name='s2250_evtavprevio',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2250detavprevio_s2250_evtavprevio', to='esocial.s2250evtAvPrevio'),
        ),
        migrations.AlterField(
            model_name='s2250detavprevio',
            name='tpavprevio',
            field=models.IntegerField(choices=[(1, '1 - Aviso pr\xe9vio trabalhado dado pelo empregador ao empregado, que optou pela redu\xe7\xe3o de duas horas di\xe1rias [caput do art. 488 da CLT]'), (2, '2 - Aviso pr\xe9vio trabalhado dado pelo empregador ao empregado, que optou pela redu\xe7\xe3o de dias corridos [par\xe1grafo \xfanico do art. 488 da CLT]'), (4, '4 - Aviso pr\xe9vio dado pelo empregado (pedido de demiss\xe3o), n\xe3o dispensado de seu cumprimento, sob pena de desconto, pelo empregador, dos sal\xe1rios correspondentes ao prazo respectivo (\xa72\xba do art. 487 da CLT)'), (5, '5 - Aviso pr\xe9vio trabalhado dado pelo empregador rural ao empregado, com redu\xe7\xe3o de um dia por semana ( art. 15 da Lei n\xba 5889/73)')], default=0),
        ),
    ]
