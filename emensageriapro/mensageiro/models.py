#coding: utf-8

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

from django.db import models
from django.db.models import Sum
from django.db.models import Count
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from emensageriapro.soft_delete import SoftDeletionModel
get_model = apps.get_model



CHOICES_S1000_TPINSC = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

CHOICES_S1050_INCLUSAO_PERHORFLEXIVEL = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S1050_INCLUSAO_TPINTERV = (
    (1, u'1 - Intervalo em Horário Fixo'),
    (2, u'2 - Intervalo em Horário Variável'),
)

CHOICES_S2200_DIA = (
    (1, u'1 - Segunda-Feira'),
    (2, u'2 - Terça-Feira'),
    (3, u'3 - Quarta-Feira'),
    (4, u'4 - Quinta-Feira'),
    (5, u'5 - Sexta-Feira'),
    (6, u'6 - Sábado'),
    (7, u'7 - Domingo'),
    (8, u'8 - Dia variável'),
)

CHOICES_S2200_INFOCOTA = (
    ('N', u'N - Não'),
    ('S', u'S - Sim'),
)

CHOICES_S2200_TMPPARC = (
    (0, u'0 - Não é contrato em tempo parcial'),
    (1, u'1 - Limitado a 25 horas semanais'),
    (2, u'2 - Limitado a 30 horas semanais'),
    (3, u'3 - Limitado a 26 horas semanais'),
)

CHOICES_S2200_TPCONTR = (
    (1, u'1 - Prazo indeterminado'),
    (2, u'2 - Prazo determinado'),
)

CHOICES_S2200_TPJORNADA = (
    (1, u'1 - Jornada com horário diário e folga fixos'),
    (2, u'2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)'),
    (3, u'3 - Jornada com horário diário fixo e folga variável'),
    (9, u'9 - Demais tipos de jornada'),
)

CHOICES_S2200_TPREGJOR = (
    (1, u'1 - Submetidos a Horário de Trabalho (Cap. II da CLT)'),
    (2, u'2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT'),
    (3, u'3 - Funções especificadas no Inciso II do Art. 62 da CLT'),
    (4, u'4 - Teletrabalho, previsto no Inciso III do Art. 62 da CLT'),
)

CHOICES_S2200_UNDSALFIXO = (
    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável'),
)

CODIGO_RESPOSTA = (
    (0, u'Cadastrado'),
    (101, u'101 - Lote Aguardando Processamento'),
    (201, u'201 - Lote Processado com Sucesso'),
    (202, u'202 - Lote Processado com Advertências'),
    (301, u'301 - Erro Servidor eSocial'),
    (401, u'401 - Lote Incorreto - Erro preenchimento'),
    (402, u'402 - Lote Incorreto - schema Inválido'),
    (403, u'403 - Lote Incorreto - Versão do Schema não permitida'),
    (404, u'404 - Lote Incorreto - Erro Certificado'),
    (405, u'405 - Lote Incorreto - Lote nulo ou vazio'),
    (501, u'501 - Solicitação de Consulta Incorreta - Erro Preenchimento'),
    (502, u'502 - Solicitação de Consulta Incorreta - Schema Inválido.'),
    (503, u'503 - Solicitação de Consulta Incorreta - Versão do Schema Não Permitida.'),
    (504, u'504 - Solicitação de Consulta Incorreta - Erro Certificado.'),
    (505, u'505 - Solicitação de Consulta Incorreta - Consulta nula ou vazia.'),
)

CODIGO_STATUS_EFDREINF = (
    (0, u'0 - Sucesso'),
    (1, u'1 - Erro'),
    (2, u'2 - Em Processamento'),
)

EVENTOS_GRUPOS = (
    (1, u'1 - Eventos de Tabelas'),
    (2, u'2 - Eventos Não Periódicos'),
    (3, u'3 - Eventos Periódicos'),
)

EVENTOS_OCORRENCIAS_TIPO = (
    (1, u'1 - Erro'),
    (2, u'2 - Advertência'),
)

EVENTOS_OCORRENCIAS_TIPO_EFDREINF = (
    (1, u'1 - Aviso'),
    (2, u'2 - Erro'),
)

