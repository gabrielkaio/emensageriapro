# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-20 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r5001', '0002_auto_20181118_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r5001infocrtom',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001infocrtom',
            name='crtom',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5001infocrtom',
            name='r5001_rtom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5001infocrtom_r5001_rtom', to='r5001.r5001RTom'),
        ),
        migrations.AlterField(
            model_name='r5001infototal',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001infototal',
            name='nrinsc',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001infototal',
            name='r5001_evttotal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='r5001infototal_r5001_evttotal', to='efdreinf.r5001evtTotal'),
        ),
        migrations.AlterField(
            model_name='r5001infototal',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (4, '4 - CNO')]),
        ),
        migrations.AlterField(
            model_name='r5001rcoml',
            name='crcoml',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5001rcoml',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001rcoml',
            name='r5001_infototal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5001rcoml_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rcoml',
            name='vlrcrcoml',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rcprb',
            name='crcprb',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5001rcprb',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001rcprb',
            name='r5001_infototal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5001rcprb_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rcprb',
            name='vlrcrcprb',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='codresp',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='dscresp',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='localerroaviso',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='r5001_evttotal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5001regocorrs_r5001_evttotal', to='efdreinf.r5001evtTotal'),
        ),
        migrations.AlterField(
            model_name='r5001regocorrs',
            name='tpocorr',
            field=models.IntegerField(choices=[(1, '1 - Aviso'), (2, '2 - Erro')]),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='nrinsctomador',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='r5001_infototal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='r5001rprest_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='tpinsctomador',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (4, '4 - CNO')]),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='vlrtotalbaseret',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rprest',
            name='vlrtotalretprinc',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='crrecespetdesp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='r5001_infototal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='r5001rrecespetdesp_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='vlrcrrecespetdesp',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecespetdesp',
            name='vlrreceitatotal',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='cnpjassocdesp',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='crrecrepad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='r5001_infototal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5001rrecrepad_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='vlrcrrecrepad',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rrecrepad',
            name='vlrtotalrep',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rtom',
            name='cnpjprestador',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='r5001rtom',
            name='criado_em',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='r5001rtom',
            name='r5001_infototal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='r5001rtom_r5001_infototal', to='r5001.r5001infoTotal'),
        ),
        migrations.AlterField(
            model_name='r5001rtom',
            name='vlrtotalbaseret',
            field=models.DecimalField(decimal_places=2, max_digits=15, max_length=14),
        ),
    ]
