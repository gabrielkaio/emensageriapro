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
from emensageriapro.s5011.forms import *
from emensageriapro.s5011.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.s5011.models import s5011infoTercSusp
from emensageriapro.s5011.forms import form_s5011_infotercsusp
from emensageriapro.s5011.models import s5011infoEmprParcial
from emensageriapro.s5011.forms import form_s5011_infoemprparcial
from emensageriapro.s5011.models import s5011dadosOpPort
from emensageriapro.s5011.forms import form_s5011_dadosopport
from emensageriapro.s5011.models import s5011basesRemun
from emensageriapro.s5011.forms import form_s5011_basesremun
from emensageriapro.s5011.models import s5011basesAvNPort
from emensageriapro.s5011.forms import form_s5011_basesavnport
from emensageriapro.s5011.models import s5011infoSubstPatrOpPort
from emensageriapro.s5011.forms import form_s5011_infosubstpatropport



@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    
    try: 
        usuario_id = request.user.id    
        dict_hash = get_hash_url( hash )
        s5011_idelotacao_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='s5011_idelotacao')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s5011_idelotacao_id:
        s5011_idelotacao = get_object_or_404(s5011ideLotacao, id = s5011_idelotacao_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    if s5011_idelotacao_id:
        dados_evento = s5011_idelotacao.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s5011_idelotacao_apagar'] = 0
            dict_permissoes['s5011_idelotacao_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s5011_idelotacao_id:
            s5011_idelotacao_form = form_s5011_idelotacao(request.POST or None, instance = s5011_idelotacao,  
                                         initial={'excluido': False})
        else:
            s5011_idelotacao_form = form_s5011_idelotacao(request.POST or None, 
                                         initial={'excluido': False})
        if request.method == 'POST':
            if s5011_idelotacao_form.is_valid():
            
                dados = s5011_idelotacao_form.cleaned_data
                obj = s5011_idelotacao_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not s5011_idelotacao_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 's5011_idelotacao', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(s5011_idelotacao), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     's5011_idelotacao', s5011_idelotacao_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('s5011_idelotacao_apagar', 's5011_idelotacao_salvar', 's5011_idelotacao'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s5011_idelotacao_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s5011_idelotacao_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        s5011_idelotacao_form = disabled_form_fields(s5011_idelotacao_form, permissao.permite_editar)
        
        if s5011_idelotacao_id:
            if dados_evento['status'] != 0:
                s5011_idelotacao_form = disabled_form_fields(s5011_idelotacao_form, 0)
                
        #s5011_idelotacao_campos_multiple_passo3
        
        if int(dict_hash['print']):
            s5011_idelotacao_form = disabled_form_for_print(s5011_idelotacao_form)
            
        
        s5011_infotercsusp_lista = None 
        s5011_infotercsusp_form = None 
        s5011_infoemprparcial_lista = None 
        s5011_infoemprparcial_form = None 
        s5011_dadosopport_lista = None 
        s5011_dadosopport_form = None 
        s5011_basesremun_lista = None 
        s5011_basesremun_form = None 
        s5011_basesavnport_lista = None 
        s5011_basesavnport_form = None 
        s5011_infosubstpatropport_lista = None 
        s5011_infosubstpatropport_form = None 
        
        if s5011_idelotacao_id:
            s5011_idelotacao = get_object_or_404(s5011ideLotacao, id = s5011_idelotacao_id)
            
            s5011_infotercsusp_form = form_s5011_infotercsusp(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_infotercsusp_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_infotercsusp_lista = s5011infoTercSusp.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
            s5011_infoemprparcial_form = form_s5011_infoemprparcial(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_infoemprparcial_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_infoemprparcial_lista = s5011infoEmprParcial.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
            s5011_dadosopport_form = form_s5011_dadosopport(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_dadosopport_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_dadosopport_lista = s5011dadosOpPort.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
            s5011_basesremun_form = form_s5011_basesremun(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_basesremun_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_basesremun_lista = s5011basesRemun.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
            s5011_basesavnport_form = form_s5011_basesavnport(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_basesavnport_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_basesavnport_lista = s5011basesAvNPort.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
            s5011_infosubstpatropport_form = form_s5011_infosubstpatropport(
                initial={ 's5011_idelotacao': s5011_idelotacao })
            s5011_infosubstpatropport_form.fields['s5011_idelotacao'].widget.attrs['readonly'] = True
            s5011_infosubstpatropport_lista = s5011infoSubstPatrOpPort.objects.\
                filter(s5011_idelotacao_id=s5011_idelotacao.id).all()
                
        else:
            s5011_idelotacao = None
            
        #s5011_idelotacao_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's5011_idelotacao' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's5011_idelotacao_salvar'
        controle_alteracoes = Auditoria.objects.filter(identidade=s5011_idelotacao_id, tabela='s5011_idelotacao').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'], 
            'validacao_precedencia': dados_evento['validacao_precedencia'], 
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'], 
            'controle_alteracoes': controle_alteracoes, 
            's5011_idelotacao': s5011_idelotacao, 
            's5011_idelotacao_form': s5011_idelotacao_form, 
            'mensagem': mensagem, 
            's5011_idelotacao_id': int(s5011_idelotacao_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            's5011_infotercsusp_form': s5011_infotercsusp_form,
            's5011_infotercsusp_lista': s5011_infotercsusp_lista,
            's5011_infoemprparcial_form': s5011_infoemprparcial_form,
            's5011_infoemprparcial_lista': s5011_infoemprparcial_lista,
            's5011_dadosopport_form': s5011_dadosopport_form,
            's5011_dadosopport_lista': s5011_dadosopport_lista,
            's5011_basesremun_form': s5011_basesremun_form,
            's5011_basesremun_lista': s5011_basesremun_lista,
            's5011_basesavnport_form': s5011_basesavnport_form,
            's5011_basesavnport_lista': s5011_basesavnport_lista,
            's5011_infosubstpatropport_form': s5011_infosubstpatropport_form,
            's5011_infosubstpatropport_lista': s5011_infosubstpatropport_lista,
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s5011_idelotacao_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's5011_idelotacao_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s5011_idelotacao_salvar.html',
                filename="s5011_idelotacao.pdf",
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
            response = render_to_response('s5011_idelotacao_salvar.html', context)
            filename = "s5011_idelotacao.xls"
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