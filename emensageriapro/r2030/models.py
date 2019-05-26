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
from emensageriapro.r2030.choices import *
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





class r2030infoProc(SoftDeletionModel):

    r2030_recursosrec = models.ForeignKey('r2030.r2030recursosRec', 
        related_name='%(class)s_r2030_recursosrec', )
    
    def evento(self): 
        return self.r2030_recursosrec.evento()
    tpproc = models.IntegerField(choices=CHOICES_R2030_TPPROC, null=True, )
    nrproc = models.CharField(max_length=21, null=True, )
    codsusp = models.IntegerField(blank=True, null=True, )
    vlrnret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2030_recursosrec),
            unicode(self.tpproc),
            unicode(self.nrproc),
            unicode(self.vlrnret),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de processos relacionados a não retenção de contribuição previdenciária'
        db_table = r'r2030_infoproc'       
        managed = True # r2030_infoproc #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2030_infoproc", "Can view r2030_infoproc"), )
            
        ordering = [
            'r2030_recursosrec',
            'tpproc',
            'nrproc',
            'vlrnret',]



class r2030infoProcSerializer(ModelSerializer):

    class Meta:
    
        model = r2030infoProc
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2030infoRecurso(SoftDeletionModel):

    r2030_recursosrec = models.ForeignKey('r2030.r2030recursosRec', 
        related_name='%(class)s_r2030_recursosrec', )
    
    def evento(self): 
        return self.r2030_recursosrec.evento()
    tprepasse = models.IntegerField(choices=CHOICES_R2030_TPREPASSE, null=True, )
    descrecurso = models.CharField(max_length=20, null=True, )
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrretapur = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2030_recursosrec),
            unicode(self.tprepasse),
            unicode(self.descrecurso),
            unicode(self.vlrbruto),
            unicode(self.vlrretapur),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Detalhamento dos recursos recebidos.'
        db_table = r'r2030_inforecurso'       
        managed = True # r2030_inforecurso #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2030_inforecurso", "Can view r2030_inforecurso"), )
            
        ordering = [
            'r2030_recursosrec',
            'tprepasse',
            'descrecurso',
            'vlrbruto',
            'vlrretapur',]



class r2030infoRecursoSerializer(ModelSerializer):

    class Meta:
    
        model = r2030infoRecurso
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r2030recursosRec(SoftDeletionModel):

    r2030_evtassocdesprec = models.ForeignKey('efdreinf.r2030evtAssocDespRec', 
        related_name='%(class)s_r2030_evtassocdesprec', )
    
    def evento(self): 
        return self.r2030_evtassocdesprec.evento()
    cnpjorigrecurso = models.CharField(max_length=14, null=True, )
    vlrtotalrec = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalnret = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r2030_evtassocdesprec),
            unicode(self.cnpjorigrecurso),
            unicode(self.vlrtotalrec),
            unicode(self.vlrtotalret),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Registro preenchido exclusivamente por associação desportiva que mantenha equipe de futebol profissional, quando receber repasse de outras empresas a título de patrocínio, publicidade, licenciamento, etc'
        db_table = r'r2030_recursosrec'       
        managed = True # r2030_recursosrec #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r2030_recursosrec", "Can view r2030_recursosrec"), )
            
        ordering = [
            'r2030_evtassocdesprec',
            'cnpjorigrecurso',
            'vlrtotalrec',
            'vlrtotalret',]



class r2030recursosRecSerializer(ModelSerializer):

    class Meta:
    
        model = r2030recursosRec
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()