#coding: utf-8



from django.db import models
from django.db.models import Sum
from django.db.models import Count
from rest_framework.serializers import ModelSerializer
from django.apps import apps
get_model = apps.get_model



CHOICES_R2020_TPPROCRETADIC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

CHOICES_R2020_TPPROCRETPRINC = (
    (1, u'1 - Administrativo'),
    (2, u'2 - Judicial'),
)

class r2020infoProcRetAd(models.Model):
    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest',
        related_name='%(class)s_r2020_evtservprest')
    def evento(self): return self.r2020_evtservprest.evento()
    tpprocretadic = models.IntegerField(choices=CHOICES_R2020_TPPROCRETADIC)
    nrprocretadic = models.CharField(max_length=21)
    codsuspadic = models.IntegerField(blank=True, null=True)
    valoradic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2020_evtservprest) + ' - ' + unicode(self.tpprocretadic) + ' - ' + unicode(self.nrprocretadic) + ' - ' + unicode(self.codsuspadic) + ' - ' + unicode(self.valoradic)
    #r2020_infoprocretad_custom#
    #r2020_infoprocretad_custom#
    class Meta:
        db_table = r'r2020_infoprocretad'
        managed = True
        ordering = ['r2020_evtservprest', 'tpprocretadic', 'nrprocretadic', 'codsuspadic', 'valoradic']



class r2020infoProcRetAdSerializer(ModelSerializer):
    class Meta:
        model = r2020infoProcRetAd
        fields = '__all__'
            

class r2020infoProcRetPr(models.Model):
    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest',
        related_name='%(class)s_r2020_evtservprest')
    def evento(self): return self.r2020_evtservprest.evento()
    tpprocretprinc = models.IntegerField(choices=CHOICES_R2020_TPPROCRETPRINC)
    nrprocretprinc = models.CharField(max_length=21)
    codsuspprinc = models.IntegerField(blank=True, null=True)
    valorprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2020_evtservprest) + ' - ' + unicode(self.tpprocretprinc) + ' - ' + unicode(self.nrprocretprinc) + ' - ' + unicode(self.codsuspprinc) + ' - ' + unicode(self.valorprinc)
    #r2020_infoprocretpr_custom#
    #r2020_infoprocretpr_custom#
    class Meta:
        db_table = r'r2020_infoprocretpr'
        managed = True
        ordering = ['r2020_evtservprest', 'tpprocretprinc', 'nrprocretprinc', 'codsuspprinc', 'valorprinc']



class r2020infoProcRetPrSerializer(ModelSerializer):
    class Meta:
        model = r2020infoProcRetPr
        fields = '__all__'
            

class r2020infoTpServ(models.Model):
    r2020_nfs = models.ForeignKey('r2020nfs',
        related_name='%(class)s_r2020_nfs')
    def evento(self): return self.r2020_nfs.evento()
    tpservico = models.IntegerField()
    vlrbaseret = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretencao = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    vlrretsub = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrnretprinc = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos15 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos20 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrservicos25 = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlradicional = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    vlrnretadic = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2020_nfs) + ' - ' + unicode(self.tpservico) + ' - ' + unicode(self.vlrbaseret) + ' - ' + unicode(self.vlrretencao) + ' - ' + unicode(self.vlrretsub) + ' - ' + unicode(self.vlrnretprinc) + ' - ' + unicode(self.vlrservicos15) + ' - ' + unicode(self.vlrservicos20) + ' - ' + unicode(self.vlrservicos25) + ' - ' + unicode(self.vlradicional) + ' - ' + unicode(self.vlrnretadic)
    #r2020_infotpserv_custom#
    #r2020_infotpserv_custom#
    class Meta:
        db_table = r'r2020_infotpserv'
        managed = True
        ordering = ['r2020_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao', 'vlrretsub', 'vlrnretprinc', 'vlrservicos15', 'vlrservicos20', 'vlrservicos25', 'vlradicional', 'vlrnretadic']



class r2020infoTpServSerializer(ModelSerializer):
    class Meta:
        model = r2020infoTpServ
        fields = '__all__'
            

class r2020nfs(models.Model):
    r2020_evtservprest = models.ForeignKey('efdreinf.r2020evtServPrest',
        related_name='%(class)s_r2020_evtservprest')
    def evento(self): return self.r2020_evtservprest.evento()
    serie = models.CharField(max_length=5)
    numdocto = models.CharField(max_length=15)
    dtemissaonf = models.DateField()
    vlrbruto = models.DecimalField(max_digits=15, decimal_places=2, max_length=14)
    obs = models.CharField(max_length=250, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)
    def __unicode__(self):
        return unicode(self.r2020_evtservprest) + ' - ' + unicode(self.serie) + ' - ' + unicode(self.numdocto) + ' - ' + unicode(self.dtemissaonf) + ' - ' + unicode(self.vlrbruto) + ' - ' + unicode(self.obs)
    #r2020_nfs_custom#
    #r2020_nfs_custom#
    class Meta:
        db_table = r'r2020_nfs'
        managed = True
        ordering = ['r2020_evtservprest', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto', 'obs']



class r2020nfsSerializer(ModelSerializer):
    class Meta:
        model = r2020nfs
        fields = '__all__'
            

#VIEWS_MODELS
