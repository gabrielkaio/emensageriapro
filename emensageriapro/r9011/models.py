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
from emensageriapro.r9011.choices import *
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





class r9011RCPRB(SoftDeletionModel):

    r9011_infototalcontrib = models.ForeignKey('r9011.r9011infoTotalContrib', 
        related_name='%(class)s_r9011_infototalcontrib', )
    
    def evento(self): 
        return self.r9011_infototalcontrib.evento()
    crcprb = models.IntegerField(null=True, )
    vlrcrcprb = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrcprbsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9011_infototalcontrib),
            unicode(self.crcprb),
            unicode(self.vlrcrcprb),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador da contribuição previdenciária sobre a Receita Bruta - CPRB, apuradas no evento R-2060'
        db_table = r'r9011_rcprb'       
        managed = True # r9011_rcprb #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_rcprb", "Can view r9011_rcprb"), )
            
        ordering = [
            'r9011_infototalcontrib',
            'crcprb',
            'vlrcrcprb',]



class r9011RCPRBSerializer(ModelSerializer):

    class Meta:
    
        model = r9011RCPRB
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9011RComl(SoftDeletionModel):

    r9011_infototalcontrib = models.ForeignKey('r9011.r9011infoTotalContrib', 
        related_name='%(class)s_r9011_infototalcontrib', )
    
    def evento(self): 
        return self.r9011_infototalcontrib.evento()
    crcoml = models.IntegerField(null=True, )
    vlrcrcoml = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrcomlsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9011_infototalcontrib),
            unicode(self.crcoml),
            unicode(self.vlrcrcoml),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das contribuições sociais incidentes sobre a comercialização de produção por Produtor Rural Pessoa Jurídica e Agroindústria, apuradas no evento R-2050'
        db_table = r'r9011_rcoml'       
        managed = True # r9011_rcoml #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_rcoml", "Can view r9011_rcoml"), )
            
        ordering = [
            'r9011_infototalcontrib',
            'crcoml',
            'vlrcrcoml',]



class r9011RComlSerializer(ModelSerializer):

    class Meta:
    
        model = r9011RComl
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9011RPrest(SoftDeletionModel):

    r9011_infototalcontrib = models.ForeignKey('r9011.r9011infoTotalContrib', 
        related_name='%(class)s_r9011_infototalcontrib', )
    
    def evento(self): 
        return self.r9011_infototalcontrib.evento()
    tpinsctomador = models.IntegerField(null=True, )
    nrinsctomador = models.CharField(max_length=14, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretprinc = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrtotalretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretprinc = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrtotalnretadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9011_infototalcontrib),
            unicode(self.tpinsctomador),
            unicode(self.nrinsctomador),
            unicode(self.vlrtotalbaseret),
            unicode(self.vlrtotalretprinc),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre serviços prestados, apuradas no evento R-2020'
        db_table = r'r9011_rprest'       
        managed = True # r9011_rprest #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_rprest", "Can view r9011_rprest"), )
            
        ordering = [
            'r9011_infototalcontrib',
            'tpinsctomador',
            'nrinsctomador',
            'vlrtotalbaseret',
            'vlrtotalretprinc',]



class r9011RPrestSerializer(ModelSerializer):

    class Meta:
    
        model = r9011RPrest
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9011RRecRepAD(SoftDeletionModel):

    r9011_infototalcontrib = models.ForeignKey('r9011.r9011infoTotalContrib', 
        related_name='%(class)s_r9011_infototalcontrib', )
    
    def evento(self): 
        return self.r9011_infototalcontrib.evento()
    crrecrepad = models.IntegerField(null=True, )
    vlrcrrecrepad = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    vlrcrrecrepadsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9011_infototalcontrib),
            unicode(self.crrecrepad),
            unicode(self.vlrcrrecrepad),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das bases de cálculo e das retenções de contribuição previdenciária sobre recursos repassados a Associações Desportivas que mantenham equipe de futebol profissional, apuradas no evento R-2040'
        db_table = r'r9011_rrecrepad'       
        managed = True # r9011_rrecrepad #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_rrecrepad", "Can view r9011_rrecrepad"), )
            
        ordering = [
            'r9011_infototalcontrib',
            'crrecrepad',
            'vlrcrrecrepad',]



