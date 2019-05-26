# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r4040', '0002_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r4040idenat',
            name='natrendim',
            field=models.IntegerField(choices=[(1, '1 - Rendimentos do trabalho'), (9, '9 - Demais rendimentos.')], default=0),
        ),
        migrations.AlterField(
            model_name='r4040idenat',
            name='r4040_evtbenefnid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r4040idenat_r4040_evtbenefnid', to='efdreinf.r4040evtBenefNId'),
        ),
        migrations.AlterField(
            model_name='r4040infopgto',
            name='descr',
            field=models.CharField(default=b'A', max_length=200),
        ),
        migrations.AlterField(
            model_name='r4040infopgto',
            name='dtfg',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='r4040infopgto',
            name='r4040_idenat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r4040infopgto_r4040_idenat', to='r4040.r4040ideNat'),
        ),
        migrations.AlterField(
            model_name='r4040infopgto',
            name='vlrir',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r4040infopgto',
            name='vlrliq',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r4040infopgto',
            name='vlrreaj',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
