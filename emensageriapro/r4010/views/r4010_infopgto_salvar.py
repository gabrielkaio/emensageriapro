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
from emensageriapro.r4010.forms import *
from emensageriapro.r4010.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.r4010.models import r4010FCI
from emensageriapro.r4010.forms import form_r4010_fci
from emensageriapro.r4010.models import r4010SCP
from emensageriapro.r4010.forms import form_r4010_scp
from emensageriapro.r4010.models import r4010detDed
from emensageriapro.r4010.forms import form_r4010_detded
from emensageriapro.r4010.models import r4010rendIsento
from emensageriapro.r4010.forms import form_r4010_rendisento
from emensageriapro.r4010.models import r4010infoProcRet
from emensageriapro.r4010.forms import form_r4010_infoprocret
from emensageriapro.r4010.models import r4010infoRRA
from emensageriapro.r4010.forms import form_r4010_inforra
from emensageriapro.r4010.models import r4010infoProcJud
from emensageriapro.r4010.forms import form_r4010_infoprocjud



@login_required
def salvar(request, hash):
    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    
    try: 
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        r4010_infopgto_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='r4010_infopgto')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r4010_infopgto_id:
        r4010_infopgto = get_object_or_404(r4010infoPgto, id = r4010_infopgto_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    if r4010_infopgto_id:
        dados_evento = r4010_infopgto.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['r4010_infopgto_apagar'] = 0
            dict_permissoes['r4010_infopgto_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r4010_infopgto_id:
            r4010_infopgto_form = form_r4010_infopgto(request.POST or None, instance = r4010_infopgto,  
                                         initial={'excluido': False})
        else:
            r4010_infopgto_form = form_r4010_infopgto(request.POST or None, 
                                         initial={'excluido': False})
        if request.method == 'POST':
            if r4010_infopgto_form.is_valid():
            
                dados = r4010_infopgto_form.cleaned_data
                obj = r4010_infopgto_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not r4010_infopgto_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'r4010_infopgto', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(r4010_infopgto), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'r4010_infopgto', r4010_infopgto_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('r4010_infopgto_apagar', 'r4010_infopgto_salvar', 'r4010_infopgto'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if r4010_infopgto_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('r4010_infopgto_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        r4010_infopgto_form = disabled_form_fields(r4010_infopgto_form, permissao.permite_editar)
        
        if r4010_infopgto_id:
            if dados_evento['status'] != 0:
                r4010_infopgto_form = disabled_form_fields(r4010_infopgto_form, 0)
                
        #r4010_infopgto_campos_multiple_passo3
        
        if int(dict_hash['print']):
            r4010_infopgto_form = disabled_form_for_print(r4010_infopgto_form)
            
        
        r4010_fci_lista = None 
        r4010_fci_form = None 
        r4010_scp_lista = None 
        r4010_scp_form = None 
        r4010_detded_lista = None 
        r4010_detded_form = None 
        r4010_rendisento_lista = None 
        r4010_rendisento_form = None 
        r4010_infoprocret_lista = None 
        r4010_infoprocret_form = None 
        r4010_inforra_lista = None 
        r4010_inforra_form = None 
        r4010_infoprocjud_lista = None 
        r4010_infoprocjud_form = None 
        
        if r4010_infopgto_id:
            r4010_infopgto = get_object_or_404(r4010infoPgto, id = r4010_infopgto_id)
            
            r4010_fci_form = form_r4010_fci(
                initial={ 'r4010_infopgto': r4010_infopgto })
            r4010_fci_form.fields['r4010_infopgto'].widget.attrs['readonly'] = True
            r4010_fci_lista = r4010FCI.objects.\
                filter(r4010_infopgto_id=r4010_infopgto.id).all()
            r4010_scp_form = form_r4010_scp(
                initial={ 'r4010_infopgto': r4010_infopgto })
            r4010_scp_form.fields['r4010_infopgto'].widget.attrs['readonly'] = True
            r4010_scp_lista = r4010SCP.objects.\
                filter(r4010_infopgto_id=r4010_infopgto.id).all()
            r4010_detded_form = form_r4010_detded(
                initial={ 'r4010_infopgto': r4010_infopgto })
            r4010_detded_form.fields['r4010_infopgto'].widget.attrs['readonly'] = True
            r4010_detded_lista = r4010detDed.objects.\
                filter(r4010_infopgto_id=r4010_infopgto.id).all()
            r4010_rendisento_form = form_r4010_rendisento(
                initial={ 'r4010_infopgto': r4010_infopgto })
            r4010_rendisento_form.fields['r4010_infopgto'].widget.attrs['readonly'] = True
            r4010_rendisento_lista = r4010rendIsento.objects.\
                filter(r4010_infopgto_id=r4010_infopgto.id).all()
            r4010_infoprocret_form = form_r4010_infoprocret(
                initial={ 'r4010_infopgto': r4010_infopgto })
            r4010_infoprocret_form.fields['r4010_infopgto'].widget.attrs['readonly'] = True
            r4010_infoprocret_lista = r4010infoProcRet.objects.\
                filter(r4010_infopgto_id=r4010_infopgto.id).all()
            r4010_inforra_form = form_r4010_inforra(
                initial={ 'r4010_infopgto': r4010_infopgto })
            r4010_inforra_form.fields['r4010_infopgto'].widget.attrs['readonly'] = True
            r4010_inforra_lista = r4010infoRRA.objects.\
                filter(r4010_infopgto_id=r4010_infopgto.id).all()
            r4010_infoprocjud_form = form_r4010_infoprocjud(
                initial={ 'r4010_infopgto': r4010_infopgto })
            r4010_infoprocjud_form.fields['r4010_infopgto'].widget.attrs['readonly'] = True
            r4010_infoprocjud_lista = r4010infoProcJud.objects.\
                filter(r4010_infopgto_id=r4010_infopgto.id).all()
                
        else:
            r4010_infopgto = None
            
        #r4010_infopgto_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'r4010_infopgto' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r4010_infopgto_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=r4010_infopgto_id, tabela='r4010_infopgto').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            'r4010_infopgto': r4010_infopgto, 
            'r4010_infopgto_form': r4010_infopgto_form, 
            'mensagem': mensagem, 
            'r4010_infopgto_id': int(r4010_infopgto_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            'r4010_fci_form': r4010_fci_form,
            'r4010_fci_lista': r4010_fci_lista,
            'r4010_scp_form': r4010_scp_form,
            'r4010_scp_lista': r4010_scp_lista,
            'r4010_detded_form': r4010_detded_form,
            'r4010_detded_lista': r4010_detded_lista,
            'r4010_rendisento_form': r4010_rendisento_form,
            'r4010_rendisento_lista': r4010_rendisento_lista,
            'r4010_infoprocret_form': r4010_infoprocret_form,
            'r4010_infoprocret_lista': r4010_infoprocret_lista,
            'r4010_inforra_form': r4010_inforra_form,
            'r4010_inforra_lista': r4010_inforra_lista,
            'r4010_infoprocjud_form': r4010_infoprocjud_form,
            'r4010_infoprocjud_lista': r4010_infoprocjud_lista,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r4010_infopgto_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'r4010_infopgto_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r4010_infopgto_salvar.html',
                filename="r4010_infopgto.pdf",
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
            response = render_to_response('r4010_infopgto_salvar.html', context)
            filename = "r4010_infopgto.xls"
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