IMPORTACAO_STATUS = (
    (0, u'Aguardando'),
    (1, u'Processando'),
    (2, u'Processado com sucesso'),
    (3, u'Erro - Processamento'),
    (4, u'Erro - Outros'),
    (5, u'Erro - Arquivo Inválido'),
    (6, u'Erro - Identidade já existente'),
    (7, u'Erro - Versão de leiaute incompatível'),
    (8, u'Erro - Validação de Leiaute'),
)

SIM_NAO = (
    (0, u'Não'),
    (1, u'Sim'),
)

TIPO_AMBIENTE = (
    (1, u'1 - Produção'),
    (2, u'2 - Produção restrita'),
)

TIPO_INSCRICAO = (
    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
)

TIPO_OCORRENCIA = (
    (1, u'1 - Erro'),
    (2, u'2 - Advertência'),
)

TRANSMISSOR_STATUS = (
    (0, u'Cadastrado'),
    (1, u'Enviado'),
    (2, u'Erro no envio'),
    (3, u'Consultado'),
    (4, u'Erro na consulta'),
)

class Arquivos(SoftDeletionModel):
    arquivo = models.CharField(max_length=300)
    data_criacao = models.DateField()
    permite_recuperacao = models.IntegerField(choices=SIM_NAO)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    #arquivos_custom#

    class Meta:
        db_table = r'arquivos'       
        managed = True # arquivos #
        permissions = (
            ("can_view_arquivos", "Can view arquivos"),
            #custom_permissions_arquivos
        )



class ArquivosSerializer(ModelSerializer):
    class Meta:
        model = Arquivos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class ImportacaoArquivos(SoftDeletionModel):
    arquivo = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(choices=IMPORTACAO_STATUS, blank=True)
    data_hora = models.DateTimeField(blank=True)
    importado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_importado_por', blank=True, null=True)
    quant_total = models.IntegerField(blank=True, null=True)
    quant_aguardando = models.IntegerField(blank=True, null=True)
    quant_processado = models.IntegerField(blank=True, null=True)
    quant_importado = models.IntegerField(blank=True, null=True)
    quant_erros = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.arquivo)
    #importacao_arquivos_custom#

    class Meta:
        db_table = r'importacao_arquivos'       
        managed = True # importacao_arquivos #
        permissions = (
            ("can_view_importacao_arquivos", "Can view importacao_arquivos"),
            #custom_permissions_importacao_arquivos
        )
        ordering = ['arquivo']



class ImportacaoArquivosSerializer(ModelSerializer):
    class Meta:
        model = ImportacaoArquivos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class ImportacaoArquivosEventos(SoftDeletionModel):
    importacao_arquivos = models.ForeignKey('ImportacaoArquivos',
        related_name='%(class)s_importacao_arquivos', blank=True)
    arquivo = models.CharField(max_length=200, blank=True, null=True)
    evento = models.CharField(max_length=100, blank=True, null=True)
    versao = models.CharField(max_length=30, blank=True, null=True)
    identidade_evento = models.CharField(max_length=100, blank=True, null=True)
    identidade = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(choices=IMPORTACAO_STATUS, blank=True, null=True)
    data_hora = models.DateTimeField(blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.importacao_arquivos) + ' - ' + unicode(self.arquivo) + ' - ' + unicode(self.evento) + ' - ' + unicode(self.versao) + ' - ' + unicode(self.identidade_evento) + ' - ' + unicode(self.identidade)
    #importacao_arquivos_eventos_custom#

    class Meta:
        db_table = r'importacao_arquivos_eventos'       
        managed = True # importacao_arquivos_eventos #
        permissions = (
            ("can_view_importacao_arquivos_eventos", "Can view importacao_arquivos_eventos"),
            #custom_permissions_importacao_arquivos_eventos
        )
        ordering = ['importacao_arquivos', 'arquivo', 'evento', 'versao', 'identidade_evento', 'identidade']



