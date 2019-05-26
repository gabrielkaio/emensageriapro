# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2245', '0011_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='codcbo',
            field=models.CharField(default=b'A', max_length=6),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='formprof',
            field=models.CharField(default=b'A', max_length=255),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='nacprof',
            field=models.IntegerField(choices=[(1, '1 - Brasileiro'), (2, '2 - Estrangeiro.')], default=0),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='nmprof',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='s2245_evttreicap',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2245ideprofresp_s2245_evttreicap', to='esocial.s2245evtTreiCap'),
        ),
        migrations.AlterField(
            model_name='s2245ideprofresp',
            name='tpprof',
            field=models.IntegerField(choices=[(1, '1 - Profissional empregado do declarante'), (2, '2 - Profissional sem v\xednculo de emprego/estatut\xe1rio com o declarante.')], default=0),
        ),
    ]
