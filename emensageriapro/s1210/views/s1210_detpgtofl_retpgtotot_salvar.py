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
from emensageriapro.s1210.forms import *
from emensageriapro.s1210.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s1210.models import s1210detPgtoFlpenAlim
from emensageriapro.s1210.forms import form_s1210_detpgtofl_penalim



@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try: 
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        s1210_detpgtofl_retpgtotot_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='s1210_detpgtofl_retpgtotot')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s1210_detpgtofl_retpgtotot_id:
        s1210_detpgtofl_retpgtotot = get_object_or_404(s1210detPgtoFlretPgtoTot, id = s1210_detpgtofl_retpgtotot_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    if s1210_detpgtofl_retpgtotot_id:
        dados_evento = s1210_detpgtofl_retpgtotot.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s1210_detpgtofl_retpgtotot_apagar'] = 0
            dict_permissoes['s1210_detpgtofl_retpgtotot_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s1210_detpgtofl_retpgtotot_id:
            s1210_detpgtofl_retpgtotot_form = form_s1210_detpgtofl_retpgtotot(request.POST or None, instance = s1210_detpgtofl_retpgtotot,  
                                         initial={'excluido': False})
        else:
            s1210_detpgtofl_retpgtotot_form = form_s1210_detpgtofl_retpgtotot(request.POST or None, 
                                         initial={'excluido': False})
        if request.method == 'POST':
            if s1210_detpgtofl_retpgtotot_form.is_valid():
            
                dados = s1210_detpgtofl_retpgtotot_form.cleaned_data
                obj = s1210_detpgtofl_retpgtotot_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s1210_detpgtofl_retpgtotot_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's1210_detpgtofl_retpgtotot', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s1210_detpgtofl_retpgtotot), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's1210_detpgtofl_retpgtotot', s1210_detpgtofl_retpgtotot_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('s1210_detpgtofl_retpgtotot_apagar', 's1210_detpgtofl_retpgtotot_salvar', 's1210_detpgtofl_retpgtotot'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s1210_detpgtofl_retpgtotot_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s1210_detpgtofl_retpgtotot_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        s1210_detpgtofl_retpgtotot_form = disabled_form_fields(s1210_detpgtofl_retpgtotot_form, permissao.permite_editar)
        
        if s1210_detpgtofl_retpgtotot_id:
            if dados_evento['status'] != 0:
                s1210_detpgtofl_retpgtotot_form = disabled_form_fields(s1210_detpgtofl_retpgtotot_form, 0)
                
        #s1210_detpgtofl_retpgtotot_campos_multiple_passo3
        
        if int(dict_hash['print']):
            s1210_detpgtofl_retpgtotot_form = disabled_form_for_print(s1210_detpgtofl_retpgtotot_form)
            
        
        s1210_detpgtofl_penalim_lista = None 
        s1210_detpgtofl_penalim_form = None 
        
        if s1210_detpgtofl_retpgtotot_id:
            s1210_detpgtofl_retpgtotot = get_object_or_404(s1210detPgtoFlretPgtoTot, id = s1210_detpgtofl_retpgtotot_id)
            
            s1210_detpgtofl_penalim_form = form_s1210_detpgtofl_penalim(
                initial={ 's1210_detpgtofl_retpgtotot': s1210_detpgtofl_retpgtotot })
            s1210_detpgtofl_penalim_form.fields['s1210_detpgtofl_retpgtotot'].widget.attrs['readonly'] = True
            s1210_detpgtofl_penalim_lista = s1210detPgtoFlpenAlim.objects.\
                filter(s1210_detpgtofl_retpgtotot_id=s1210_detpgtofl_retpgtotot.id).all()
                
        else:
            s1210_detpgtofl_retpgtotot = None
            
        #s1210_detpgtofl_retpgtotot_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's1210_detpgtofl_retpgtotot' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's1210_detpgtofl_retpgtotot_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=s1210_detpgtofl_retpgtotot_id, tabela='s1210_detpgtofl_retpgtotot').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's1210_detpgtofl_retpgtotot': s1210_detpgtofl_retpgtotot, 
            's1210_detpgtofl_retpgtotot_form': s1210_detpgtofl_retpgtotot_form, 
            'mensagem': mensagem, 
            's1210_detpgtofl_retpgtotot_id': int(s1210_detpgtofl_retpgtotot_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            's1210_detpgtofl_penalim_form': s1210_detpgtofl_penalim_form,
            's1210_detpgtofl_penalim_lista': s1210_detpgtofl_penalim_lista,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s1210_detpgtofl_retpgtotot_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's1210_detpgtofl_retpgtotot_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s1210_detpgtofl_retpgtotot_salvar.html',
                filename="s1210_detpgtofl_retpgtotot.pdf",
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
            response = render_to_response('s1210_detpgtofl_retpgtotot_salvar.html', context)
            filename = "s1210_detpgtofl_retpgtotot.xls"
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