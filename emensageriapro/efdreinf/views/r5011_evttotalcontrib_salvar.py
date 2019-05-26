#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"


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


import datetime
import json
import base64
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.efdreinf.models import r1000evtInfoContri
from emensageriapro.efdreinf.forms import form_r1000_evtinfocontri
from emensageriapro.efdreinf.models import r1070evtTabProcesso
from emensageriapro.efdreinf.forms import form_r1070_evttabprocesso
from emensageriapro.efdreinf.models import r2010evtServTom
from emensageriapro.efdreinf.forms import form_r2010_evtservtom
from emensageriapro.efdreinf.models import r2020evtServPrest
from emensageriapro.efdreinf.forms import form_r2020_evtservprest
from emensageriapro.efdreinf.models import r2030evtAssocDespRec
from emensageriapro.efdreinf.forms import form_r2030_evtassocdesprec
from emensageriapro.efdreinf.models import r2040evtAssocDespRep
from emensageriapro.efdreinf.forms import form_r2040_evtassocdesprep
from emensageriapro.efdreinf.models import r2050evtComProd
from emensageriapro.efdreinf.forms import form_r2050_evtcomprod
from emensageriapro.efdreinf.models import r2060evtCPRB
from emensageriapro.efdreinf.forms import form_r2060_evtcprb
from emensageriapro.efdreinf.models import r2070evtPgtosDivs
from emensageriapro.efdreinf.forms import form_r2070_evtpgtosdivs
from emensageriapro.efdreinf.models import r2098evtReabreEvPer
from emensageriapro.efdreinf.forms import form_r2098_evtreabreevper
from emensageriapro.efdreinf.models import r2099evtFechaEvPer
from emensageriapro.efdreinf.forms import form_r2099_evtfechaevper
from emensageriapro.efdreinf.models import r3010evtEspDesportivo
from emensageriapro.efdreinf.forms import form_r3010_evtespdesportivo
from emensageriapro.efdreinf.models import r4010evtRetPF
from emensageriapro.efdreinf.forms import form_r4010_evtretpf
from emensageriapro.efdreinf.models import r4020evtRetPJ
from emensageriapro.efdreinf.forms import form_r4020_evtretpj
from emensageriapro.efdreinf.models import r4040evtBenefNId
from emensageriapro.efdreinf.forms import form_r4040_evtbenefnid
from emensageriapro.efdreinf.models import r4098evtReab
from emensageriapro.efdreinf.forms import form_r4098_evtreab
from emensageriapro.efdreinf.models import r4099evtFech
from emensageriapro.efdreinf.forms import form_r4099_evtfech
from emensageriapro.efdreinf.models import r5001evtTotal
from emensageriapro.efdreinf.forms import form_r5001_evttotal
from emensageriapro.efdreinf.models import r5011evtTotalContrib
from emensageriapro.efdreinf.forms import form_r5011_evttotalcontrib
from emensageriapro.efdreinf.models import r9000evtExclusao
from emensageriapro.efdreinf.forms import form_r9000_evtexclusao
from emensageriapro.efdreinf.models import r9001evtTotal
from emensageriapro.efdreinf.forms import form_r9001_evttotal
from emensageriapro.efdreinf.models import r9002evtRet
from emensageriapro.efdreinf.forms import form_r9002_evtret
from emensageriapro.efdreinf.models import r9011evtTotalContrib
from emensageriapro.efdreinf.forms import form_r9011_evttotalcontrib
from emensageriapro.efdreinf.models import r9012evtRetCons
from emensageriapro.efdreinf.forms import form_r9012_evtretcons
from emensageriapro.r5011.models import r5011regOcorrs
from emensageriapro.r5011.forms import form_r5011_regocorrs
from emensageriapro.r5011.models import r5011infoTotalContrib
from emensageriapro.r5011.forms import form_r5011_infototalcontrib


