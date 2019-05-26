# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('efdreinf', '0016_auto_20190427_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='r9011infoCRTom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crtom', models.IntegerField(default=0)),
                ('vlrcrtom', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('vlrcrtomsusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011infocrtom_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011infocrtom_modificado_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'ordering': ['r9011_rtom', 'crtom'],
                'db_table': 'r9011_infocrtom',
                'permissions': (('can_view_r9011_infocrtom', 'Can view r9011_infocrtom'),),
            },
        ),
        migrations.CreateModel(
            name='r9011infoTotalContrib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrrecarqbase', models.CharField(blank=True, max_length=52, null=True)),
                ('indexistinfo', models.IntegerField(choices=[(1, '1 - H\xe1 informa\xe7\xf5es de bases e/ou de tributos'), (2, '2 - H\xe1 movimento, por\xe9m n\xe3o h\xe1 informa\xe7\xf5es de bases ou de tributos'), (3, '3 - N\xe3o h\xe1 movimento na compet\xeancia')], default=0)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011infototalcontrib_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011infototalcontrib_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9011_evttotalcontrib', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9011infototalcontrib_r9011_evttotalcontrib', to='efdreinf.r9011evtTotalContrib')),
            ],
            options={
                'managed': True,
                'ordering': ['r9011_evttotalcontrib', 'indexistinfo'],
                'db_table': 'r9011_infototalcontrib',
                'permissions': (('can_view_r9011_infototalcontrib', 'Can view r9011_infototalcontrib'),),
            },
        ),
        migrations.CreateModel(
            name='r9011RComl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crcoml', models.IntegerField(default=0)),
                ('vlrcrcoml', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrcrcomlsusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rcoml_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rcoml_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9011_infototalcontrib', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rcoml_r9011_infototalcontrib', to='r9011.r9011infoTotalContrib')),
            ],
            options={
                'managed': True,
                'ordering': ['r9011_infototalcontrib', 'crcoml', 'vlrcrcoml'],
                'db_table': 'r9011_rcoml',
                'permissions': (('can_view_r9011_rcoml', 'Can view r9011_rcoml'),),
            },
        ),
        migrations.CreateModel(
            name='r9011RCPRB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crcprb', models.IntegerField(default=0)),
                ('vlrcrcprb', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrcrcprbsusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rcprb_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rcprb_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9011_infototalcontrib', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rcprb_r9011_infototalcontrib', to='r9011.r9011infoTotalContrib')),
            ],
            options={
                'managed': True,
                'ordering': ['r9011_infototalcontrib', 'crcprb', 'vlrcrcprb'],
                'db_table': 'r9011_rcprb',
                'permissions': (('can_view_r9011_rcprb', 'Can view r9011_rcprb'),),
            },
        ),
        migrations.CreateModel(
            name='r9011regOcorrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpocorr', models.IntegerField(choices=[(1, '1 - Erro'), (2, '2 - Aviso.')], default=0)),
                ('localerroaviso', models.CharField(default=b'A', max_length=200)),
                ('codresp', models.CharField(default=b'A', max_length=6)),
                ('dscresp', models.CharField(default=b'A', max_length=999)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011regocorrs_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011regocorrs_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9011_evttotalcontrib', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9011regocorrs_r9011_evttotalcontrib', to='efdreinf.r9011evtTotalContrib')),
            ],
            options={
                'managed': True,
                'ordering': ['r9011_evttotalcontrib', 'tpocorr', 'localerroaviso', 'codresp', 'dscresp'],
                'db_table': 'r9011_regocorrs',
                'permissions': (('can_view_r9011_regocorrs', 'Can view r9011_regocorrs'),),
            },
        ),
        migrations.CreateModel(
            name='r9011RPrest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tpinsctomador', models.IntegerField(default=0)),
                ('nrinsctomador', models.CharField(default=b'A', max_length=14)),
                ('vlrtotalbaseret', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrtotalretprinc', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrtotalretadic', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('vlrtotalnretprinc', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('vlrtotalnretadic', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rprest_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rprest_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9011_infototalcontrib', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rprest_r9011_infototalcontrib', to='r9011.r9011infoTotalContrib')),
            ],
            options={
                'managed': True,
                'ordering': ['r9011_infototalcontrib', 'tpinsctomador', 'nrinsctomador', 'vlrtotalbaseret', 'vlrtotalretprinc'],
                'db_table': 'r9011_rprest',
                'permissions': (('can_view_r9011_rprest', 'Can view r9011_rprest'),),
            },
        ),
        migrations.CreateModel(
            name='r9011RRecRepAD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crrecrepad', models.IntegerField(default=0)),
                ('vlrcrrecrepad', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('vlrcrrecrepadsusp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=14, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rrecrepad_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rrecrepad_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9011_infototalcontrib', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rrecrepad_r9011_infototalcontrib', to='r9011.r9011infoTotalContrib')),
            ],
            options={
                'managed': True,
                'ordering': ['r9011_infototalcontrib', 'crrecrepad', 'vlrcrrecrepad'],
                'db_table': 'r9011_rrecrepad',
                'permissions': (('can_view_r9011_rrecrepad', 'Can view r9011_rrecrepad'),),
            },
        ),
        migrations.CreateModel(
            name='r9011RTom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpjprestador', models.CharField(default=b'A', max_length=14)),
                ('cno', models.CharField(blank=True, max_length=12, null=True)),
                ('vlrtotalbaseret', models.DecimalField(decimal_places=2, default=0, max_digits=15, max_length=14)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rtom_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rtom_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r9011_infototalcontrib', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9011rtom_r9011_infototalcontrib', to='r9011.r9011infoTotalContrib')),
            ],
            options={
                'managed': True,
                'ordering': ['r9011_infototalcontrib', 'cnpjprestador', 'vlrtotalbaseret'],
                'db_table': 'r9011_rtom',
                'permissions': (('can_view_r9011_rtom', 'Can view r9011_rtom'),),
            },
        ),
        migrations.AddField(
            model_name='r9011infocrtom',
            name='r9011_rtom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r9011infocrtom_r9011_rtom', to='r9011.r9011RTom'),
        ),
    ]
