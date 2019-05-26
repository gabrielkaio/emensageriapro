# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2416', '0009_auto_20190427_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2416homologtc',
            name='nratolegal',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='s2416homologtc',
            name='s2416_evtcdbenalt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2416homologtc_s2416_evtcdbenalt', to='esocial.s2416evtCdBenAlt'),
        ),
        migrations.AlterField(
            model_name='s2416infopenmorte',
            name='s2416_evtcdbenalt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2416infopenmorte_s2416_evtcdbenalt', to='esocial.s2416evtCdBenAlt'),
        ),
        migrations.AlterField(
            model_name='s2416infopenmorte',
            name='tppenmorte',
            field=models.IntegerField(choices=[(1, '1 - Vital\xedcia'), (2, '2 - Tempor\xe1ria')]),
        ),
        migrations.AlterField(
            model_name='s2416suspensao',
            name='mtvsuspensao',
            field=models.CharField(choices=[(b'01', '01 - Suspens\xe3o por n\xe3o recadastramento'), (b'99', '99 - Outros motivos de suspens\xe3o')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s2416suspensao',
            name='s2416_evtcdbenalt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s2416suspensao_s2416_evtcdbenalt', to='esocial.s2416evtCdBenAlt'),
        ),
    ]
