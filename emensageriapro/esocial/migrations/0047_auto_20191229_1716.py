# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-29 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esocial', '0046_auto_20191228_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s1000evtinfoempregador',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1000evtinfoempregador',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1005evttabestab',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1005evttabestab',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1010evttabrubrica',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1010evttabrubrica',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1020evttablotacao',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1020evttablotacao',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1030evttabcargo',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1030evttabcargo',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1035evttabcarreira',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1035evttabcarreira',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1040evttabfuncao',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1040evttabfuncao',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1050evttabhortur',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1050evttabhortur',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1060evttabambiente',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1060evttabambiente',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1070evttabprocesso',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1070evttabprocesso',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1080evttaboperport',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1080evttaboperport',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1200evtremun',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1200evtremun',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1200evtremun',
            name='retornos_s5001',
        ),
        migrations.RemoveField(
            model_name='s1200evtremun',
            name='retornos_s5003',
        ),
        migrations.RemoveField(
            model_name='s1202evtrmnrpps',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1202evtrmnrpps',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1207evtbenprrp',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1207evtbenprrp',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1210evtpgtos',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1210evtpgtos',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1210evtpgtos',
            name='retornos_s5002',
        ),
        migrations.RemoveField(
            model_name='s1250evtaqprod',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1250evtaqprod',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1260evtcomprod',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1260evtcomprod',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1270evtcontratavnp',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1270evtcontratavnp',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1280evtinfocomplper',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1280evtinfocomplper',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1295evttotconting',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1295evttotconting',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1295evttotconting',
            name='retornos_s5011',
        ),
        migrations.RemoveField(
            model_name='s1295evttotconting',
            name='retornos_s5012',
        ),
        migrations.RemoveField(
            model_name='s1295evttotconting',
            name='retornos_s5013',
        ),
        migrations.RemoveField(
            model_name='s1298evtreabreevper',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1298evtreabreevper',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1299evtfechaevper',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1299evtfechaevper',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s1299evtfechaevper',
            name='retornos_s5011',
        ),
        migrations.RemoveField(
            model_name='s1299evtfechaevper',
            name='retornos_s5012',
        ),
        migrations.RemoveField(
            model_name='s1299evtfechaevper',
            name='retornos_s5013',
        ),
        migrations.RemoveField(
            model_name='s1300evtcontrsindpatr',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s1300evtcontrsindpatr',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2190evtadmprelim',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2190evtadmprelim',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2200evtadmissao',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2200evtadmissao',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2205evtaltcadastral',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2205evtaltcadastral',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2206evtaltcontratual',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2206evtaltcontratual',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2210evtcat',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2210evtcat',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2220evtmonit',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2220evtmonit',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2221evttoxic',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2221evttoxic',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2230evtafasttemp',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2230evtafasttemp',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2231evtcessao',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2231evtcessao',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2240evtexprisco',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2240evtexprisco',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2241evtinsapo',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2241evtinsapo',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2245evttreicap',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2245evttreicap',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2250evtavprevio',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2250evtavprevio',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2260evtconvinterm',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2260evtconvinterm',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2298evtreintegr',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2298evtreintegr',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2299evtdeslig',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2299evtdeslig',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2299evtdeslig',
            name='retornos_s5001',
        ),
        migrations.RemoveField(
            model_name='s2299evtdeslig',
            name='retornos_s5003',
        ),
        migrations.RemoveField(
            model_name='s2300evttsvinicio',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2300evttsvinicio',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2306evttsvaltcontr',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2306evttsvaltcontr',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2399evttsvtermino',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2399evttsvtermino',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2399evttsvtermino',
            name='retornos_s5001',
        ),
        migrations.RemoveField(
            model_name='s2399evttsvtermino',
            name='retornos_s5003',
        ),
        migrations.RemoveField(
            model_name='s2400evtcdbenefin',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2400evtcdbenefin',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2405evtcdbenefalt',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2405evtcdbenefalt',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2410evtcdbenin',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2410evtcdbenin',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2416evtcdbenalt',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2416evtcdbenalt',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s2420evtcdbenterm',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s2420evtcdbenterm',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s3000evtexclusao',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s3000evtexclusao',
            name='retornos_eventos',
        ),
        migrations.RemoveField(
            model_name='s5001evtbasestrab',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s5002evtirrfbenef',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s5003evtbasesfgts',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s5011evtcs',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s5012evtirrf',
            name='ocorrencias',
        ),
        migrations.RemoveField(
            model_name='s5013evtfgts',
            name='ocorrencias',
        ),
    ]