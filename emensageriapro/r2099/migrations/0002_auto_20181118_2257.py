# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r2099', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2099iderespinf',
            options={'managed': True, 'ordering': ['r2099_evtfechaevper', 'nmresp', 'cpfresp']},
        ),
        migrations.AlterField(
            model_name='r2099iderespinf',
            name='cpfresp',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='r2099iderespinf',
            name='criado_em',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='r2099iderespinf',
            name='nmresp',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='r2099iderespinf',
            name='r2099_evtfechaevper',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r2099iderespinf_r2099_evtfechaevper', to='efdreinf.r2099evtFechaEvPer'),
        ),
    ]
