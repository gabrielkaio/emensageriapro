# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2245', '0010_auto_20190427_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='codcbo',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='formprof',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='nacprof',
            field=models.IntegerField(choices=[(1, '1 - Brasileiro'), (2, '2 - Estrangeiro')]),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='nmprof',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='s2245_evttreicap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2245ideprofresp_s2245_evttreicap', to='esocial.s2245evtTreiCap'),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='tpprof',
            field=models.IntegerField(choices=[(1, '1 - Profissional empregado do declarante'), (2, '2 - Profissional sem v\xednculo de emprego/estatut\xe1rio com o declarante')]),
        ),
    ]