class ImportacaoArquivosEventosSerializer(ModelSerializer):
    class Meta:
        model = ImportacaoArquivosEventos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class RegrasDeValidacao(SoftDeletionModel):
    evento = models.CharField(max_length=5000)
    versao = models.CharField(max_length=20, blank=True)
    numero = models.IntegerField()
    registro_campo = models.CharField(max_length=100)
    registro_pai = models.CharField(max_length=100)
    elemento = models.CharField(max_length=2)
    tipo = models.CharField(max_length=1)
    ocorrencias = models.CharField(max_length=10)
    tamanho = models.CharField(max_length=10)
    casas_decimais = models.CharField(max_length=10)
    obrigatorio = models.IntegerField(choices=SIM_NAO, blank=True)
    descricao = models.TextField(blank=True)
    tabela = models.CharField(max_length=200, blank=True, null=True)
    valores_validos = models.TextField(blank=True, null=True)
    validacoes_precedencia = models.TextField(blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.evento) + ' - ' + unicode(self.versao) + ' - ' + unicode(self.numero) + ' - ' + unicode(self.registro_campo) + ' - ' + unicode(self.registro_pai)
    #regras_validacao_custom#

    class Meta:
        db_table = r'regras_validacao'       
        managed = True # regras_validacao #
        permissions = (
            ("can_view_regras_validacao", "Can view regras_validacao"),
            #custom_permissions_regras_validacao
        )



class RegrasDeValidacaoSerializer(ModelSerializer):
    class Meta:
        model = RegrasDeValidacao
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class Relatorios(SoftDeletionModel):
    titulo = models.CharField(max_length=500)
    campos = models.CharField(max_length=500)
    sql = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    #relatorios_custom#

    class Meta:
        db_table = r'relatorios'       
        managed = True # relatorios #
        permissions = (
            ("can_view_relatorios", "Can view relatorios"),
            #custom_permissions_relatorios
        )



