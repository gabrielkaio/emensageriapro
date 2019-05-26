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
from emensageriapro.r1070.choices import *
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





class r1070alteracao(SoftDeletionModel):

    r1070_evttabprocesso = models.ForeignKey('efdreinf.r1070evtTabProcesso', 
        related_name='%(class)s_r1070_evttabprocesso', )
    
    def evento(self): 
        return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_TPPROC_ALTERACAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    indautoria = models.IntegerField(choices=CHOICES_R1070_INDAUTORIA_ALTERACAO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1070_evttabprocesso),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.inivalid),
            unicode(self.indautoria),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Alteração das informações'
        db_table = r'r1070_alteracao'       
        managed = True # r1070_alteracao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_alteracao", "Can view r1070_alteracao"), )
            
        ordering = [
            'r1070_evttabprocesso',
            'tpproc',
            'nrproc',
            'inivalid',
            'indautoria',]



class r1070alteracaoSerializer(ModelSerializer):

    class Meta:
    
        model = r1070alteracao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1070alteracaodadosProcJud(SoftDeletionModel):

    r1070_alteracao = models.ForeignKey('r1070.r1070alteracao', 
        related_name='%(class)s_r1070_alteracao', )
    
    def evento(self): 
        return self.r1070_alteracao.evento()
    ufvara = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    codmunic = models.TextField(null=True, )
    idvara = models.CharField(max_length=4, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1070_alteracao),
            unicode(self.ufvara),
            unicode(self.codmunic),
            unicode(self.idvara),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações Complementares do Processo Judicial'
        db_table = r'r1070_alteracao_dadosprocjud'       
        managed = True # r1070_alteracao_dadosprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_alteracao_dadosprocjud", "Can view r1070_alteracao_dadosprocjud"), )
            
        ordering = [
            'r1070_alteracao',
            'ufvara',
            'codmunic',
            'idvara',]



class r1070alteracaodadosProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = r1070alteracaodadosProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1070alteracaoinfoSusp(SoftDeletionModel):

    r1070_alteracao = models.ForeignKey('r1070.r1070alteracao', 
        related_name='%(class)s_r1070_alteracao', )
    
    def evento(self): 
        return self.r1070_alteracao.evento()
    codsusp = models.IntegerField(blank=True, null=True, )
    indsusp = models.CharField(choices=CHOICES_R1070_INDSUSP_ALTERACAO, max_length=2, null=True, )
    dtdecisao = models.DateField(null=True, )
    inddeposito = models.CharField(choices=CHOICES_R1070_INDDEPOSITO_ALTERACAO, max_length=1, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1070_alteracao),
            unicode(self.indsusp),
            unicode(self.dtdecisao),
            unicode(self.inddeposito),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de Suspensão de Exibilidade de tributos'
        db_table = r'r1070_alteracao_infosusp'       
        managed = True # r1070_alteracao_infosusp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_alteracao_infosusp", "Can view r1070_alteracao_infosusp"), )
            
        ordering = [
            'r1070_alteracao',
            'indsusp',
            'dtdecisao',
            'inddeposito',]



class r1070alteracaoinfoSuspSerializer(ModelSerializer):

    class Meta:
    
        model = r1070alteracaoinfoSusp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1070alteracaonovaValidade(SoftDeletionModel):

    r1070_alteracao = models.ForeignKey('r1070.r1070alteracao', 
        related_name='%(class)s_r1070_alteracao', )
    
    def evento(self): 
        return self.r1070_alteracao.evento()
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
            unicode(self.r1070_alteracao),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informação preenchida exclusivamente em caso de alteração do período de validade das informações do registro identificado no evento, apresentando o novo período de validade'
        db_table = r'r1070_alteracao_novavalidade'       
        managed = True # r1070_alteracao_novavalidade #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_alteracao_novavalidade", "Can view r1070_alteracao_novavalidade"), )
            
        ordering = [
            'r1070_alteracao',
            'inivalid',]



