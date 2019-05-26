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
from emensageriapro.r2030.models import r2030recursosRec
from emensageriapro.r2030.forms import form_r2030_recursosrec


@login_required
def salvar(request, hash):
    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r2030_evtassocdesprec_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='r2030_evtassocdesprec')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    
    if r2030_evtassocdesprec_id:
        r2030_evtassocdesprec = get_object_or_404(r2030evtAssocDespRec, id = r2030_evtassocdesprec_id)
        
        if r2030_evtassocdesprec.status != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['r2030_evtassocdesprec_apagar'] = 0
            dict_permissoes['r2030_evtassocdesprec_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r2030_evtassocdesprec_id:
            r2030_evtassocdesprec_form = form_r2030_evtassocdesprec(request.POST or None, instance = r2030_evtassocdesprec, 
                                         initial={'excluido': False})
        else:
            r2030_evtassocdesprec_form = form_r2030_evtassocdesprec(request.POST or None, 
                                         initial={'versao': VERSAO_LAYOUT_EFDREINF, 
                                                  'status': STATUS_EVENTO_CADASTRADO, 
                                                  'tpamb': TP_AMB, 
                                                  'procemi': 1, 
                                                  'verproc': VERSAO_EMENSAGERIA, 
                                                  'excluido': False})
        if request.method == 'POST':
            if r2030_evtassocdesprec_form.is_valid():
            
                dados = r2030_evtassocdesprec_form.cleaned_data
                obj = r2030_evtassocdesprec_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r2030_evtassocdesprec_id:
                    from emensageriapro.functions import identidade_evento
                    identidade_evento(obj)
                  
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r2030_evtassocdesprec', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r2030_evtassocdesprec), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r2030_evtassocdesprec', r2030_evtassocdesprec_id, usuario_id, 2)
                                 
                if request.session['retorno_pagina'] not in ('r2030_evtassocdesprec_apagar', 'r2030_evtassocdesprec_salvar', 'r2030_evtassocdesprec'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r2030_evtassocdesprec_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r2030_evtassocdesprec_salvar', hash=url_hash)

            else:
                messages.error(request, u'Erro ao salvar!')
        r2030_evtassocdesprec_form = disabled_form_fields(r2030_evtassocdesprec_form, permissao.permite_editar)
        
        if r2030_evtassocdesprec_id:
            if r2030_evtassocdesprec.status != 0:
                r2030_evtassocdesprec_form = disabled_form_fields(r2030_evtassocdesprec_form, False)
        #r2030_evtassocdesprec_campos_multiple_passo3

        for field in r2030_evtassocdesprec_form.fields.keys():
            r2030_evtassocdesprec_form.fields[field].widget.attrs['ng-model'] = 'r2030_evtassocdesprec_'+field
        if int(dict_hash['print']):
            r2030_evtassocdesprec_form = disabled_form_for_print(r2030_evtassocdesprec_form)

        
        r2030_recursosrec_lista = None 
        r2030_recursosrec_form = None 
        
        if r2030_evtassocdesprec_id:
            r2030_evtassocdesprec = get_object_or_404(r2030evtAssocDespRec, id = r2030_evtassocdesprec_id)
            
            r2030_recursosrec_form = form_r2030_recursosrec(
                initial={ 'r2030_evtassocdesprec': r2030_evtassocdesprec })
            r2030_recursosrec_form.fields['r2030_evtassocdesprec'].widget.attrs['readonly'] = True
            r2030_recursosrec_lista = r2030recursosRec.objects.\
                filter(r2030_evtassocdesprec_id=r2030_evtassocdesprec.id).all()
                
        else:
            r2030_evtassocdesprec = None
        #r2030_evtassocdesprec_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if 'r2030_evtassocdesprec'[1] == '5':
            evento_totalizador = True
        else:
            evento_totalizador = False
        
        if dict_hash['tab'] or 'r2030_evtassocdesprec' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r2030_evtassocdesprec_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=r2030_evtassocdesprec_id, tabela='r2030_evtassocdesprec').all()
        context = {
            'evento_totalizador': evento_totalizador,
            'controle_alteracoes': controle_alteracoes,
            'r2030_evtassocdesprec': r2030_evtassocdesprec, 
            'r2030_evtassocdesprec_form': r2030_evtassocdesprec_form, 
            'mensagem': mensagem, 
            'r2030_evtassocdesprec_id': int(r2030_evtassocdesprec_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            'r2030_recursosrec_form': r2030_recursosrec_form,
            'r2030_recursosrec_lista': r2030_recursosrec_lista,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r2030_evtassocdesprec_salvar_custom_variaveis_context#
        }
        
        if for_print in (0, 1):
            return render(request, 'r2030_evtassocdesprec_salvar.html', context)
            
        elif for_print == 2:
            response = PDFTemplateResponse(
                request=request,
                template='r2030_evtassocdesprec_salvar.html',
                filename="r2030_evtassocdesprec.pdf",
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
            response = render_to_response('r2030_evtassocdesprec_salvar.html', context)
            filename = "r2030_evtassocdesprec.xls"
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
