# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1210', '0012_auto_20190428_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1210deps',
            name='s1210_evtpgtos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210deps_s1210_evtpgtos', to='esocial.s1210evtPgtos'),
        ),
        migrations.AlterField(
            model_name='s1210deps',
            name='vrdeddep',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoant',
            name='codcateg',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoant',
            name='s1210_infopgto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtoant_s1210_infopgto', to='s1210.s1210infoPgto'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoantinfopgtoant',
            name='s1210_detpgtoant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtoantinfopgtoant_s1210_detpgtoant', to='s1210.s1210detPgtoAnt'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoantinfopgtoant',
            name='tpbcirrf',
            field=models.CharField(choices=[(b'11', '11 - Remunera\xe7\xe3o Mensal'), (b'12', '12 - 13o Sal\xe1rio'), (b'13', '13 - F\xe9rias'), (b'14', '14 - PLR'), (b'15', '15 - Rendimentos Recebidos Acumuladamente - RRA'), (b'31', '31 - (Reten\xe7\xf5es do IRRF efetuadas sobre) Remunera\xe7\xe3o mensal'), (b'32', '32 - (Reten\xe7\xf5es do IRRF efetuadas sobre) 13o Sal\xe1rio'), (b'33', '33 - (Reten\xe7\xf5es do IRRF efetuadas sobre) F\xe9rias'), (b'34', '34 - (Reten\xe7\xf5es do IRRF efetuadas sobre) PLR'), (b'35', '35 - (Reten\xe7\xf5es do IRRF efetuadas sobre) RRA'), (b'41', '41 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Previd\xeancia Social Oficial - PSO - Remuner. Mensal'), (b'42', '42 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) PSO - 13\xb0 sal\xe1rio'), (b'43', '43 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) PSO - F\xe9rias'), (b'44', '44 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) PSO - RRA'), (b'46', '46 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Previd\xeancia Privada - sal\xe1rio mensal'), (b'47', '47 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Previd\xeancia Privada - 13\xb0 sal\xe1rio'), (b'51', '51 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - Remunera\xe7\xe3o Mensal'), (b'52', '52 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - 13\xb0 sal\xe1rio'), (b'53', '53 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - F\xe9rias'), (b'54', '54 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - PLR'), (b'55', '55 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Pens\xe3o Aliment\xedcia - RRA'), (b'61', '61 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Fundo de Aposentadoria Programada Individual - FAPI - Remunera\xe7\xe3o Mensal'), (b'62', '62 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Fundo de Aposentadoria Programada Individual - FAPI - 13\xb0 sal\xe1rio'), (b'63', '63 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Funda\xe7\xe3o de Previd\xeancia Complementar do Servidor P\xfablico - Funpresp - Remunera\xe7\xe3o Mensal'), (b'64', '64 - (Dedu\xe7\xf5es da base de c\xe1lculo do IRRF) Funda\xe7\xe3o de Previd\xeancia Complementar do Servidor P\xfablico - Funpresp - 13\xb0 sal\xe1rio'), (b'70', '70 - (Isen\xe7\xf5es do IRRF) Parcela Isenta 65 anos - Remunera\xe7\xe3o Mensal'), (b'71', '71 - (Isen\xe7\xf5es do IRRF) Parcela Isenta 65 anos - 13\xb0 sal\xe1rio'), (b'72', '72 - (Isen\xe7\xf5es do IRRF) Di\xe1rias'), (b'73', '73 - (Isen\xe7\xf5es do IRRF) Ajuda de Custo'), (b'74', '74 - (Isen\xe7\xf5es do IRRF) Indeniza\xe7\xe3o e rescis\xe3o de contrato, inclusive a t\xedtulo de PDV e acidentes de trabalho'), (b'75', '75 - (Isen\xe7\xf5es do IRRF) Abono pecuni\xe1rio'), (b'76', '76 - (Isen\xe7\xf5es do IRRF) Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - Remunera\xe7\xe3o Mensal'), (b'77', '77 - (Isen\xe7\xf5es do IRRF) Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o - 13\xb0 sal\xe1rio'), (b'78', '78 - (Isen\xe7\xf5es do IRRF) Valores pagos a titular ou s\xf3cio de microempresa ou empresa de pequeno porte, exceto pr\xf3-labore e alugueis'), (b'79', '79 - (Isen\xe7\xf5es do IRRF) Outras isen\xe7\xf5es (o nome da rubrica deve ser claro para identifica\xe7\xe3o da natureza dos valores)'), (b'81', '81 - (Demandas Judiciais) Dep\xf3sito Judicial'), (b'82', '82 - (Demandas Judiciais) Compensa\xe7\xe3o Judicial do ano calend\xe1rio'), (b'83', '83 - (Demandas Judiciais) Compensa\xe7\xe3o Judicial de anos anteriores'), (b'91', '91 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) Remunera\xe7\xe3o Mensal'), (b'92', '92 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) 13o Sal\xe1rio'), (b'93', '93 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) F\xe9rias'), (b'94', '94 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) PLR'), (b'95', '95 - (Incid\xeancia Suspensa decorrente de decis\xe3o judicial, relativas a base de c\xe1lculo do IRRF sobre) RRA.')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoantinfopgtoant',
            name='vrbcirrf',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenpr',
            name='idedmdev',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenpr',
            name='indpgtott',
            field=models.CharField(choices=[(b'N', 'N - O valor que est\xe1 sendo pago \xe9 inferior ao previsto no eventoS - 1207 em {dmDev}. neste caso, significa que est\xe1 sendo informando um pagamento de parte do que \xe9 devido ou ent\xe3o, est\xe1 sendo informado um pagamento parcelado sendo o presente pagamento apenas uma das parcelas.'), (b'S', 'S - O valor que est\xe1 sendo pago \xe9 exatamente o previsto no eventoS - 1207 em {dmDev}')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenpr',
            name='perref',
            field=models.CharField(default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenpr',
            name='s1210_infopgto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtobenpr_s1210_infopgto', to='s1210.s1210infoPgto'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenpr',
            name='vrliq',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='codrubr',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='fatorrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='idetabrubr',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='qtdrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='s1210_detpgtobenpr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtobenprinfopgtoparc_s1210_detpgtobenpr', to='s1210.s1210detPgtoBenPr'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='vrunit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='codrubr',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='fatorrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='idetabrubr',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='qtdrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='s1210_detpgtobenpr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtobenprretpgtotot_s1210_detpgtobenpr', to='s1210.s1210detPgtoBenPr'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='vrunit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofer',
            name='codcateg',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofer',
            name='dtinigoz',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofer',
            name='qtdias',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofer',
            name='s1210_infopgto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtofer_s1210_infopgto', to='s1210.s1210infoPgto'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofer',
            name='vrliq',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='codrubr',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='fatorrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='idetabrubr',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='qtdrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='s1210_detpgtofer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtoferdetrubrfer_s1210_detpgtofer', to='s1210.s1210detPgtoFer'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='vrunit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferpenalim',
            name='cpfbenef',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferpenalim',
            name='nmbenefic',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferpenalim',
            name='s1210_detpgtofer_detrubrfer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtoferpenalim_s1210_detpgtofer_detrubrfer', to='s1210.s1210detPgtoFerdetRubrFer'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferpenalim',
            name='vlrpensao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofl',
            name='idedmdev',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofl',
            name='indpgtott',
            field=models.CharField(choices=[(b'N', 'N - O valor que est\xe1 sendo pago \xe9 inferior ao previsto nos eventosS - 1200,S - 1202,S - 2299 ouS - 2399 em {dmDev}, neste caso, significa que est\xe1 sendo informando um pagamento de parte do que \xe9 devido ou ent\xe3o, est\xe1 sendo informado um pagamento parcelado sendo o presente pagamento apenas uma das parcelas.'), (b'S', 'S - O valor que est\xe1 sendo pago \xe9 exatamente o previsto nos eventosS - 1200,S - 1202,S - 2299 ouS - 2399 em {dmDev}')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofl',
            name='s1210_infopgto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtofl_s1210_infopgto', to='s1210.s1210infoPgto'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofl',
            name='vrliq',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='codrubr',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='fatorrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='idetabrubr',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='qtdrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='s1210_detpgtofl',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtoflinfopgtoparc_s1210_detpgtofl', to='s1210.s1210detPgtoFl'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='vrunit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflpenalim',
            name='cpfbenef',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflpenalim',
            name='nmbenefic',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflpenalim',
            name='s1210_detpgtofl_retpgtotot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtoflpenalim_s1210_detpgtofl_retpgtotot', to='s1210.s1210detPgtoFlretPgtoTot'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflpenalim',
            name='vlrpensao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='codrubr',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='fatorrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='idetabrubr',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='qtdrubr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='s1210_detpgtofl',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210detpgtoflretpgtotot_s1210_detpgtofl', to='s1210.s1210detPgtoFl'),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='vrunit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='s1210idepgtoext',
            name='codpais',
            field=models.CharField(default=b'A', max_length=3),
        ),
        migrations.AlterField(
            model_name='s1210idepgtoext',
            name='dsclograd',
            field=models.CharField(default=b'A', max_length=100),
        ),
        migrations.AlterField(
            model_name='s1210idepgtoext',
            name='indnif',
            field=models.IntegerField(choices=[(1, '1 - Benefici\xe1rio com NIF'), (2, '2 - Benefici\xe1rio dispensado do NIF'), (3, '3 - Pa\xeds n\xe3o exige NIF.')], default=0),
        ),
        migrations.AlterField(
            model_name='s1210idepgtoext',
            name='nmcid',
            field=models.CharField(default=b'A', max_length=50),
        ),
        migrations.AlterField(
            model_name='s1210idepgtoext',
            name='s1210_infopgto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210idepgtoext_s1210_infopgto', to='s1210.s1210infoPgto'),
        ),
        migrations.AlterField(
            model_name='s1210infopgto',
            name='dtpgto',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s1210infopgto',
            name='indresbr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s1210infopgto',
            name='s1210_evtpgtos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1210infopgto_s1210_evtpgtos', to='esocial.s1210evtPgtos'),
        ),
        migrations.AlterField(
            model_name='s1210infopgto',
            name='tppgto',
            field=models.IntegerField(choices=[(1, '1 - Pagamento de remunera\xe7\xe3o, conforme apurado em {dmDev} do S-1200'), (2, '2 - Pagamento de verbas rescis\xf3rias conforme apurado em {dmDev} do S- 2299'), (3, '3 - Pagamento de verbas rescis\xf3rias conforme apurado em {dmDev} do S- 2399'), (5, '5 - Pagamento de remunera\xe7\xe3o conforme apurado em {dmDev} do S-1202'), (6, '6 - Pagamento de Benef\xedcios Previdenci\xe1rios, conforme apurado em {dmDev} do S-1207'), (7, '7 - Recibo de f\xe9rias'), (9, '9 - Pagamento relativo a compet\xeancias anteriores ao in\xedcio de obrigatoriedade dos eventos peri\xf3dicos para o contribuinte.')], default=0),
        ),
    ]
