# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s1202', '0010_auto_20190204_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='s1202infoPerAnt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperant_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperant_modificado_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'ordering': ['s1202_dmdev'],
                'db_table': 's1202_infoperant',
                'permissions': (('can_view_s1202_infoperant', 'Can view s1202_infoperant'),),
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapur_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapur_modificado_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'ordering': ['s1202_dmdev'],
                'db_table': 's1202_infoperapur',
                'permissions': (('can_view_s1202_infoperapur', 'Can view s1202_infoperapur'),),
            },
        ),
        migrations.CreateModel(
            name='s1202infoPerApurinfoSaudeColet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapurinfosaudecolet_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapurinfosaudecolet_modificado_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'ordering': ['s1202_infoperapur_remunperapur'],
                'db_table': 's1202_infoperapur_infosaudecolet',
                'permissions': (('can_view_s1202_infoperapur_infosaudecolet', 'Can view s1202_infoperapur_infosaudecolet'),),
            },
        ),
        migrations.AlterModelOptions(
            name='s1202infoperantideadc',
            options={'managed': True, 'ordering': ['s1202_infoperant', 'dtlei', 'nrlei', 'tpacconv', 'dsc'], 'permissions': (('can_view_s1202_infoperant_ideadc', 'Can view s1202_infoperant_ideadc'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurdetoper',
            options={'managed': True, 'ordering': ['s1202_infoperapur_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit'], 'permissions': (('can_view_s1202_infoperapur_detoper', 'Can view s1202_infoperapur_detoper'),)},
        ),
        migrations.AlterModelOptions(
            name='s1202infoperapurideestab',
            options={'managed': True, 'ordering': ['s1202_infoperapur', 'tpinsc', 'nrinsc'], 'permissions': (('can_view_s1202_infoperapur_ideestab', 'Can view s1202_infoperapur_ideestab'),)},
        ),
        migrations.RemoveField(
            model_name='s1202infoperantideadc',
            name='s1202_dmdev',
        ),
        migrations.RemoveField(
            model_name='s1202infoperapurdetoper',
            name='s1202_infoperapur_remunperapur',
        ),
        migrations.RemoveField(
            model_name='s1202infoperapurideestab',
            name='s1202_dmdev',
        ),
        migrations.AlterField(
            model_name='s1202dmdev',
            name='codcateg',
            field=models.TextField(default=b'0', max_length=3),
        ),
        migrations.AlterField(
            model_name='s1202dmdev',
            name='idedmdev',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1202dmdev',
            name='s1202_evtrmnrpps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202dmdev_s1202_evtrmnrpps', to='esocial.s1202evtRmnRPPS'),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideadc',
            name='dsc',
            field=models.CharField(default=b'A', max_length=255),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideadc',
            name='dtlei',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideadc',
            name='nrlei',
            field=models.CharField(default=b'A', max_length=12),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideadc',
            name='tpacconv',
            field=models.CharField(choices=[(b'B', 'B - Legisla\xe7\xe3o federal, estadual, municipal ou distrital'), (b'F', 'F - Outras verbas de natureza salarial ou n\xe3o salarial devidas ap\xf3s o desligamento'), (b'G', 'G - Decis\xe3o administrativa'), (b'H', 'H - Decis\xe3o judicial')], default=b'A', max_length=1),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideestab',
            name='nrinsc',
            field=models.CharField(default=b'A', max_length=15),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideestab',
            name='s1202_infoperant_ideperiodo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperantideestab_s1202_infoperant_ideperiodo', to='s1202.s1202infoPerAntidePeriodo'),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideestab',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')], default=0),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideperiodo',
            name='perref',
            field=models.CharField(default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='s1202infoperantideperiodo',
            name='s1202_infoperant_ideadc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperantideperiodo_s1202_infoperant_ideadc', to='s1202.s1202infoPerAntideADC'),
        ),
        migrations.AlterField(
            model_name='s1202infoperantitensremun',
            name='codrubr',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1202infoperantitensremun',
            name='idetabrubr',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s1202infoperantitensremun',
            name='s1202_infoperant_remunperant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperantitensremun_s1202_infoperant_remunperant', to='s1202.s1202infoPerAntremunPerAnt'),
        ),
        migrations.AlterField(
            model_name='s1202infoperantitensremun',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1202infoperantremunperant',
            name='codcateg',
            field=models.TextField(default=b'0', max_length=3),
        ),
        migrations.AlterField(
            model_name='s1202infoperantremunperant',
            name='s1202_infoperant_ideestab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperantremunperant_s1202_infoperant_ideestab', to='s1202.s1202infoPerAntideEstab'),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurdetoper',
            name='cnpjoper',
            field=models.CharField(default=b'A', max_length=14),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurdetoper',
            name='regans',
            field=models.CharField(default=b'A', max_length=6),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurdetoper',
            name='vrpgtit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurdetplano',
            name='dtnascto',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurdetplano',
            name='nmdep',
            field=models.CharField(default=b'A', max_length=70),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurdetplano',
            name='s1202_infoperapur_detoper',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapurdetplano_s1202_infoperapur_detoper', to='s1202.s1202infoPerApurdetOper'),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurdetplano',
            name='tpdep',
            field=models.CharField(choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')], default=b'A', max_length=2),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurdetplano',
            name='vlrpgdep',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurideestab',
            name='nrinsc',
            field=models.CharField(default=b'A', max_length=15),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurideestab',
            name='tpinsc',
            field=models.IntegerField(choices=[(1, '1 - CNPJ'), (2, '2 - CPF'), (3, '3 - CAEPF (Cadastro de Atividade Econ\xf4mica de Pessoa F\xedsica)'), (4, '4 - CNO (Cadastro Nacional de Obra)')], default=0),
        ),
        migrations.AlterField(
            model_name='s1202infoperapuritensremun',
            name='codrubr',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s1202infoperapuritensremun',
            name='idetabrubr',
            field=models.CharField(default=b'A', max_length=8),
        ),
        migrations.AlterField(
            model_name='s1202infoperapuritensremun',
            name='s1202_infoperapur_remunperapur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapuritensremun_s1202_infoperapur_remunperapur', to='s1202.s1202infoPerApurremunPerApur'),
        ),
        migrations.AlterField(
            model_name='s1202infoperapuritensremun',
            name='vrrubr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurremunperapur',
            name='codcateg',
            field=models.TextField(default=b'0', max_length=3),
        ),
        migrations.AlterField(
            model_name='s1202infoperapurremunperapur',
            name='s1202_infoperapur_ideestab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapurremunperapur_s1202_infoperapur_ideestab', to='s1202.s1202infoPerApurideEstab'),
        ),
        migrations.AlterField(
            model_name='s1202procjudtrab',
            name='nrprocjud',
            field=models.CharField(default=b'A', max_length=20),
        ),
        migrations.AlterField(
            model_name='s1202procjudtrab',
            name='s1202_evtrmnrpps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202procjudtrab_s1202_evtrmnrpps', to='esocial.s1202evtRmnRPPS'),
        ),
        migrations.AlterField(
            model_name='s1202procjudtrab',
            name='tptrib',
            field=models.IntegerField(choices=[(2, '2 - IRRF'), (2, '2 - Contribui\xe7\xf5es sociais do trabalhador'), (3, '3 - FGTS'), (4, '4 - Contribui\xe7\xe3o sindical')], default=0),
        ),
        migrations.AddField(
            model_name='s1202infoperapurinfosaudecolet',
            name='s1202_infoperapur_remunperapur',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapurinfosaudecolet_s1202_infoperapur_remunperapur', to='s1202.s1202infoPerApurremunPerApur'),
        ),
        migrations.AddField(
            model_name='s1202infoperapur',
            name='s1202_dmdev',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapur_s1202_dmdev', to='s1202.s1202dmDev'),
        ),
        migrations.AddField(
            model_name='s1202infoperant',
            name='s1202_dmdev',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperant_s1202_dmdev', to='s1202.s1202dmDev'),
        ),
        migrations.AddField(
            model_name='s1202infoperantideadc',
            name='s1202_infoperant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperantideadc_s1202_infoperant', to='s1202.s1202infoPerAnt'),
        ),
        migrations.AddField(
            model_name='s1202infoperapurdetoper',
            name='s1202_infoperapur_infosaudecolet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapurdetoper_s1202_infoperapur_infosaudecolet', to='s1202.s1202infoPerApurinfoSaudeColet'),
        ),
        migrations.AddField(
            model_name='s1202infoperapurideestab',
            name='s1202_infoperapur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s1202infoperapurideestab_s1202_infoperapur', to='s1202.s1202infoPerApur'),
        ),
    ]