class r1070alteracaonovaValidadeSerializer(ModelSerializer):

    class Meta:
    
        model = r1070alteracaonovaValidade
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1070exclusao(SoftDeletionModel):

    r1070_evttabprocesso = models.ForeignKey('efdreinf.r1070evtTabProcesso', 
        related_name='%(class)s_r1070_evttabprocesso', )
    
    def evento(self): 
        return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_TPPROC_EXCLUSAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
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
            unicode(self.r1070_evttabprocesso),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.inivalid),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Exclusão das informações'
        db_table = r'r1070_exclusao'       
        managed = True # r1070_exclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_exclusao", "Can view r1070_exclusao"), )
            
        ordering = [
            'r1070_evttabprocesso',
            'tpproc',
            'nrproc',
            'inivalid',]



class r1070exclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = r1070exclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1070inclusao(SoftDeletionModel):

    r1070_evttabprocesso = models.ForeignKey('efdreinf.r1070evtTabProcesso', 
        related_name='%(class)s_r1070_evttabprocesso', )
    
    def evento(self): 
        return self.r1070_evttabprocesso.evento()
    tpproc = models.IntegerField(choices=CHOICES_R1070_TPPROC_INCLUSAO, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    inivalid = models.CharField(choices=PERIODOS, max_length=7, null=True, )
    fimvalid = models.CharField(choices=PERIODOS, max_length=7, blank=True, null=True, )
    indautoria = models.IntegerField(choices=CHOICES_R1070_INDAUTORIA_INCLUSAO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1070_evttabprocesso),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.inivalid),
            unicode(self.indautoria),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Inclusão de novas informações'
        db_table = r'r1070_inclusao'       
        managed = True # r1070_inclusao #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_inclusao", "Can view r1070_inclusao"), )
            
        ordering = [
            'r1070_evttabprocesso',
            'tpproc',
            'nrproc',
            'inivalid',
            'indautoria',]



class r1070inclusaoSerializer(ModelSerializer):

    class Meta:
    
        model = r1070inclusao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1070inclusaodadosProcJud(SoftDeletionModel):

    r1070_inclusao = models.ForeignKey('r1070.r1070inclusao', 
        related_name='%(class)s_r1070_inclusao', )
    
    def evento(self): 
        return self.r1070_inclusao.evento()
    ufvara = models.CharField(choices=ESTADOS, max_length=2, null=True, )
    codmunic = models.TextField(null=True, )
    idvara = models.CharField(max_length=4, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1070_inclusao),
            unicode(self.ufvara),
            unicode(self.codmunic),
            unicode(self.idvara),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações Complementares do Processo Judicial'
        db_table = r'r1070_inclusao_dadosprocjud'       
        managed = True # r1070_inclusao_dadosprocjud #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_inclusao_dadosprocjud", "Can view r1070_inclusao_dadosprocjud"), )
            
        ordering = [
            'r1070_inclusao',
            'ufvara',
            'codmunic',
            'idvara',]



class r1070inclusaodadosProcJudSerializer(ModelSerializer):

    class Meta:
    
        model = r1070inclusaodadosProcJud
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r1070inclusaoinfoSusp(SoftDeletionModel):

    r1070_inclusao = models.ForeignKey('r1070.r1070inclusao', 
        related_name='%(class)s_r1070_inclusao', )
    
    def evento(self): 
        return self.r1070_inclusao.evento()
    codsusp = models.IntegerField(blank=True, null=True, )
    indsusp = models.CharField(choices=CHOICES_R1070_INDSUSP_INCLUSAO, max_length=2, null=True, )
    dtdecisao = models.DateField(null=True, )
    inddeposito = models.CharField(choices=CHOICES_R1070_INDDEPOSITO_INCLUSAO, max_length=1, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r1070_inclusao),
            unicode(self.indsusp),
            unicode(self.dtdecisao),
            unicode(self.inddeposito),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de Suspensão de Exibilidade de tributos'
        db_table = r'r1070_inclusao_infosusp'       
        managed = True # r1070_inclusao_infosusp #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r1070_inclusao_infosusp", "Can view r1070_inclusao_infosusp"), )
            
        ordering = [
            'r1070_inclusao',
            'indsusp',
            'dtdecisao',
            'inddeposito',]



class r1070inclusaoinfoSuspSerializer(ModelSerializer):

    class Meta:
    
        model = r1070inclusaoinfoSusp
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()