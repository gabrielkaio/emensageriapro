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
from emensageriapro.tabelas.forms import *
from emensageriapro.tabelas.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.models import s2205evtAltCadastral
from emensageriapro.esocial.forms import form_s2205_evtaltcadastral
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.models import s2400evtCdBenefIn
from emensageriapro.esocial.forms import form_s2400_evtcdbenefin
from emensageriapro.s1000.models import s1000inclusaoinfoEnte
from emensageriapro.s1000.forms import form_s1000_inclusao_infoente
from emensageriapro.s1000.models import s1000alteracaoinfoEnte
from emensageriapro.s1000.forms import form_s1000_alteracao_infoente
from emensageriapro.s1070.models import s1070inclusaodadosProcJud
from emensageriapro.s1070.forms import form_s1070_inclusao_dadosprocjud
from emensageriapro.s1070.models import s1070alteracaodadosProcJud
from emensageriapro.s1070.forms import form_s1070_alteracao_dadosprocjud
from emensageriapro.s2200.models import s2200brasil
from emensageriapro.s2200.forms import form_s2200_brasil
from emensageriapro.s2200.models import s2200localTrabDom
from emensageriapro.s2200.forms import form_s2200_localtrabdom
from emensageriapro.s2205.models import s2205brasil
from emensageriapro.s2205.forms import form_s2205_brasil
from emensageriapro.s2206.models import s2206localTrabDom
from emensageriapro.s2206.forms import form_s2206_localtrabdom
from emensageriapro.s2260.models import s2260localTrabInterm
from emensageriapro.s2260.forms import form_s2260_localtrabinterm
from emensageriapro.s2300.models import s2300brasil
from emensageriapro.s2300.forms import form_s2300_brasil
from emensageriapro.s2300.models import s2300infoEstagiario
from emensageriapro.s2300.forms import form_s2300_infoestagiario
from emensageriapro.s2300.models import s2300ageIntegracao
from emensageriapro.s2300.forms import form_s2300_ageintegracao
from emensageriapro.s2306.models import s2306infoEstagiario
from emensageriapro.s2306.forms import form_s2306_infoestagiario
from emensageriapro.s2306.models import s2306ageIntegracao
from emensageriapro.s2306.forms import form_s2306_ageintegracao
from emensageriapro.s2400.models import s2400brasil
from emensageriapro.s2400.forms import form_s2400_brasil
from emensageriapro.s2405.models import s2405brasil
from emensageriapro.s2405.forms import form_s2405_brasil
from emensageriapro.r1070.models import r1070inclusaodadosProcJud
from emensageriapro.r1070.forms import form_r1070_inclusao_dadosprocjud
from emensageriapro.r1070.models import r1070alteracaodadosProcJud
from emensageriapro.r1070.forms import form_r1070_alteracao_dadosprocjud
from emensageriapro.r3010.models import r3010boletim
from emensageriapro.r3010.forms import form_r3010_boletim



@login_required
def salvar(request, hash):

    try: 
        usuario_id = request.user.id 
        dict_hash = get_hash_url( hash )
        municipios_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='municipios')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    if municipios_id:
        municipios = get_object_or_404(Municipios, id = municipios_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if municipios_id:
            municipios_form = form_municipios(request.POST or None, instance = municipios, 
                                         initial = {'excluido': False})
        else:
            municipios_form = form_municipios(request.POST or None,
                                         initial = {'excluido': False})
        if request.method == 'POST':
            if municipios_form.is_valid():
            
                dados = municipios_form.cleaned_data
                obj = municipios_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not municipios_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'municipios', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(municipios), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'municipios', municipios_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('municipios_apagar', 'municipios_salvar', 'municipios'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if municipios_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('municipios_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        municipios_form = disabled_form_fields(municipios_form, permissao.permite_editar)
        
        #municipios_campos_multiple_passo3
        
        if int(dict_hash['print']):
            municipios_form = disabled_form_for_print(municipios_form)
            
        #municipios_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'municipios' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'municipios_salvar'
        context = {
            'municipios': municipios, 
            'municipios_form': municipios_form, 
            'mensagem': mensagem, 
            'municipios_id': int(municipios_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #municipios_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'municipios_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='municipios_salvar.html',
                filename="municipios.pdf",
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
            from django.shortcuts import render_to_response
            response = render_to_response('municipios_salvar.html', context)
            filename = "municipios.xls"
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