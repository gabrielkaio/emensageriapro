# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2410', '0008_auto_20190204_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2410homologtc',
            name='dthomol',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2410homologtc',
            name='nratolegal',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s2410homologtc',
            name='s2410_evtcdbenin',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2410homologtc_s2410_evtcdbenin', to='esocial.s2410evtCdBenIn'),
        ),
        migrations.AlterField(
            model_name='s2410infopenmorte',
            name='s2410_evtcdbenin',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2410infopenmorte_s2410_evtcdbenin', to='esocial.s2410evtCdBenIn'),
        ),
        migrations.AlterField(
            model_name='s2410infopenmorte',
            name='tppenmorte',
            field=models.IntegerField(choices=[(1, '1 - Vital\xedcia'), (2, '2 - Tempor\xe1ria')], default=0),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='cpfinst',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='dtinst',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='intaposentado',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s2410instpenmorte',
            name='s2410_infopenmorte',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2410instpenmorte_s2410_infopenmorte', to='s2410.s2410infoPenMorte'),
        ),
    ]
