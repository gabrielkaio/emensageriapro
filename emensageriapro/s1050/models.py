#coding:utf-8
from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
from emensageriapro.s1050.choices import *
get_model = apps.get_model


"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""


STATUS_EVENTO_CADASTRADO = 0
STATUS_EVENTO_IMPORTADO = 1
STATUS_EVENTO_DUPLICADO = 2
STATUS_EVENTO_GERADO = 3
STATUS_EVENTO_GERADO_ERRO = 4
STATUS_EVENTO_ASSINADO = 5
STATUS_EVENTO_ASSINADO_ERRO = 6
STATUS_EVENTO_VALIDADO = 7
STATUS_EVENTO_VALIDADO_ERRO = 8
STATUS_EVENTO_AGUARD_PRECEDENCIA = 9
STATUS_EVENTO_AGUARD_ENVIO = 10
STATUS_EVENTO_ENVIADO = 11
STATUS_EVENTO_ENVIADO_ERRO = 12
STATUS_EVENTO_PROCESSADO = 13





class s1050alteracao(SoftDeletionModel):

    s1050_evttabhortur = models.ForeignKey('esocial.s1050evtTabHorTur', 
        related_name='%(class)s_s1050_evttabhortur', )
    
    def evento(self): 
        return self.s1050_evttabhortur.evento()
    codhorcontrat = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    hrentr = models.CharField(max_length=4, null=True, )
    hrsaida = models.CharField(max_length=4, null=True, )
    durjornada = models.IntegerField(null=True, )
    perhorflexivel = models.CharField(choices=CHOICES_S1050_PERHORFLEXIVEL_ALTERACAO, max_length=1, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1050_evttabhortur),
            unicode(self.codhorcontrat),
            unicode(self.inivalid),
            unicode(self.hrentr),
            unicode(self.hrsaida),
            unicode(self.durjornada),
            unicode(self.perhorflexivel),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r's1050_alteracao'       
        managed = True # s1050_alteracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1050_alteracao", "Can view s1050_alteracao"), )
            
        ordering = [
            's1050_evttabhortur',
            'codhorcontrat',
            'inivalid',
            'hrentr',
            'hrsaida',
            'durjornada',
            'perhorflexivel',]



class s1050alteracaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1050alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1050alteracaohorarioIntervalo(SoftDeletionModel):

    s1050_alteracao = models.ForeignKey('s1050.s1050alteracao', 
        related_name='%(class)s_s1050_alteracao', )
    
    def evento(self): 
        return self.s1050_alteracao.evento()
    tpinterv = models.IntegerField(choices=CHOICES_S1050_TPINTERV_ALTERACAO, null=True, )
    durinterv = models.IntegerField(null=True, )
    iniinterv = models.CharField(max_length=4, blank=True, null=True, )
    terminterv = models.CharField(max_length=4, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1050_alteracao),
            unicode(self.tpinterv),
            unicode(self.durinterv),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que detalha os intervalos para a jornada. O preenchimento do registro é obrigatório se existir ao menos um intervalo.'
        db_table = r's1050_alteracao_horariointervalo'       
        managed = True # s1050_alteracao_horariointervalo #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1050_alteracao_horariointervalo", "Can view s1050_alteracao_horariointervalo"), )
            
        ordering = [
            's1050_alteracao',
            'tpinterv',
            'durinterv',]



class s1050alteracaohorarioIntervaloSerializer(ModelSerializer):

    class Meta:
    
        model = s1050alteracaohorarioIntervalo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1050alteracaonovaValidade(SoftDeletionModel):

    s1050_alteracao = models.ForeignKey('s1050.s1050alteracao', 
        related_name='%(class)s_s1050_alteracao', )
    
    def evento(self): 
        return self.s1050_alteracao.evento()
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1050_alteracao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade.'
        db_table = r's1050_alteracao_novavalidade'       
        managed = True # s1050_alteracao_novavalidade #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1050_alteracao_novavalidade", "Can view s1050_alteracao_novavalidade"), )
            
        ordering = [
            's1050_alteracao',
            'inivalid',]



class s1050alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = s1050alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1050exclusao(SoftDeletionModel):

    s1050_evttabhortur = models.ForeignKey('esocial.s1050evtTabHorTur', 
        related_name='%(class)s_s1050_evttabhortur', )
    
    def evento(self): 
        return self.s1050_evttabhortur.evento()
    codhorcontrat = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1050_evttabhortur),
            unicode(self.codhorcontrat),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r's1050_exclusao'       
        managed = True # s1050_exclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1050_exclusao", "Can view s1050_exclusao"), )
            
        ordering = [
            's1050_evttabhortur',
            'codhorcontrat',
            'inivalid',]



class s1050exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1050exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1050inclusao(SoftDeletionModel):

    s1050_evttabhortur = models.ForeignKey('esocial.s1050evtTabHorTur', 
        related_name='%(class)s_s1050_evttabhortur', )
    
    def evento(self): 
        return self.s1050_evttabhortur.evento()
    codhorcontrat = models.CharField(max_length=30, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    hrentr = models.CharField(max_length=4, null=True, )
    hrsaida = models.CharField(max_length=4, null=True, )
    durjornada = models.IntegerField(null=True, )
    perhorflexivel = models.CharField(choices=CHOICES_S1050_PERHORFLEXIVEL_INCLUSAO, max_length=1, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1050_evttabhortur),
            unicode(self.codhorcontrat),
            unicode(self.inivalid),
            unicode(self.hrentr),
            unicode(self.hrsaida),
            unicode(self.durjornada),
            unicode(self.perhorflexivel),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r's1050_inclusao'       
        managed = True # s1050_inclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1050_inclusao", "Can view s1050_inclusao"), )
            
        ordering = [
            's1050_evttabhortur',
            'codhorcontrat',
            'inivalid',
            'hrentr',
            'hrsaida',
            'durjornada',
            'perhorflexivel',]



class s1050inclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = s1050inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class s1050inclusaohorarioIntervalo(SoftDeletionModel):

    s1050_inclusao = models.ForeignKey('s1050.s1050inclusao', 
        related_name='%(class)s_s1050_inclusao', )
    
    def evento(self): 
        return self.s1050_inclusao.evento()
    tpinterv = models.IntegerField(choices=CHOICES_S1050_TPINTERV_INCLUSAO, null=True, )
    durinterv = models.IntegerField(null=True, )
    iniinterv = models.CharField(max_length=4, blank=True, null=True, )
    terminterv = models.CharField(max_length=4, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.s1050_inclusao),
            unicode(self.tpinterv),
            unicode(self.durinterv),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro que detalha os intervalos para a jornada. O preenchimento do registro é obrigatório se existir ao menos um intervalo.'
        db_table = r's1050_inclusao_horariointervalo'       
        managed = True # s1050_inclusao_horariointervalo #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_s1050_inclusao_horariointervalo", "Can view s1050_inclusao_horariointervalo"), )
            
        ordering = [
            's1050_inclusao',
            'tpinterv',
            'durinterv',]



class s1050inclusaohorarioIntervaloSerializer(ModelSerializer):

    class Meta:
    
        model = s1050inclusaohorarioIntervalo
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()