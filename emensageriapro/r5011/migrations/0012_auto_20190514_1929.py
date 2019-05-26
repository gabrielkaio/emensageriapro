# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r5011', '0011_auto_20190513_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r5011infocrtom',
            name='crtom',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5011infocrtom',
            name='r5011_rtom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5011infocrtom_r5011_rtom', to='r5011.r5011RTom'),
        ),
        migrations.AlterField(
            model_name='r5011infototalcontrib',
            name='indexistinfo',
            field=models.IntegerField(choices=[(1, '1 - H\xe1 informa\xe7\xf5es de bases e/ou de tributos'), (2, '2 - H\xe1 movimento, por\xe9m n\xe3o h\xe1 informa\xe7\xf5es de bases ou de tributos'), (3, '3 - N\xe3o h\xe1 movimento na compet\xeancia.')]),
        ),
        migrations.AlterField(
            model_name='r5011infototalcontrib',
            name='r5011_evttotalcontrib',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5011infototalcontrib_r5011_evttotalcontrib', to='efdreinf.r5011evtTotalContrib'),
        ),
        migrations.AlterField(
            model_name='r5011rcoml',
            name='crcoml',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5011rcoml',
            name='r5011_infototalcontrib',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5011rcoml_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib'),
        ),
        migrations.AlterField(
            model_name='r5011rcoml',
            name='vlrcrcoml',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r5011rcprb',
            name='crcprb',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5011rcprb',
            name='r5011_infototalcontrib',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5011rcprb_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib'),
        ),
        migrations.AlterField(
            model_name='r5011rcprb',
            name='vlrcrcprb',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r5011regocorrs',
            name='codresp',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='r5011regocorrs',
            name='dscresp',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='r5011regocorrs',
            name='localerroaviso',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='r5011regocorrs',
            name='r5011_evttotalcontrib',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5011regocorrs_r5011_evttotalcontrib', to='efdreinf.r5011evtTotalContrib'),
        ),
        migrations.AlterField(
            model_name='r5011regocorrs',
            name='tpocorr',
            field=models.IntegerField(choices=[(1, '1 - Erro'), (2, '2 - Aviso')]),
        ),
        migrations.AlterField(
            model_name='r5011rprest',
            name='nrinsctomador',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='r5011rprest',
            name='r5011_infototalcontrib',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5011rprest_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib'),
        ),
        migrations.AlterField(
            model_name='r5011rprest',
            name='tpinsctomador',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5011rprest',
            name='vlrtotalbaseret',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r5011rprest',
            name='vlrtotalretprinc',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r5011rrecrepad',
            name='cnpjassocdesp',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='r5011rrecrepad',
            name='crrecrepad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='r5011rrecrepad',
            name='r5011_infototalcontrib',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5011rrecrepad_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib'),
        ),
        migrations.AlterField(
            model_name='r5011rrecrepad',
            name='vlrcrrecrepad',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r5011rrecrepad',
            name='vlrtotalrep',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='r5011rtom',
            name='cnpjprestador',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='r5011rtom',
            name='r5011_infototalcontrib',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r5011rtom_r5011_infototalcontrib', to='r5011.r5011infoTotalContrib'),
        ),
        migrations.AlterField(
            model_name='r5011rtom',
            name='vlrtotalbaseret',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
