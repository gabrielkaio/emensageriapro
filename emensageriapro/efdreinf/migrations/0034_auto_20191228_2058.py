# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-28 20:58
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0033_auto_20191228_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='r1000evtinfocontri',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r1070evttabprocesso',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2010evtservtom',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2020evtservprest',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2030evtassocdesprec',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2040evtassocdesprep',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2050evtcomprod',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2060evtcprb',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2070evtpgtosdivs',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2098evtreabreevper',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r2099evtfechaevper',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r5001evttotal',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r5011evttotalcontrib',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
        migrations.AddField(
            model_name='r9000evtexclusao',
            name='ocorrencias_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name=b'ocorrencias_json'),
        ),
    ]