@login_required
def salvar(request, hash):
    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r5011_evttotalcontrib_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='r5011_evttotalcontrib')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    
    if r5011_evttotalcontrib_id:
        r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib, id = r5011_evttotalcontrib_id)
        
        if r5011_evttotalcontrib.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['r5011_evttotalcontrib_apagar'] = 0
            dict_permissoes['r5011_evttotalcontrib_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r5011_evttotalcontrib_id:
            r5011_evttotalcontrib_form = form_r5011_evttotalcontrib(request.POST or None, instance = r5011_evttotalcontrib, 
                                         initial={'excluido': False})
        else:
            r5011_evttotalcontrib_form = form_r5011_evttotalcontrib(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
        if request.method == 'POST':
            if r5011_evttotalcontrib_form.is_valid():
            
                dados = r5011_evttotalcontrib_form.cleaned_data
                obj = r5011_evttotalcontrib_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r5011_evttotalcontrib_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r5011_evttotalcontrib', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r5011_evttotalcontrib), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r5011_evttotalcontrib', r5011_evttotalcontrib_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('r5011_evttotalcontrib_apagar', 'r5011_evttotalcontrib_salvar', 'r5011_evttotalcontrib'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r5011_evttotalcontrib_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r5011_evttotalcontrib_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
        r5011_evttotalcontrib_form = disabled_form_fields(r5011_evttotalcontrib_form, permissao.permite_editar)
        
        if r5011_evttotalcontrib_id:
            if r5011_evttotalcontrib.status != 0:
                r5011_evttotalcontrib_form = disabled_form_fields(r5011_evttotalcontrib_form, False)
        #r5011_evttotalcontrib_campos_multiple_passo3

        for field in r5011_evttotalcontrib_form.fields.keys():
            r5011_evttotalcontrib_form.fields[field].widget.attrs['ng-model'] = 'r5011_evttotalcontrib_'+field
        if int(dict_hash['print']):
            r5011_evttotalcontrib_form = disabled_form_for_print(r5011_evttotalcontrib_form)

        
        r1000_evtinfocontri_lista = None 
        r1000_evtinfocontri_form = None 
        r1070_evttabprocesso_lista = None 
        r1070_evttabprocesso_form = None 
        r2010_evtservtom_lista = None 
        r2010_evtservtom_form = None 
        r2020_evtservprest_lista = None 
        r2020_evtservprest_form = None 
        r2030_evtassocdesprec_lista = None 
        r2030_evtassocdesprec_form = None 
        r2040_evtassocdesprep_lista = None 
        r2040_evtassocdesprep_form = None 
        r2050_evtcomprod_lista = None 
        r2050_evtcomprod_form = None 
        r2060_evtcprb_lista = None 
        r2060_evtcprb_form = None 
        r2070_evtpgtosdivs_lista = None 
        r2070_evtpgtosdivs_form = None 
        r2098_evtreabreevper_lista = None 
        r2098_evtreabreevper_form = None 
        r2099_evtfechaevper_lista = None 
        r2099_evtfechaevper_form = None 
        r3010_evtespdesportivo_lista = None 
        r3010_evtespdesportivo_form = None 
        r4010_evtretpf_lista = None 
        r4010_evtretpf_form = None 
        r4020_evtretpj_lista = None 
        r4020_evtretpj_form = None 
        r4040_evtbenefnid_lista = None 
        r4040_evtbenefnid_form = None 
        r4098_evtreab_lista = None 
        r4098_evtreab_form = None 
        r4099_evtfech_lista = None 
        r4099_evtfech_form = None 
        r5001_evttotal_lista = None 
        r5001_evttotal_form = None 
        r5011_evttotalcontrib_lista = None 
        r5011_evttotalcontrib_form = None 
        r9000_evtexclusao_lista = None 
        r9000_evtexclusao_form = None 
        r9001_evttotal_lista = None 
        r9001_evttotal_form = None 
        r9002_evtret_lista = None 
        r9002_evtret_form = None 
        r9011_evttotalcontrib_lista = None 
        r9011_evttotalcontrib_form = None 
        r9012_evtretcons_lista = None 
        r9012_evtretcons_form = None 
        r5011_regocorrs_lista = None 
        r5011_regocorrs_form = None 
        r5011_infototalcontrib_lista = None 
        r5011_infototalcontrib_form = None 
        
        if r5011_evttotalcontrib_id:
            r5011_evttotalcontrib = get_object_or_404(r5011evtTotalContrib, id = r5011_evttotalcontrib_id)
            
            r5011_regocorrs_form = form_r5011_regocorrs(
                initial={ 'r5011_evttotalcontrib': r5011_evttotalcontrib })
            r5011_regocorrs_form.fields['r5011_evttotalcontrib'].widget.attrs['readonly'] = True
            r5011_regocorrs_lista = r5011regOcorrs.objects.\
                filter(r5011_evttotalcontrib_id=r5011_evttotalcontrib.id).all()
            r5011_infototalcontrib_form = form_r5011_infototalcontrib(
                initial={ 'r5011_evttotalcontrib': r5011_evttotalcontrib })
            r5011_infototalcontrib_form.fields['r5011_evttotalcontrib'].widget.attrs['readonly'] = True
            r5011_infototalcontrib_lista = r5011infoTotalContrib.objects.\
                filter(r5011_evttotalcontrib_id=r5011_evttotalcontrib.id).all()
            r1000_evtinfocontri_form = form_r1000_evtinfocontri(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r1000_evtinfocontri_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r1000_evtinfocontri_lista = r1000evtInfoContri.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r1070_evttabprocesso_form = form_r1070_evttabprocesso(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r1070_evttabprocesso_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r1070_evttabprocesso_lista = r1070evtTabProcesso.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2010_evtservtom_form = form_r2010_evtservtom(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2010_evtservtom_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2010_evtservtom_lista = r2010evtServTom.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2020_evtservprest_form = form_r2020_evtservprest(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2020_evtservprest_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2020_evtservprest_lista = r2020evtServPrest.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2030_evtassocdesprec_form = form_r2030_evtassocdesprec(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2030_evtassocdesprec_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2030_evtassocdesprec_lista = r2030evtAssocDespRec.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2040_evtassocdesprep_form = form_r2040_evtassocdesprep(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2040_evtassocdesprep_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2040_evtassocdesprep_lista = r2040evtAssocDespRep.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2050_evtcomprod_form = form_r2050_evtcomprod(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2050_evtcomprod_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2050_evtcomprod_lista = r2050evtComProd.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2060_evtcprb_form = form_r2060_evtcprb(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2060_evtcprb_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2060_evtcprb_lista = r2060evtCPRB.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2070_evtpgtosdivs_form = form_r2070_evtpgtosdivs(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2070_evtpgtosdivs_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2070_evtpgtosdivs_lista = r2070evtPgtosDivs.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2098_evtreabreevper_form = form_r2098_evtreabreevper(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2098_evtreabreevper_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2098_evtreabreevper_lista = r2098evtReabreEvPer.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r2099_evtfechaevper_form = form_r2099_evtfechaevper(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r2099_evtfechaevper_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r2099_evtfechaevper_lista = r2099evtFechaEvPer.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r3010_evtespdesportivo_form = form_r3010_evtespdesportivo(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r3010_evtespdesportivo_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r3010_evtespdesportivo_lista = r3010evtEspDesportivo.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r4010_evtretpf_form = form_r4010_evtretpf(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r4010_evtretpf_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r4010_evtretpf_lista = r4010evtRetPF.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r4020_evtretpj_form = form_r4020_evtretpj(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r4020_evtretpj_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r4020_evtretpj_lista = r4020evtRetPJ.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r4040_evtbenefnid_form = form_r4040_evtbenefnid(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r4040_evtbenefnid_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r4040_evtbenefnid_lista = r4040evtBenefNId.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r4098_evtreab_form = form_r4098_evtreab(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r4098_evtreab_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r4098_evtreab_lista = r4098evtReab.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r4099_evtfech_form = form_r4099_evtfech(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r4099_evtfech_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r4099_evtfech_lista = r4099evtFech.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r5001_evttotal_form = form_r5001_evttotal(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r5001_evttotal_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r5001_evttotal_lista = r5001evtTotal.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r5011_evttotalcontrib_form = form_r5011_evttotalcontrib(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r5011_evttotalcontrib_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r5011_evttotalcontrib_lista = r5011evtTotalContrib.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r9000_evtexclusao_form = form_r9000_evtexclusao(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r9000_evtexclusao_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r9000_evtexclusao_lista = r9000evtExclusao.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r9001_evttotal_form = form_r9001_evttotal(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r9001_evttotal_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r9001_evttotal_lista = r9001evtTotal.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r9002_evtret_form = form_r9002_evtret(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r9002_evtret_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r9002_evtret_lista = r9002evtRet.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r9011_evttotalcontrib_form = form_r9011_evttotalcontrib(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r9011_evttotalcontrib_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r9011_evttotalcontrib_lista = r9011evtTotalContrib.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
            r9012_evtretcons_form = form_r9012_evtretcons(
                initial={ 'retornos_r5011': r5011_evttotalcontrib })
            r9012_evtretcons_form.fields['retornos_r5011'].widget.attrs['readonly'] = True
            r9012_evtretcons_lista = r9012evtRetCons.objects.\
                filter(retornos_r5011_id=r5011_evttotalcontrib.id).all()
                
        else:
            r5011_evttotalcontrib = None
        #r5011_evttotalcontrib_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 'r5011_evttotalcontrib'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 'r5011_evttotalcontrib' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r5011_evttotalcontrib_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=r5011_evttotalcontrib_id, tabela='r5011_evttotalcontrib').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r5011_evttotalcontrib': r5011_evttotalcontrib, 
            'r5011_evttotalcontrib_form': r5011_evttotalcontrib_form, 
            'mensagem': mensagem, 
            'r5011_evttotalcontrib_id': int(r5011_evttotalcontrib_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            'r1000_evtinfocontri_form': r1000_evtinfocontri_form,
            'r1000_evtinfocontri_lista': r1000_evtinfocontri_lista,
            'r1070_evttabprocesso_form': r1070_evttabprocesso_form,
            'r1070_evttabprocesso_lista': r1070_evttabprocesso_lista,
            'r2010_evtservtom_form': r2010_evtservtom_form,
            'r2010_evtservtom_lista': r2010_evtservtom_lista,
            'r2020_evtservprest_form': r2020_evtservprest_form,
            'r2020_evtservprest_lista': r2020_evtservprest_lista,
            'r2030_evtassocdesprec_form': r2030_evtassocdesprec_form,
            'r2030_evtassocdesprec_lista': r2030_evtassocdesprec_lista,
            'r2040_evtassocdesprep_form': r2040_evtassocdesprep_form,
            'r2040_evtassocdesprep_lista': r2040_evtassocdesprep_lista,
            'r2050_evtcomprod_form': r2050_evtcomprod_form,
            'r2050_evtcomprod_lista': r2050_evtcomprod_lista,
            'r2060_evtcprb_form': r2060_evtcprb_form,
            'r2060_evtcprb_lista': r2060_evtcprb_lista,
            'r2070_evtpgtosdivs_form': r2070_evtpgtosdivs_form,
            'r2070_evtpgtosdivs_lista': r2070_evtpgtosdivs_lista,
            'r2098_evtreabreevper_form': r2098_evtreabreevper_form,
            'r2098_evtreabreevper_lista': r2098_evtreabreevper_lista,
            'r2099_evtfechaevper_form': r2099_evtfechaevper_form,
            'r2099_evtfechaevper_lista': r2099_evtfechaevper_lista,
            'r3010_evtespdesportivo_form': r3010_evtespdesportivo_form,
            'r3010_evtespdesportivo_lista': r3010_evtespdesportivo_lista,
            'r4010_evtretpf_form': r4010_evtretpf_form,
            'r4010_evtretpf_lista': r4010_evtretpf_lista,
            'r4020_evtretpj_form': r4020_evtretpj_form,
            'r4020_evtretpj_lista': r4020_evtretpj_lista,
            'r4040_evtbenefnid_form': r4040_evtbenefnid_form,
            'r4040_evtbenefnid_lista': r4040_evtbenefnid_lista,
            'r4098_evtreab_form': r4098_evtreab_form,
            'r4098_evtreab_lista': r4098_evtreab_lista,
            'r4099_evtfech_form': r4099_evtfech_form,
            'r4099_evtfech_lista': r4099_evtfech_lista,
            'r5001_evttotal_form': r5001_evttotal_form,
            'r5001_evttotal_lista': r5001_evttotal_lista,
            'r5011_evttotalcontrib_form': r5011_evttotalcontrib_form,
            'r5011_evttotalcontrib_lista': r5011_evttotalcontrib_lista,
            'r9000_evtexclusao_form': r9000_evtexclusao_form,
            'r9000_evtexclusao_lista': r9000_evtexclusao_lista,
            'r9001_evttotal_form': r9001_evttotal_form,
            'r9001_evttotal_lista': r9001_evttotal_lista,
            'r9002_evtret_form': r9002_evtret_form,
            'r9002_evtret_lista': r9002_evtret_lista,
            'r9011_evttotalcontrib_form': r9011_evttotalcontrib_form,
            'r9011_evttotalcontrib_lista': r9011_evttotalcontrib_lista,
            'r9012_evtretcons_form': r9012_evtretcons_form,
            'r9012_evtretcons_lista': r9012_evtretcons_lista,
            'r5011_regocorrs_form': r5011_regocorrs_form,
            'r5011_regocorrs_lista': r5011_regocorrs_lista,
            'r5011_infototalcontrib_form': r5011_infototalcontrib_form,
            'r5011_infototalcontrib_lista': r5011_infototalcontrib_lista,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r5011_evttotalcontrib_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
            return render(request, 'r5011_evttotalcontrib_salvar.html', context)
            
        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='r5011_evttotalcontrib_salvar.html',
                filename="r5011_evttotalcontrib.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
            
        elif for_print == 3:
            response = render_to_response('r5011_evttotalcontrib_salvar.html', context)
            filename = "r5011_evttotalcontrib.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
    else:
        context = {
            'usuario': usuario, 
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)