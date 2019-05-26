# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r2070', '0013_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2070detcompet',
            name='indperreferencia',
            field=models.IntegerField(choices=[(1, '1 - Folha de Pagamento Mensal'), (2, '2 - Folha do D\xe9cimo Terceiro Sal\xe1rio.')], null=True),
        ),
        migrations.AlterField(
            model_name='r2070detcompet',
            name='perrefpagto',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='r2070detcompet',
            name='vlrrendtributavel',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070detdeducao',
            name='indtpdeducao',
            field=models.IntegerField(choices=[(1, '1 - Previd\xeancia Oficial'), (2, '2 - Previd\xeancia Privada'), (3, '3 - Fapi'), (4, '4 - Funpresp'), (5, '5 - Pens\xe3o Aliment\xedcia'), (6, '6 - Dependentes.')], null=True),
        ),
        migrations.AlterField(
            model_name='r2070detdeducao',
            name='vlrdeducao',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070ideestab',
            name='nrinsc',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r2070ideestab',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)'), (5, '5 - CGC')], null=True),
        ),
        migrations.AlterField(
            model_name='r2070infomolestia',
            name='dtlaudo',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjud',
            name='indorigemrecursos',
            field=models.IntegerField(choices=[(1, '1 - Recursos do pr\xf3prio declarante'), (2, '2 - Recursos de terceiros - Declarante \xe9 a Institui\xe7\xe3o Financeira respons\xe1vel apenas pelo repasse dos valores.')], null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjud',
            name='nrprocjud',
            field=models.CharField(max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjuddespprocjud',
            name='vlrdespadvogados',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjuddespprocjud',
            name='vlrdespcustas',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjudideadvogado',
            name='nrinscadvogado',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjudideadvogado',
            name='tpinscadvogado',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjudideadvogado',
            name='vlradvogado',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070infoprocjudorigemrecursos',
            name='cnpjorigemrecursos',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforesidext',
            name='dsclograd',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforesidext',
            name='indnif',
            field=models.IntegerField(choices=[(1, '1 - Benefici\xe1rio com NIF'), (2, '2 - Benefici\xe1rio dispensado do NIF'), (3, '3 - Pa\xeds n\xe3o exige NIF.')], null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforesidext',
            name='paisresid',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforradespprocjud',
            name='vlrdespadvogados',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforradespprocjud',
            name='vlrdespcustas',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforraideadvogado',
            name='nrinscadvogado',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforraideadvogado',
            name='tpinscadvogado',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070inforraideadvogado',
            name='vlradvogado',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopf',
            name='dtpgto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopf',
            name='inddecterceiro',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopf',
            name='indsuspexig',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopf',
            name='vlrirrf',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopf',
            name='vlrrendtributavel',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopj',
            name='dtpagto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopj',
            name='vlrrendtributavel',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopj',
            name='vlrret',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjdespprocjud',
            name='vlrdespadvogados',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjdespprocjud',
            name='vlrdespcustas',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjideadvogado',
            name='nrinscadvogado',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjideadvogado',
            name='tpinscadvogado',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjideadvogado',
            name='vlradvogado',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjinfoprocjud',
            name='indorigemrecursos',
            field=models.IntegerField(choices=[(1, '1 - Recursos do pr\xf3prio declarante'), (2, '2 - Recursos de terceiros - Declarante \xe9 a Institui\xe7\xe3o Financeira respons\xe1vel apenas pelo repasse dos valores.')], null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjinfoprocjud',
            name='nrprocjud',
            field=models.CharField(max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtopjorigemrecursos',
            name='cnpjorigemrecursos',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtoresidext',
            name='dtpagto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtoresidext',
            name='formatributacao',
            field=models.CharField(choices=[(b'10', '10 - Reten\xe7\xe3o do IRRF - al\xedquota padr\xe3o.'), (b'11', '11 - Reten\xe7\xe3o do IRRF - al\xedquota da tabela progressiva.'), (b'12', '12 - Reten\xe7\xe3o do IRRF - al\xedquota diferenciada (pa\xedses com tributa\xe7\xe3o favorecida).'), (b'13', '13 - Reten\xe7\xe3o do IRRF - al\xedquota limitada conforme cl\xe1usula em conv\xeanio.'), (b'30', '30 - Reten\xe7\xe3o do IRRF - outras hip\xf3teses.'), (b'40', '40 - N\xe3o reten\xe7\xe3o do IRRF - isen\xe7\xe3o estabelecida em conv\xeanio.'), (b'41', '41 - N\xe3o reten\xe7\xe3o do IRRF - isen\xe7\xe3o prevista em lei interna'), (b'42', '42 - N\xe3o reten\xe7\xe3o do IRRF - al\xedquota Zero prevista em lei interna'), (b'43', '43 - N\xe3o reten\xe7\xe3o do IRRF - pagamento antecipado do imposto'), (b'44', '44 - N\xe3o reten\xe7\xe3o do IRRF - medida Judicial'), (b'50', '50 - N\xe3o reten\xe7\xe3o do IRRF - outras hip\xf3teses')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtoresidext',
            name='tprendimento',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtoresidext',
            name='vlrpgto',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070pgtoresidext',
            name='vlrret',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='r2070rendisento',
            name='tpisencao',
            field=models.IntegerField(choices=[(1, '1 - Parcela Isenta 65 anos'), (10, '10 - Bolsa de estudo recebida por m\xe9dico-residente'), (11, '11 - Complementa\xe7\xe3o de aposentadoria, correspondente \xe0s contribui\xe7\xf5es efetuadas no per\xedodo de 01/01/1989 a 31/12/1995.'), (2, '2 - Di\xe1ria e Ajuda de Custo'), (3, '3 - Indeniza\xe7\xe3o e rescis\xe3o de contrato, inclusive a t\xedtulo de PDV'), (4, '4 - Abono pecuni\xe1rio'), (5, '5 - Outros (especificar)'), (6, '6 - Lucros e dividendos pagos a partir de 1996'), (7, '7 - Valores pagos a titular ou s\xf3cio de microempresa ou empresa de pequeno porte, exceto pr\xf3-labore e alugueis'), (8, '8 - Pens\xe3o, aposentadoria ou reforma por mol\xe9stia grave ou acidente em servi\xe7o'), (9, '9 - Benef\xedcios indiretos e/ou reembolso de despesas recebidas por volunt\xe1rio da copa do mundo ou da copa das confedera\xe7\xf5es')], null=True),
        ),
        migrations.AlterField(
            model_name='r2070rendisento',
            name='vlrisento',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]