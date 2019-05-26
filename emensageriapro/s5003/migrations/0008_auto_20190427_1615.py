# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esocial', '0024_auto_20190427_1615'),
        ('s5003', '0007_auto_20190204_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='s5003infoBaseFGTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infobasefgts_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infobasefgts_modificado_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'ordering': ['s5003_infotrabfgts'],
                'db_table': 's5003_infobasefgts',
                'permissions': (('can_view_s5003_infobasefgts', 'Can view s5003_infobasefgts'),),
            },
        ),
        migrations.CreateModel(
            name='s5003infoDpsFGTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infodpsfgts_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infodpsfgts_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('s5003_evtbasesfgts', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infodpsfgts_s5003_evtbasesfgts', to='esocial.s5003evtBasesFGTS')),
            ],
            options={
                'managed': True,
                'ordering': ['s5003_evtbasesfgts'],
                'db_table': 's5003_infodpsfgts',
                'permissions': (('can_view_s5003_infodpsfgts', 'Can view s5003_infodpsfgts'),),
            },
        ),
        migrations.RemoveField(
            model_name='s5003infofgts',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infofgts',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5003infofgts',
            name='s5003_evtbasesfgts',
        ),
        migrations.AlterModelOptions(
            name='s5003baseperapur',
            options={'managed': True, 'ordering': ['s5003_infobasefgts', 'tpvalor', 'remfgts'], 'permissions': (('can_view_s5003_baseperapur', 'Can view s5003_baseperapur'),)},
        ),
        migrations.AlterModelOptions(
            name='s5003ideestablot',
            options={'managed': True, 'ordering': ['s5003_evtbasesfgts', 'tpinsc', 'nrinsc', 'codlotacao'], 'permissions': (('can_view_s5003_ideestablot', 'Can view s5003_ideestablot'),)},
        ),
        migrations.AlterModelOptions(
            name='s5003infobaseperante',
            options={'managed': True, 'ordering': ['s5003_infobasefgts', 'perref'], 'permissions': (('can_view_s5003_infobaseperante', 'Can view s5003_infobaseperante'),)},
        ),
        migrations.AlterModelOptions(
            name='s5003infotrabdps',
            options={'managed': True, 'ordering': ['s5003_infodpsfgts', 'codcateg'], 'permissions': (('can_view_s5003_infotrabdps', 'Can view s5003_infotrabdps'),)},
        ),
        migrations.RemoveField(
            model_name='s5003baseperapur',
            name='s5003_infotrabfgts',
        ),
        migrations.RemoveField(
            model_name='s5003ideestablot',
            name='s5003_infofgts',
        ),
        migrations.RemoveField(
            model_name='s5003infobaseperante',
            name='s5003_infotrabfgts',
        ),
        migrations.RemoveField(
            model_name='s5003infotrabdps',
            name='s5003_infofgts',
        ),
        migrations.AddField(
            model_name='s5003ideestablot',
            name='s5003_evtbasesfgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003ideestablot_s5003_evtbasesfgts', to='esocial.s5003evtBasesFGTS'),
        ),
        migrations.AlterField(
            model_name='s5003baseperante',
            name='remfgtse',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s5003baseperante',
            name='s5003_infobaseperante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003baseperante_s5003_infobaseperante', to='s5003.s5003infoBasePerAntE'),
        ),
        migrations.AlterField(
            model_name='s5003baseperante',
            name='tpvalore',
            field=models.IntegerField(choices=[(13, '13 - Base de C\xe1lculo do FGTS Diss\xeddio'), (14, '14 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (17, '17 - Base de C\xe1lculo do FGTS Diss\xeddio - Aprendiz'), (18, '18 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (24, '24 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio'), (25, '25 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (26, '26 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (30, '30 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (31, '31 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (32, '32 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz'), (91, '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003baseperapur',
            name='remfgts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s5003baseperapur',
            name='tpvalor',
            field=models.IntegerField(choices=[(11, '11 - Base de C\xe1lculo do FGTS'), (12, '12 - Base de C\xe1lculo do FGTS 13\xb0 Sal\xe1rio'), (13, '13 - Base de C\xe1lculo do FGTS Diss\xeddio'), (14, '14 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (15, '15 - Base de C\xe1lculo do FGTS - Aprendiz'), (16, '16 - Base de C\xe1lculo do FGTS 13\xb0 Sal\xe1rio - Aprendiz'), (17, '17 - Base de C\xe1lculo do FGTS Diss\xeddio - Aprendiz'), (18, '18 - Base de C\xe1lculo do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (21, '21 - Base de C\xe1lculo do FGTS Rescis\xf3rio'), (22, '22 - Base de C\xe1lculo do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio'), (23, '23 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aviso Pr\xe9vio'), (24, '24 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio'), (25, '25 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (26, '26 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (27, '27 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aprendiz'), (28, '28 - Base de C\xe1lculo do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio Aprendiz'), (29, '29 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Aviso Pr\xe9vio Aprendiz'), (30, '30 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (31, '31 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (32, '32 - Base de C\xe1lculo do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz'), (91, '91 - Incid\xeancia suspensa em decorr\xeancia de decis\xe3o judicial')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003dpsperante',
            name='dpsfgtse',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s5003dpsperante',
            name='s5003_infodpsperante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003dpsperante_s5003_infodpsperante', to='s5003.s5003infoDpsPerAntE'),
        ),
        migrations.AlterField(
            model_name='s5003dpsperante',
            name='tpdpse',
            field=models.IntegerField(choices=[(53, '53 - Dep\xf3sito do FGTS Diss\xeddio'), (54, '54 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (57, '57 - Dep\xf3sito do FGTS Diss\xeddio - Aprendiz'), (58, '58 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (64, '64 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio'), (65, '65 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (66, '66 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (70, '70 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (71, '71 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (72, '72 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003dpsperapur',
            name='dpsfgts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14),
        ),
        migrations.AlterField(
            model_name='s5003dpsperapur',
            name='s5003_infotrabdps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003dpsperapur_s5003_infotrabdps', to='s5003.s5003infoTrabDps'),
        ),
        migrations.AlterField(
            model_name='s5003dpsperapur',
            name='tpdps',
            field=models.IntegerField(choices=[(51, '51 - Dep\xf3sito do FGTS'), (52, '52 - Dep\xf3sito do FGTS 13\xb0 Sal\xe1rio'), (53, '53 - Dep\xf3sito do FGTS Diss\xeddio'), (54, '54 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio'), (55, '55 - Dep\xf3sito do FGTS - Aprendiz'), (56, '56 - Dep\xf3sito do FGTS 13\xb0 Sal\xe1rio - Aprendiz'), (57, '57 - Dep\xf3sito do FGTS Diss\xeddio - Aprendiz'), (58, '58 - Dep\xf3sito do FGTS Diss\xeddio 13\xba Sal\xe1rio - Aprendiz'), (61, '61 - Dep\xf3sito do FGTS Rescis\xf3rio'), (62, '62 - Dep\xf3sito do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio'), (63, '63 - Dep\xf3sito do FGTS Rescis\xf3rio - Aviso Pr\xe9vio'), (64, '64 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio'), (65, '65 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xba Sal\xe1rio'), (66, '66 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio'), (67, '67 - Dep\xf3sito do FGTS Rescis\xf3rio - Aprendiz'), (68, '68 - Dep\xf3sito do FGTS Rescis\xf3rio - 13\xb0 Sal\xe1rio Aprendiz'), (69, '69 - Dep\xf3sito do FGTS Rescis\xf3rio - Aviso Pr\xe9vio Aprendiz'), (70, '70 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aprendiz'), (71, '71 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio 13\xb0 Sal\xe1rio Aprendiz'), (72, '72 - Dep\xf3sito do FGTS Rescis\xf3rio - Diss\xeddio Aviso Pr\xe9vio Aprendiz')], default=0),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='codlotacao',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='nrinsc',
            field=models.CharField(default=b'A', max_length=15),
        ),
        migrations.AlterField(
            model_name='s5003ideestablot',
            name='tpinsc',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='s5003infobaseperante',
            name='perref',
            field=models.CharField(default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='s5003infodpsperante',
            name='perref',
            field=models.CharField(default=b'A', max_length=7),
        ),
        migrations.AlterField(
            model_name='s5003infodpsperante',
            name='s5003_infotrabdps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infodpsperante_s5003_infotrabdps', to='s5003.s5003infoTrabDps'),
        ),
        migrations.AlterField(
            model_name='s5003infotrabdps',
            name='codcateg',
            field=models.TextField(default=b'0', max_length=3),
        ),
        migrations.AlterField(
            model_name='s5003infotrabfgts',
            name='codcateg',
            field=models.TextField(default=b'0', max_length=3),
        ),
        migrations.AlterField(
            model_name='s5003infotrabfgts',
            name='s5003_ideestablot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infotrabfgts_s5003_ideestablot', to='s5003.s5003ideEstabLot'),
        ),
        migrations.DeleteModel(
            name='s5003infoFGTS',
        ),
        migrations.AddField(
            model_name='s5003infobasefgts',
            name='s5003_infotrabfgts',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infobasefgts_s5003_infotrabfgts', to='s5003.s5003infoTrabFGTS'),
        ),
        migrations.AddField(
            model_name='s5003baseperapur',
            name='s5003_infobasefgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003baseperapur_s5003_infobasefgts', to='s5003.s5003infoBaseFGTS'),
        ),
        migrations.AddField(
            model_name='s5003infobaseperante',
            name='s5003_infobasefgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infobaseperante_s5003_infobasefgts', to='s5003.s5003infoBaseFGTS'),
        ),
        migrations.AddField(
            model_name='s5003infotrabdps',
            name='s5003_infodpsfgts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s5003infotrabdps_s5003_infodpsfgts', to='s5003.s5003infoDpsFGTS'),
        ),
    ]