class r9011RRecRepADSerializer(ModelSerializer):

    class Meta:
    
        model = r9011RRecRepAD
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9011RTom(SoftDeletionModel):

    r9011_infototalcontrib = models.ForeignKey('r9011.r9011infoTotalContrib', 
        related_name='%(class)s_r9011_infototalcontrib', )
    
    def evento(self): 
        return self.r9011_infototalcontrib.evento()
    cnpjprestador = models.CharField(max_length=14, null=True, )
    cno = models.CharField(max_length=12, blank=True, null=True, )
    vlrtotalbaseret = models.DecimalField(max_digits=15, decimal_places=2, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9011_infototalcontrib),
            unicode(self.cnpjprestador),
            unicode(self.vlrtotalbaseret),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados, apuradas no evento R-2010'
        db_table = r'r9011_rtom'       
        managed = True # r9011_rtom #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_rtom", "Can view r9011_rtom"), )
            
        ordering = [
            'r9011_infototalcontrib',
            'cnpjprestador',
            'vlrtotalbaseret',]



class r9011RTomSerializer(ModelSerializer):

    class Meta:
    
        model = r9011RTom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9011infoCRTom(SoftDeletionModel):

    r9011_rtom = models.ForeignKey('r9011.r9011RTom', 
        related_name='%(class)s_r9011_rtom', )
    
    def evento(self): 
        return self.r9011_rtom.evento()
    crtom = models.IntegerField(null=True, )
    vlrcrtom = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    vlrcrtomsusp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9011_rtom),
            unicode(self.crtom),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Totalizador das retenções de contribuição previdenciária sobre serviços tomados'
        db_table = r'r9011_infocrtom'       
        managed = True # r9011_infocrtom #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_infocrtom", "Can view r9011_infocrtom"), )
            
        ordering = [
            'r9011_rtom',
            'crtom',]



class r9011infoCRTomSerializer(ModelSerializer):

    class Meta:
    
        model = r9011infoCRTom
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9011infoTotalContrib(SoftDeletionModel):

    r9011_evttotalcontrib = models.ForeignKey('efdreinf.r9011evtTotalContrib', 
        related_name='%(class)s_r9011_evttotalcontrib', )
    
    def evento(self): 
        return self.r9011_evttotalcontrib.evento()
    nrrecarqbase = models.CharField(max_length=52, blank=True, null=True, )
    indexistinfo = models.IntegerField(choices=CHOICES_R9011_INDEXISTINFO, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9011_evttotalcontrib),
            unicode(self.indexistinfo),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações consolidadas por contribuinte relativas a totalizadores de bases e tributos'
        db_table = r'r9011_infototalcontrib'       
        managed = True # r9011_infototalcontrib #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_infototalcontrib", "Can view r9011_infototalcontrib"), )
            
        ordering = [
            'r9011_evttotalcontrib',
            'indexistinfo',]



class r9011infoTotalContribSerializer(ModelSerializer):

    class Meta:
    
        model = r9011infoTotalContrib
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()


class r9011regOcorrs(SoftDeletionModel):

    r9011_evttotalcontrib = models.ForeignKey('efdreinf.r9011evtTotalContrib', 
        related_name='%(class)s_r9011_evttotalcontrib', )
    
    def evento(self): 
        return self.r9011_evttotalcontrib.evento()
    tpocorr = models.IntegerField(choices=CHOICES_R9011_TPOCORR, null=True, )
    localerroaviso = models.CharField(max_length=200, null=True, )
    codresp = models.CharField(max_length=6, null=True, )
    dscresp = models.CharField(max_length=999, null=True, )
    
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    
    def __unicode__(self):
        
        lista = [
            unicode(self.r9011_evttotalcontrib),
            unicode(self.tpocorr),
            unicode(self.localerroaviso),
            unicode(self.codresp),
            unicode(self.dscresp),]
            
        if lista:
            return ' - '.join(lista)
            
        else:
            return self.id
        
    class Meta:
    
        # verbose_name = u'Informações de ocorrências registradas'
        db_table = r'r9011_regocorrs'       
        managed = True # r9011_regocorrs #
        
        unique_together = ()
            
        index_together = ()
        
        permissions = (
            ("can_view_r9011_regocorrs", "Can view r9011_regocorrs"), )
            
        ordering = [
            'r9011_evttotalcontrib',
            'tpocorr',
            'localerroaviso',
            'codresp',
            'dscresp',]



class r9011regOcorrsSerializer(ModelSerializer):

    class Meta:
    
        model = r9011regOcorrs
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
    
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()