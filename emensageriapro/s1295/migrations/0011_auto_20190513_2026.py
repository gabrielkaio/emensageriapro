# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1295', '0010_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='cpfresp',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='nmresp',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='s1295_evttotconting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1295iderespinf_s1295_evttotconting', to='esocial.s1295evtTotConting'),
        ),
        migrations.AlterField(
            model_name='s1295iderespinf',
            name='telefone',
            field=models.CharField(default=b'A', max_length=13),
        ),
    ]
