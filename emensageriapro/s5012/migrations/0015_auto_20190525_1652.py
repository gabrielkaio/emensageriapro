# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s5012', '0014_auto_20190516_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5012infocrcontrib',
            name='tpcr',
            field=models.CharField(choices=[(b'0473-01', '0473-01 - IRRF - Residentes Fiscais no Exterior 0561-07 - IRRF Mensal, 13\xb0 sal\xe1rio e F\xe9rias sobre Trabalho Assalariado no pa\xeds ou ausente no exterior a servi\xe7o do pa\xeds, exceto se contratado por Empregador Dom\xe9stico ou por Segurado Especial sujeito a recolhimento unificado'), (b'0561-08', '0561-08 - IRRF Mensal, 13\xb0 sal\xe1rio e F\xe9rias sobre Trabalho Assalariado no pa\xeds ou ausente no exterior a servi\xe7o do pa\xeds, Empregado Dom\xe9stico ou Trabalhador contratado por Segurado Especial sujeito a recolhimento unificado'), (b'0561-09', '0561-09 - IRRF 13\xb0 sal\xe1rio na rescis\xe3o de contrato de trabalho relativo a empregador sujeito a recolhimento unificado'), (b'0561-10', '0561-10 - IRRF - Empregado dom\xe9stico - 13\xba sal\xe1rio'), (b'0561-11', '0561-11 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'), (b'0561-12', '0561-12 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio. 0561-13 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio rescis\xf3rio'), (b'0588-06', '0588-06 - IRRF sobre Rendimento do trabalho sem v\xednculo empregat\xedcio'), (b'0610- 01', '0610- 01 - IRRF sobre Rendimentos relativos a presta\xe7\xe3o de servi\xe7os de transporte rodovi\xe1rio internacional de carga, pagos a transportador aut\xf4nomo PF residente no Paraguai'), (b'3533', '3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pens\xe3o Pagos por Previd\xeancia P\xfablica'), (b'3562-01', '3562-01 - IRRF sobre Participa\xe7\xe3o dos trabalhadores em Lucros ou Resultados (PLR).')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='s5012infocrcontrib',
            name='vrcr',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]
