# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('r1000', '0008_auto_20190204_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r1000alteracao',
            name='classtrib',
            field=models.CharField(default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='cpfctt',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='indacordoisenmulta',
            field=models.IntegerField(choices=[(0, '0 - Sem acordo'), (1, '1 - Com acordo')], default=0),
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='inddesoneracao',
            field=models.IntegerField(choices=[(0, '0 - N\xe3o Aplic\xe1vel'), (1, '1 - Empresa enquadrada nos termos da Lei 12.546/2011 e altera\xe7\xf5es')], default=0),
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='indescrituracao',
            field=models.IntegerField(choices=[(0, '0 - Empresa N\xe3o obrigada \xe0 ECD'), (1, '1 - Empresa obrigada \xe0 ECD')], default=0),
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='nmctt',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='r1000alteracao',
            name='r1000_evtinfocontri',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1000alteracao_r1000_evtinfocontri', to='efdreinf.r1000evtInfoContri'),
        ),
        migrations.AlterField(
            model_name='r1000alteracaoinfoefr',
            name='ideefr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='r1000alteracaoinfoefr',
            name='r1000_alteracao',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1000alteracaoinfoefr_r1000_alteracao', to='r1000.r1000alteracao'),
        ),
        migrations.AlterField(
            model_name='r1000alteracaonovavalidade',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='r1000alteracaonovavalidade',
            name='r1000_alteracao',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1000alteracaonovavalidade_r1000_alteracao', to='r1000.r1000alteracao'),
        ),
        migrations.AlterField(
            model_name='r1000alteracaosofthouse',
            name='cnpjsofthouse',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r1000alteracaosofthouse',
            name='nmcont',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='r1000alteracaosofthouse',
            name='nmrazao',
            field=models.CharField(default=b'A', max_length=115),
        ),
        migrations.AlterField(
            model_name='r1000alteracaosofthouse',
            name='r1000_alteracao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1000alteracaosofthouse_r1000_alteracao', to='r1000.r1000alteracao'),
        ),
        migrations.AlterField(
            model_name='r1000exclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='r1000exclusao',
            name='r1000_evtinfocontri',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1000exclusao_r1000_evtinfocontri', to='efdreinf.r1000evtInfoContri'),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='classtrib',
            field=models.CharField(default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='cpfctt',
            field=models.CharField(default=b'A', max_length=11),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='indacordoisenmulta',
            field=models.IntegerField(choices=[(0, '0 - Sem acordo'), (1, '1 - Com acordo')], default=0),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='inddesoneracao',
            field=models.IntegerField(choices=[(0, '0 - N\xe3o Aplic\xe1vel'), (1, '1 - Empresa enquadrada nos termos da Lei 12.546/2011 e altera\xe7\xf5es')], default=0),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='indescrituracao',
            field=models.IntegerField(choices=[(0, '0 - Empresa N\xe3o obrigada \xe0 ECD'), (1, '1 - Empresa obrigada \xe0 ECD')], default=0),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='inivalid',
            field=models.CharField(choices=[(b'2017-01', 'Janeiro/2017'), (b'2017-02', 'Fevereiro/2017'), (b'2017-03', 'Mar\xe7o/2017'), (b'2017-04', 'Abril/2017'), (b'2017-05', 'Maio/2017'), (b'2017-06', 'Junho/2017'), (b'2017-07', 'Julho/2017'), (b'2017-08', 'Agosto/2017'), (b'2017-09', 'Setembro/2017'), (b'2017-10', 'Outubro/2017'), (b'2017-11', 'Novembro/2017'), (b'2017-12', 'Dezembro/2017'), (b'2018-01', 'Janeiro/2018'), (b'2018-02', 'Fevereiro/2018'), (b'2018-03', 'Mar\xe7o/2018'), (b'2018-04', 'Abril/2018'), (b'2018-05', 'Maio/2018'), (b'2018-06', 'Junho/2018'), (b'2018-07', 'Julho/2018'), (b'2018-08', 'Agosto/2018'), (b'2018-09', 'Setembro/2018'), (b'2018-10', 'Outubro/2018'), (b'2018-11', 'Novembro/2018'), (b'2018-12', 'Dezembro/2018'), (b'2019-01', 'Janeiro/2019'), (b'2019-02', 'Fevereiro/2019'), (b'2019-03', 'Mar\xe7o/2019'), (b'2019-04', 'Abril/2019'), (b'2019-05', 'Maio/2019'), (b'2019-06', 'Junho/2019'), (b'2019-07', 'Julho/2019'), (b'2019-08', 'Agosto/2019'), (b'2019-09', 'Setembro/2019'), (b'2019-10', 'Outubro/2019'), (b'2019-11', 'Novembro/2019'), (b'2019-12', 'Dezembro/2019')], default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='nmctt',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='r1000inclusao',
            name='r1000_evtinfocontri',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1000inclusao_r1000_evtinfocontri', to='efdreinf.r1000evtInfoContri'),
        ),
        migrations.AlterField(
            model_name='r1000inclusaoinfoefr',
            name='ideefr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o \xe9 EFR'), (b'S', 'S - \xc9 EFR')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='r1000inclusaoinfoefr',
            name='r1000_inclusao',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1000inclusaoinfoefr_r1000_inclusao', to='r1000.r1000inclusao'),
        ),
        migrations.AlterField(
            model_name='r1000inclusaosofthouse',
            name='cnpjsofthouse',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='r1000inclusaosofthouse',
            name='nmcont',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='r1000inclusaosofthouse',
            name='nmrazao',
            field=models.CharField(default=b'A', max_length=115),
        ),
        migrations.AlterField(
            model_name='r1000inclusaosofthouse',
            name='r1000_inclusao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r1000inclusaosofthouse_r1000_inclusao', to='r1000.r1000inclusao'),
        ),
    ]
