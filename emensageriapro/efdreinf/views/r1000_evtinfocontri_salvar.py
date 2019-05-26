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
from emensageriapro.r1000.models import r1000inclusao
from emensageriapro.r1000.forms import form_r1000_inclusao
from emensageriapro.r1000.models import r1000alteracao
from emensageriapro.r1000.forms import form_r1000_alteracao
from emensageriapro.r1000.models import r1000exclusao
from emensageriapro.r1000.forms import form_r1000_exclusao


@login_required
def salvar(request, hash):
    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r1000_evtinfocontri_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='r1000_evtinfocontri')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    
    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri, id = r1000_evtinfocontri_id)
        
        if r1000_evtinfocontri.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['r1000_evtinfocontri_apagar'] = 0
            dict_permissoes['r1000_evtinfocontri_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r1000_evtinfocontri_id:
            r1000_evtinfocontri_form = form_r1000_evtinfocontri(request.POST or None, instance = r1000_evtinfocontri, 
                                         initial={'excluido': False})
        else:
            r1000_evtinfocontri_form = form_r1000_evtinfocontri(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
        if request.method == 'POST':
            if r1000_evtinfocontri_form.is_valid():
            
                dados = r1000_evtinfocontri_form.cleaned_data
                obj = r1000_evtinfocontri_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r1000_evtinfocontri_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r1000_evtinfocontri', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r1000_evtinfocontri), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r1000_evtinfocontri', r1000_evtinfocontri_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('r1000_evtinfocontri_apagar', 'r1000_evtinfocontri_salvar', 'r1000_evtinfocontri'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r1000_evtinfocontri_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r1000_evtinfocontri_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
        r1000_evtinfocontri_form = disabled_form_fields(r1000_evtinfocontri_form, permissao.permite_editar)
        
        if r1000_evtinfocontri_id:
            if r1000_evtinfocontri.status != 0:
                r1000_evtinfocontri_form = disabled_form_fields(r1000_evtinfocontri_form, False)
        #r1000_evtinfocontri_campos_multiple_passo3

        for field in r1000_evtinfocontri_form.fields.keys():
            r1000_evtinfocontri_form.fields[field].widget.attrs['ng-model'] = 'r1000_evtinfocontri_'+field
        if int(dict_hash['print']):
            r1000_evtinfocontri_form = disabled_form_for_print(r1000_evtinfocontri_form)

        
        r1000_inclusao_lista = None 
        r1000_inclusao_form = None 
        r1000_alteracao_lista = None 
        r1000_alteracao_form = None 
        r1000_exclusao_lista = None 
        r1000_exclusao_form = None 
        
        if r1000_evtinfocontri_id:
            r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri, id = r1000_evtinfocontri_id)
            
            r1000_inclusao_form = form_r1000_inclusao(
                initial={ 'r1000_evtinfocontri': r1000_evtinfocontri })
            r1000_inclusao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_inclusao_lista = r1000inclusao.objects.\
                filter(r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
            r1000_alteracao_form = form_r1000_alteracao(
                initial={ 'r1000_evtinfocontri': r1000_evtinfocontri })
            r1000_alteracao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_alteracao_lista = r1000alteracao.objects.\
                filter(r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
            r1000_exclusao_form = form_r1000_exclusao(
                initial={ 'r1000_evtinfocontri': r1000_evtinfocontri })
            r1000_exclusao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_exclusao_lista = r1000exclusao.objects.\
                filter(r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
                
        else:
            r1000_evtinfocontri = None
        #r1000_evtinfocontri_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 'r1000_evtinfocontri'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 'r1000_evtinfocontri' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r1000_evtinfocontri_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=r1000_evtinfocontri_id, tabela='r1000_evtinfocontri').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r1000_evtinfocontri': r1000_evtinfocontri, 
            'r1000_evtinfocontri_form': r1000_evtinfocontri_form, 
            'mensagem': mensagem, 
            'r1000_evtinfocontri_id': int(r1000_evtinfocontri_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            'r1000_inclusao_form': r1000_inclusao_form,
            'r1000_inclusao_lista': r1000_inclusao_lista,
            'r1000_alteracao_form': r1000_alteracao_form,
            'r1000_alteracao_lista': r1000_alteracao_lista,
            'r1000_exclusao_form': r1000_exclusao_form,
            'r1000_exclusao_lista': r1000_exclusao_lista,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r1000_evtinfocontri_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
            return render(request, 'r1000_evtinfocontri_salvar.html', context)
            
        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='r1000_evtinfocontri_salvar.html',
                filename="r1000_evtinfocontri.pdf",
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
            response = render_to_response('r1000_evtinfocontri_salvar.html', context)
            filename = "r1000_evtinfocontri.xls"
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
