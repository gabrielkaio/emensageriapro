# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-21 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0019_auto_20190220_2121'),
        ('esocial', '0021_auto_20190220_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='s2231evtcessao',
            name='arquivo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='arquivo_original',
            field=models.IntegerField(blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='ocorrencias',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='retornos_eventos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2231evtcessao_retornos_eventos', to='mensageiro.RetornosEventos'),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (1, 'Importado'), (10, 'XML Assinado'), (11, 'XML Gerado'), (12, 'Retorno'), (14, 'Processado'), (15, 'Aguardando consulta'), (2, 'Duplicado'), (3, 'Erro na valida\xe7\xe3o'), (4, 'Validado'), (5, 'Erro no envio'), (6, 'Aguardando envio')], default=0),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='transmissor_lote_esocial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2231evtcessao_transmissor_lote_esocial', to='mensageiro.TransmissorLoteEsocial'),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='validacao_precedencia',
            field=models.IntegerField(blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')], null=True),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='validacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='s2231evtcessao',
            name='versao',
            field=models.CharField(blank=True, choices=[(b'v02_04_02', 'Vers\xe3o 2.04.02'), (b'v02_05_00', 'Vers\xe3o 2.05.00')], default=b'v02_05_00', max_length=20),
        ),
    ]