class RelatoriosSerializer(ModelSerializer):
    class Meta:
        model = Relatorios
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class RetornosEventos(SoftDeletionModel):
    transmissor_lote_esocial = models.ForeignKey('TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial')
    identidade = models.CharField(max_length=36, blank=True, null=True)
    recepcao_tp_amb = models.IntegerField(choices=TIPO_AMBIENTE, blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(blank=True, null=True)
    recepcao_versao_app = models.CharField(max_length=30, blank=True, null=True)
    recepcao_protocolo_envio_lote = models.CharField(max_length=30, blank=True, null=True)
    processamento_codigo_resposta = models.CharField(max_length=10, blank=True, null=True)
    processamento_descricao_resposta = models.TextField(blank=True, null=True)
    processamento_versao_app_processamento = models.CharField(max_length=30, blank=True, null=True)
    processamento_data_hora = models.DateTimeField(blank=True, null=True)
    recibo_numero = models.CharField(max_length=100, blank=True, null=True)
    recibo_hash = models.CharField(max_length=100, blank=True, null=True)
    tpinsc = models.IntegerField(choices=CHOICES_S1000_TPINSC, blank=True, null=True)
    empregador_tpinsc = models.IntegerField(choices=CHOICES_S1000_TPINSC, blank=True, null=True)
    nrinsc = models.CharField(max_length=15, blank=True, null=True)
    empregador_nrinsc = models.CharField(max_length=15, blank=True, null=True)
    cpftrab = models.CharField(max_length=11, blank=True, null=True)
    nistrab = models.CharField(max_length=11, blank=True, null=True)
    nmtrab = models.CharField(max_length=70, blank=True, null=True)
    infocota = models.CharField(choices=CHOICES_S2200_INFOCOTA, max_length=50, blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    dtadm = models.DateField(blank=True, null=True)
    tpregjor = models.IntegerField(choices=CHOICES_S2200_TPREGJOR, blank=True, null=True)
    dtbase = models.IntegerField(blank=True, null=True)
    cnpjsindcategprof = models.CharField(max_length=14, blank=True, null=True)
    dtposse = models.DateField(blank=True, null=True)
    dtexercicio = models.DateField(blank=True, null=True)
    codcargo = models.CharField(max_length=30, blank=True, null=True)
    nmcargo = models.CharField(max_length=100, blank=True, null=True)
    codcbocargo = models.CharField(max_length=6, blank=True, null=True)
    codfuncao = models.CharField(max_length=30, blank=True, null=True)
    dscfuncao = models.CharField(max_length=100, blank=True, null=True)
    codcbofuncao = models.CharField(max_length=6, blank=True, null=True)
    codcateg = models.IntegerField(blank=True, null=True)
    vrsalfx = models.DecimalField(max_digits=15, decimal_places=2, max_length=14, blank=True, null=True)
    undsalfixo = models.IntegerField(choices=CHOICES_S2200_UNDSALFIXO, blank=True, null=True)
    dscsalvar = models.CharField(max_length=255, blank=True, null=True)
    tpcontr = models.IntegerField(choices=CHOICES_S2200_TPCONTR, blank=True, null=True)
    dtterm = models.DateField(blank=True, null=True)
    clauasseg = models.CharField(max_length=50, blank=True, null=True)
    local_tpinsc = models.IntegerField(choices=CHOICES_S1000_TPINSC, blank=True, null=True)
    local_nrinsc = models.CharField(max_length=15, blank=True, null=True)
    local_cnae = models.IntegerField(blank=True, null=True)
    qtdhrssem = models.DecimalField(max_digits=15, decimal_places=2, max_length=4, blank=True, null=True)
    tpjornada = models.IntegerField(choices=CHOICES_S2200_TPJORNADA, blank=True, null=True)
    dsctpjorn = models.CharField(max_length=100, blank=True, null=True)
    tmpparc = models.IntegerField(choices=CHOICES_S2200_TMPPARC, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.transmissor_lote_esocial) + ' - ' + unicode(self.identidade)
    #retornos_eventos_custom#

    class Meta:
        db_table = r'retornos_eventos'       
        managed = True # retornos_eventos #
        permissions = (
            ("can_view_retornos_eventos", "Can view retornos_eventos"),
            #custom_permissions_retornos_eventos
        )
        ordering = ['transmissor_lote_esocial', 'identidade']



class RetornosEventosSerializer(ModelSerializer):
    class Meta:
        model = RetornosEventos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class RetornosEventosHorarios(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True, null=True)
    dia = models.IntegerField(choices=CHOICES_S2200_DIA, blank=True, null=True)
    codhorcontrat = models.CharField(max_length=30, blank=True, null=True)
    hrentr = models.CharField(max_length=50, blank=True, null=True)
    hrsaida = models.CharField(max_length=50, blank=True, null=True)
    durjornada = models.IntegerField(blank=True, null=True)
    perhorflexivel = models.CharField(choices=CHOICES_S1050_INCLUSAO_PERHORFLEXIVEL, max_length=50, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    #retornos_eventos_horarios_custom#

    class Meta:
        db_table = r'retornos_eventos_horarios'       
        managed = True # retornos_eventos_horarios #
        permissions = (
            ("can_view_retornos_eventos_horarios", "Can view retornos_eventos_horarios"),
            #custom_permissions_retornos_eventos_horarios
        )



class RetornosEventosHorariosSerializer(ModelSerializer):
    class Meta:
        model = RetornosEventosHorarios
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class RetornosEventosIntervalos(SoftDeletionModel):
    retornos_eventos_horarios = models.ForeignKey('RetornosEventosHorarios',
        related_name='%(class)s_retornos_eventos_horarios', blank=True, null=True)
    tpinterv = models.IntegerField(choices=CHOICES_S1050_INCLUSAO_TPINTERV, blank=True, null=True)
    durinterv = models.IntegerField(blank=True, null=True)
    iniinterv = models.CharField(max_length=50, blank=True, null=True)
    terminterv = models.CharField(max_length=50, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    #retornos_eventos_intervalos_custom#

    class Meta:
        db_table = r'retornos_eventos_intervalos'       
        managed = True # retornos_eventos_intervalos #
        permissions = (
            ("can_view_retornos_eventos_intervalos", "Can view retornos_eventos_intervalos"),
            #custom_permissions_retornos_eventos_intervalos
        )



class RetornosEventosIntervalosSerializer(ModelSerializer):
    class Meta:
        model = RetornosEventosIntervalos
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class RetornosEventosOcorrencias(SoftDeletionModel):
    retornos_eventos = models.ForeignKey('RetornosEventos',
        related_name='%(class)s_retornos_eventos', blank=True)
    tipo = models.IntegerField(choices=TIPO_OCORRENCIA, blank=True)
    codigo = models.IntegerField(blank=True)
    descricao = models.TextField(blank=True)
    localizacao = models.TextField(max_length=30, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    #retornos_eventos_ocorrencias_custom#

    class Meta:
        db_table = r'retornos_eventos_ocorrencias'       
        managed = True # retornos_eventos_ocorrencias #
        permissions = (
            ("can_view_retornos_eventos_ocorrencias", "Can view retornos_eventos_ocorrencias"),
            #custom_permissions_retornos_eventos_ocorrencias
        )



class RetornosEventosOcorrenciasSerializer(ModelSerializer):
    class Meta:
        model = RetornosEventosOcorrencias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class TransmissorLote(SoftDeletionModel):
    transmissor_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO)
    transmissor_nrinsc = models.CharField(max_length=20)
    nome_empresa = models.CharField(max_length=200, unique=True)
    data_abertura = models.DateField()
    validar_eventos = models.IntegerField(choices=SIM_NAO)
    verificar_predecessao = models.IntegerField(choices=SIM_NAO)
    envio_automatico = models.IntegerField(choices=SIM_NAO)
    logotipo = models.FileField(upload_to="logotipo", blank=True, null=True)
    endereco_completo = models.TextField()
    empregador_tpinsc = models.CharField(max_length=20)
    empregador_nrinsc = models.IntegerField(choices=TIPO_INSCRICAO)
    esocial_lote_min = models.IntegerField()
    esocial_lote_max = models.IntegerField()
    esocial_timeout = models.DecimalField(max_digits=15, decimal_places=2)
    esocial_intervalo = models.IntegerField()
    esocial_tempo_prox_envio = models.IntegerField(blank=True, null=True)
    esocial_certificado = models.FileField(upload_to="esocial_certificado", blank=True, null=True)
    esocial_senha = models.CharField(max_length=20, blank=True, null=True)
    esocial_pasta = models.CharField(max_length=200, blank=True, null=True)
    contribuinte_tpinsc = models.CharField(max_length=20)
    contribuinte_nrinsc = models.IntegerField(choices=TIPO_INSCRICAO)
    efdreinf_lote_min = models.IntegerField()
    efdreinf_lote_max = models.IntegerField()
    efdreinf_timeout = models.DecimalField(max_digits=15, decimal_places=2)
    efdreinf_intervalo = models.IntegerField()
    efdreinf_tempo_prox_envio = models.IntegerField(blank=True, null=True)
    efdreinf_certificado = models.FileField(upload_to="efdreinf_certificado", blank=True, null=True)
    efdreinf_senha = models.CharField(max_length=20, blank=True, null=True)
    efdreinf_pasta = models.CharField(max_length=200, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.transmissor_nrinsc) + ' - ' + unicode(self.nome_empresa) + ' - ' + unicode(self.empregador_tpinsc) + ' - ' + unicode(self.contribuinte_tpinsc)
    #transmissores_custom#

    class Meta:
        db_table = r'transmissores'       
        managed = True # transmissores #
        permissions = (
            ("can_view_transmissores", "Can view transmissores"),
            #custom_permissions_transmissores
        )



class TransmissorLoteSerializer(ModelSerializer):
    class Meta:
        model = TransmissorLote
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class TransmissorLoteEfdreinf(SoftDeletionModel):
    transmissor = models.ForeignKey('TransmissorLote',
        related_name='%(class)s_transmissor', max_length=1, blank=True, null=True)
    contribuinte_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO)
    contribuinte_nrinsc = models.CharField(max_length=15)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, blank=True, default=0)
    identidade_transmissor = models.CharField(max_length=20, blank=True, null=True)
    codigo_status = models.IntegerField(choices=CODIGO_STATUS_EFDREINF, blank=True, null=True)
    retorno_descricao = models.TextField(blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(max_length=50, blank=True, null=True)
    recepcao_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True)
    protocolo = models.CharField(max_length=50, blank=True, null=True)
    numero_protocolo_fechamento = models.CharField(max_length=50, blank=True, null=True)
    processamento_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True)
    tempo_estimado_conclusao = models.IntegerField(blank=True, null=True)
    arquivo_header = models.CharField(max_length=200, blank=True, null=True)
    arquivo_request = models.CharField(max_length=200, blank=True, null=True)
    arquivo_response = models.CharField(max_length=200, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.transmissor) + ' - ' + unicode(self.contribuinte_tpinsc) + ' - ' + unicode(self.contribuinte_nrinsc) + ' - ' + unicode(self.identidade_transmissor) + ' - ' + unicode(self.codigo_status) + ' - ' + unicode(self.retorno_descricao)
    #transmissor_lote_efdreinf_custom#

    class Meta:
        db_table = r'transmissor_lote_efdreinf'       
        managed = True # transmissor_lote_efdreinf #
        permissions = (
            ("can_view_transmissor_lote_efdreinf", "Can view transmissor_lote_efdreinf"),
            #custom_permissions_transmissor_lote_efdreinf
        )



class TransmissorLoteEfdreinfSerializer(ModelSerializer):
    class Meta:
        model = TransmissorLoteEfdreinf
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class TransmissorLoteEfdreinfOcorrencias(SoftDeletionModel):
    transmissor_lote_efdreinf = models.ForeignKey('TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True)
    resposta_codigo = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(blank=True)
    tipo = models.IntegerField(choices=EVENTOS_OCORRENCIAS_TIPO_EFDREINF, blank=True)
    localizacao = models.CharField(max_length=50, blank=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    #transmissor_lote_efdreinf_ocorrencias_custom#

    class Meta:
        db_table = r'transmissor_lote_efdreinf_ocorrencias'       
        managed = True # transmissor_lote_efdreinf_ocorrencias #
        permissions = (
            ("can_view_transmissor_lote_efdreinf_ocorrencias", "Can view transmissor_lote_efdreinf_ocorrencias"),
            #custom_permissions_transmissor_lote_efdreinf_ocorrencias
        )



class TransmissorLoteEfdreinfOcorrenciasSerializer(ModelSerializer):
    class Meta:
        model = TransmissorLoteEfdreinfOcorrencias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class TransmissorLoteEsocial(SoftDeletionModel):
    transmissor = models.ForeignKey('TransmissorLote',
        related_name='%(class)s_transmissor', max_length=1, blank=True, null=True)
    empregador_tpinsc = models.IntegerField(choices=TIPO_INSCRICAO)
    empregador_nrinsc = models.CharField(max_length=15)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    status = models.IntegerField(choices=TRANSMISSOR_STATUS, blank=True, default=0)
    resposta_codigo = models.IntegerField(choices=CODIGO_RESPOSTA, blank=True, null=True)
    resposta_descricao = models.TextField(blank=True, null=True)
    recepcao_data_hora = models.DateTimeField(max_length=50, blank=True, null=True)
    recepcao_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True)
    protocolo = models.CharField(max_length=50, blank=True, null=True)
    processamento_versao_aplicativo = models.CharField(max_length=50, blank=True, null=True)
    tempo_estimado_conclusao = models.IntegerField(blank=True, null=True)
    arquivo_header = models.CharField(max_length=200, blank=True, null=True)
    arquivo_request = models.CharField(max_length=200, blank=True, null=True)
    arquivo_response = models.CharField(max_length=200, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    def __unicode__(self):
        return unicode(self.transmissor) + ' - ' + unicode(self.empregador_tpinsc) + ' - ' + unicode(self.empregador_nrinsc) + ' - ' + unicode(self.resposta_codigo) + ' - ' + unicode(self.resposta_descricao)
    #transmissor_lote_esocial_custom#

    class Meta:
        db_table = r'transmissor_lote_esocial'       
        managed = True # transmissor_lote_esocial #
        permissions = (
            ("can_view_transmissor_lote_esocial", "Can view transmissor_lote_esocial"),
            #custom_permissions_transmissor_lote_esocial
        )



class TransmissorLoteEsocialSerializer(ModelSerializer):
    class Meta:
        model = TransmissorLoteEsocial
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

class TransmissorLoteEsocialOcorrencias(SoftDeletionModel):
    transmissor_lote_esocial = models.ForeignKey('TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True)
    resposta_codigo = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(blank=True)
    tipo = models.IntegerField(choices=EVENTOS_OCORRENCIAS_TIPO, blank=True)
    localizacao = models.CharField(max_length=50, blank=True)
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(User,
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(User,
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.NullBooleanField(blank=True, null=True, default=False)
    #transmissor_lote_esocial_ocorrencias_custom#

    class Meta:
        db_table = r'transmissor_lote_esocial_ocorrencias'       
        managed = True # transmissor_lote_esocial_ocorrencias #
        permissions = (
            ("can_view_transmissor_lote_esocial_ocorrencias", "Can view transmissor_lote_esocial_ocorrencias"),
            #custom_permissions_transmissor_lote_esocial_ocorrencias
        )



class TransmissorLoteEsocialOcorrenciasSerializer(ModelSerializer):
    class Meta:
        model = TransmissorLoteEsocialOcorrencias
        exclude = ('criado_em', 'criado_por', 'modificado_em', 'modificado_por', 'excluido')

    def save(self):
        if not self.criado_por:
            self.criado_por = CurrentUserDefault()
            self.criado_em = timezone.now()
        self.modificado_por = CurrentUserDefault()
        self.modificado_em = timezone.now()
            

TPINSC_TRANSMISSOR_EVENTOS = (
    ('1', u'1 - CNPJ'),
    ('2', u'2 - CPF'),
    ('3', u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    ('4', u'4 - CNO (Cadastro Nacional de Obra)'),
)

TIPO_TRANSMISSOR_EVENTOS = (
    ('esocial', u'eSocial'),
    ('efdreinf', u'EFD-Reinf'),
)




class TransmissorEventosEsocial(models.Model):
    from emensageriapro.esocial.models import EVENTO_STATUS
    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'
        
    class Meta:
        db_table = r'transmissor_eventos_esocial'
        managed = False


class TransmissorEventosEfdreinf(models.Model):
    from emensageriapro.esocial.models import EVENTO_STATUS
    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    retornos_evttotal = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:
        db_table = r'transmissor_eventos_efdreinf'
        managed = False
        
        

class TransmissorEventosEsocialTotalizacoes(models.Model):
    from emensageriapro.esocial.models import EVENTO_STATUS
    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote_esocial = models.ForeignKey('mensageiro.TransmissorLoteEsocial',
        related_name='%(class)s_transmissor_lote_esocial', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:
        db_table = r'transmissor_eventos_esocial_totalizacoes'
        managed = False


class TransmissorEventosEfdreinfTotalizacoes(models.Model):
    from emensageriapro.esocial.models import EVENTO_STATUS
    evento = models.CharField(max_length=10)
    identidade = models.CharField(max_length=36)
    transmissor_lote_efdreinf = models.ForeignKey('mensageiro.TransmissorLoteEfdreinf',
        related_name='%(class)s_transmissor_lote_efdreinf', blank=True, null=True)
    grupo = models.IntegerField(choices=EVENTOS_GRUPOS)
    tabela = models.CharField(max_length=50)
    tabela_salvar = models.CharField(max_length=50)
    ordem = models.IntegerField()
    tpinsc = models.CharField(max_length=1, choices=TPINSC_TRANSMISSOR_EVENTOS)
    nrinsc = models.CharField(max_length=15)
    url_recibo = models.CharField(max_length=100, blank=True, null=True)
    validacao_precedencia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    validacoes = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=EVENTO_STATUS, default=0)
    retornos_evttotal = models.ForeignKey('efdreinf.r5001evtTotal',
        related_name='%(class)s_retornos_evttotal', blank=True, null=True)
    retornos_evttotalcontrib = models.ForeignKey('efdreinf.r5011evtTotalContrib',
        related_name='%(class)s_retornos_evttotalcontrib', blank=True, null=True)
    criado_em = models.DateTimeField(blank=True)
    criado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_criado_por', blank=True, null=True)
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey('controle_de_acesso.Usuarios',
        related_name='%(class)s_modificado_por', blank=True, null=True)
    excluido = models.BooleanField(blank=True)

    def tabela_verificar(self):
        return self.tabela + '_verificar'

    def tabela_recibo(self):
        return self.tabela + '_recibo'

    def tabela_duplicar(self):
        return self.tabela + '_duplicar'

    def tabela_xml(self):
        return self.tabela + '_xml'

    class Meta:
        db_table = r'transmissor_eventos_efdreinf_totalizacoes'
        managed = False
