# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s5002', '0012_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5002basesirrf',
            name='s5002_infoirrf',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5002basesirrf_s5002_infoirrf', to='s5002.s5002infoIrrf'),
        ),
        migrations.AlterField(
            model_name='s5002basesirrf',
            name='tpvalor',
            field=models.IntegerField(choices=[(11, '11 - Remunera\xe7\xe3o Mensal'), (12, '12 - 13o Sal\xe1rio'), (13, '13 - F\xe9rias'), (14, '14 - PLR'), (15, '15 - Rendimentos Recebidos Acumuladamente - RRA'), (31, '31 - (Reten\xe7\xf5es do IRRF efetuadas sobre) Remunera\xe7\xe3o Mensal'), (32, '32 - (Reten\xe7\xf5es do IRRF efetuadas sobre) 13o Sal\xe1rio'), (33, '33 - (Reten\xe7\xf5es do IRRF efetuadas sobre) F\xe9rias'), (34, '34 - (Reten\xe7\xf5es do IRRF efetuadas sobre) PLR'), (35, '35 - (Reten\xe7\xf5es do IRRF efetuadas sobre) RRA'), (41, '41 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Previd\xeancia Social Oficial - PSO - Remuner. Mensal'), (42, '42 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) PSO - 13\xb0 sal\xe1rio'), (43, '43 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) PSO - F\xe9rias'), (44, '44 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) PSO - RRA'), (46, '46 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Previd\xeancia Privada - sal\xe1rio mensal'), (47, '47 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Previd\xeancia Privada - 13\xb0 sal\xe1rio'), (51, '51 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - Remunera\xe7\xe3o Mensal'), (52, '52 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - 13\xb0 sal\xe1rio'), (53, '53 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - F\xe9rias'), (54, '54 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - PLR'), (55, '55 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - RRA'), (61, '61 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Fundo de Aposentadoria Programada Individual - FAPI - Remunera\xe7\xe3o Mensal'), (62, '62 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Fundo de Aposentadoria Programada Individual - FAPI - 13\xb0 sal\xe1rio'), (63, '63 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Funda\xe7\xe3o de Previd\xeancia Complementar do Servidor P\xfablico - Funpresp - Remunera\xe7\xe3o Mensal'), (64, '64 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Funda\xe7\xe3o de Previd\xeancia Complementar do Servidor P\xfablico - Funpresp - 13\xb0 sal\xe1rio'), (70, '70 - (Isen\xe7\xf5es do IRRF) Parcela Isenta 65 anos - Remunera\xe7\xe3o Mensal'), (71, '71 - (Isen\xe7\xf5es do IRRF) Parcela Isenta 65 anos - 13\xb0 sal\xe1rio'), (72, '72 - (Isen\xe7\xf5es do IRRF) Di\xe1rias'), (73, '73 - (Isen\xe7\xf5es do IRRF) Ajuda de Custo'), (74, '74 - (Isen\xe7\xf5es do IRRF) Indeniza\xe7\xe3o e rescis\xe3o de contrato, inclusive a t\xedtulo de PDV e acidentes de trabalho'), (75, '75 - (Isen\xe7\xf5es do IRRF) Abono pecuni\xe1rio'), (76, '76 - (Isen\xe7\xf5es do IRRF) Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - Remunera\xe7\xe3o Mensal'), (77, '77 - (Isen\xe7\xf5es do IRRF) Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - 13\xb0 sal\xe1rio'), (78, '78 - (Isen\xe7\xf5es do IRRF) Valores pagos a titular ou s\xf3cio de microempresa ou empresa de pequeno porte, exceto pr\xf3-labore e alugueis'), (79, '79 - (Isen\xe7\xf5es do IRRF) Outras isen\xe7\xf5es (identificar o nome da rubrica em S-1010)'), (81, '81 - (Demandas Judiciais) Dep\xf3sito Judicial'), (82, '82 - (Demandas Judiciais) Compensa\xe7\xe3o Judicial do ano calend\xe1rio'), (83, '83 - (Demandas Judiciais) Compensa\xe7\xe3o Judicial de anos anteriores'), (91, '91 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) Remunera\xe7\xe3o Mensal'), (92, '92 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) 13o Sal\xe1rio'), (93, '93 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre)F\xe9rias'), (94, '94 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) PLR'), (95, '95 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) RRA.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5002basesirrf',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5002idepgtoext',
            name='codpais',
            field=models.CharField(default=b'A', max_length=3),
        ),
        migrations.AlterField(
            model_name='s5002idepgtoext',
            name='dsclograd',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s5002idepgtoext',
            name='indnif',
            field=models.IntegerField(choices=[(1, '1 - Benefici\xe1rio com NIF'), (2, '2 - Benefici\xe1rio dispensado do NIF'), (3, '3 - Pa\xeds n\xe3o exige NIF.')], default=0),
        ),
        migrations.AlterField(
            model_name='s5002idepgtoext',
            name='nmcid',
            field=models.CharField(default=b'A', max_length=50),
        ),
        migrations.AlterField(
            model_name='s5002idepgtoext',
            name='s5002_infoirrf',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5002idepgtoext_s5002_infoirrf', to='s5002.s5002infoIrrf'),
        ),
        migrations.AlterField(
            model_name='s5002infodep',
            name='s5002_evtirrfbenef',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5002infodep_s5002_evtirrfbenef', to='esocial.s5002evtIrrfBenef'),
        ),
        migrations.AlterField(
            model_name='s5002infodep',
            name='vrdeddep',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s5002infoirrf',
            name='codcateg',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5002infoirrf',
            name='indresbr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s5002infoirrf',
            name='s5002_evtirrfbenef',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5002infoirrf_s5002_evtirrfbenef', to='esocial.s5002evtIrrfBenef'),
        ),
        migrations.AlterField(
            model_name='s5002irrf',
            name='s5002_infoirrf',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5002irrf_s5002_infoirrf', to='s5002.s5002infoIrrf'),
        ),
        migrations.AlterField(
            model_name='s5002irrf',
            name='tpcr',
            field=models.CharField(choices=[(b'0473-01', '0473-01 - Renda e Proventos de Qualquer Natureza'), (b'0561-07', '0561-07 - IRRF - Rendimento do Trabalho Assalariado no Pa\xeds/Ausente no Exterior a Servi\xe7o do Pa\xeds'), (b'0561-08', '0561-08 - IRRF - Empregado Dom\xe9stico'), (b'0561-09', '0561-09 - IRRF - Empregado Dom\xe9stico - 13\xba Sal Rescis\xe3o'), (b'0561-10', '0561-10 - IRRF - Empregado dom\xe9stico - 13\xba sal\xe1rio'), (b'0561-11', '0561-11 - IRRF - Empregado/Trabalhador Rural - Segurado Especial'), (b'0561-12', '0561-12 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio'), (b'0561-13', '0561-13 - IRRF - Empregado/Trabalhador Rural - Segurado Especial 13\xb0 sal\xe1rio rescis\xf3rio'), (b'0588-06', '0588-06 - IRRF - Rendimento do trabalho sem v\xednculo empregat\xedcio'), (b'0610- 01', '0610- 01 - IRRF - Rendimentos relativos a presta\xe7\xe3o de servi\xe7os de transporte rodovi\xe1rio internacional de carga, pagos a transportador aut\xf4nomo PF residente no Paraguai'), (b'3533', '3533 - Proventos de Aposentadoria, Reserva, Reforma ou Pens\xe3o Pagos por Previd\xeancia P\xfablica'), (b'3562-01', '3562-01 - IRRF - Participa\xe7\xe3o dos trabalhadores em Lucros ou Resultados (PLR). Origem S-1210, para defini\xe7\xe3o do m\xeas de ocorr\xeancia dos fatos geradores e os respectivos demonstrativos de pagamento constantes dos eventos S-1200, S- 1202,S-1207, S-2299 e S-2399.')], default=b'A', max_length=6),
        ),
        migrations.AlterField(
            model_name='s5002irrf',
            name='vrirrfdesc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]