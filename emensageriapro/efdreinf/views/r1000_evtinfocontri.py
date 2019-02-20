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
import json
import base64
from emensageriapro.r1000.models import r1000inclusao
from emensageriapro.r1000.models import r1000alteracao
from emensageriapro.r1000.models import r1000exclusao
from emensageriapro.r1000.forms import form_r1000_inclusao
from emensageriapro.r1000.forms import form_r1000_alteracao
from emensageriapro.r1000.forms import form_r1000_exclusao

#IMPORTACOES
@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r1000_evtinfocontri_id = int(dict_hash['id'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r1000_evtinfocontri')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = r1000_evtinfocontri_id)

    if r1000_evtinfocontri_id:
        if r1000_evtinfocontri.status != 0:
            dict_permissoes['r1000_evtinfocontri_apagar'] = 0
            dict_permissoes['r1000_evtinfocontri_editar'] = 0

    if request.method == 'POST':
        if r1000_evtinfocontri.status == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r1000_evtinfocontri), indent=4, sort_keys=True, default=str)
            obj = r1000evtInfoContri.objects.using( db_slug ).get(id = r1000_evtinfocontri_id)
            obj.delete(request=request)
            #r1000_evtinfocontri_apagar_custom
            #r1000_evtinfocontri_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r1000_evtinfocontri', r1000_evtinfocontri_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 'r1000_evtinfocontri_salvar':
            return redirect('r1000_evtinfocontri', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,

        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'r1000_evtinfocontri_apagar.html', context)

class r1000evtInfoContriList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = r1000evtInfoContri.objects.using(db_slug).all()
    serializer_class = r1000evtInfoContriSerializer
    # permission_classes = (IsAdminUser,)


class r1000evtInfoContriDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = r1000evtInfoContri.objects.using(db_slug).all()
    serializer_class = r1000evtInfoContriSerializer
    # permission_classes = (IsAdminUser,)


@login_required
def listar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r1000_evtinfocontri')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_arquivo': 0,
            'show_arquivo_original': 0,
            'show_cdretorno': 1,
            'show_descretorno': 0,
            'show_dhprocess': 0,
            'show_evtinfocontri': 0,
            'show_idecontri': 0,
            'show_ideevento': 0,
            'show_identidade': 1,
            'show_nrinsc': 0,
            'show_ocorrencias': 0,
            'show_operacao': 1,
            'show_procemi': 0,
            'show_retornos_evttotal': 0,
            'show_retornos_evttotalcontrib': 0,
            'show_status': 1,
            'show_tpamb': 0,
            'show_tpinsc': 0,
            'show_transmissor_lote_efdreinf': 0,
            'show_validacao_precedencia': 0,
            'show_validacoes': 0,
            'show_verproc': 0,
            'show_versao': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'evtinfocontri': 'evtinfocontri',
                'idecontri': 'idecontri',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'operacao': 'operacao',
                'procemi': 'procemi',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'evtinfocontri': 'evtinfocontri',
                'idecontri': 'idecontri',
                'ideevento': 'ideevento',
                'identidade__icontains': 'identidade__icontains',
                'nrinsc__icontains': 'nrinsc__icontains',
                'operacao': 'operacao',
                'procemi': 'procemi',
                'status': 'status',
                'tpamb': 'tpamb',
                'tpinsc': 'tpinsc',
                'transmissor_lote_efdreinf': 'transmissor_lote_efdreinf',
                'verproc__icontains': 'verproc__icontains',
                'versao__icontains': 'versao__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r1000_evtinfocontri_lista = r1000evtInfoContri.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r1000_evtinfocontri_lista) > 100:
            filtrar = True
            r1000_evtinfocontri_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        transmissor_lote_efdreinf_lista = TransmissorLoteEfdreinf.objects.using( db_slug ).filter(excluido = False).all()
        #r1000_evtinfocontri_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r1000_evtinfocontri'
        context = {
            'r1000_evtinfocontri_lista': r1000_evtinfocontri_lista,
  
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,

            'transmissor_lote_efdreinf_lista': transmissor_lote_efdreinf_lista,
        }

        if for_print in (0,1):
            return render(request, 'r1000_evtinfocontri_listar.html', context)

        elif for_print == 2:
            from emensageriapro.functions import render_to_pdf
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r1000_evtinfocontri_listar.html',
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
                             'viewport-size': "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response

        elif for_print == 3:
            response = render_to_response('r1000_evtinfocontri_listar.html', context)
            filename = "r1000_evtinfocontri.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

        elif for_print == 4:
            response = render_to_response('tables/r1000_evtinfocontri_csv.html', context)
            filename = "r1000_evtinfocontri.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
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

def gerar_identidade(request, chave, evento_id):
    from emensageriapro.functions import identidade_evento
    from emensageriapro.settings import PASS_SCRIPT
    if chave == PASS_SCRIPT:
        db_slug = 'default'
        obj = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = evento_id)
        ident = identidade_evento(obj)
        mensagem = ident
    else:
        mensagem = 'Chave incorreta!'
    return HttpResponse(mensagem)


@login_required
def salvar(request, hash):
    from emensageriapro.settings import VERSAO_EMENSAGERIA, VERSAO_LAYOUT_EFDREINF, TP_AMB
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r1000_evtinfocontri_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        return redirect('login')

    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r1000_evtinfocontri')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if r1000_evtinfocontri_id:
        r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = r1000_evtinfocontri_id)

        if r1000_evtinfocontri.status != 0:
            dict_permissoes['r1000_evtinfocontri_apagar'] = 0
            dict_permissoes['r1000_evtinfocontri_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r1000_evtinfocontri_id:
            r1000_evtinfocontri_form = form_r1000_evtinfocontri(request.POST or None, instance = r1000_evtinfocontri, slug = db_slug)
        else:
            r1000_evtinfocontri_form = form_r1000_evtinfocontri(request.POST or None, slug = db_slug, initial={'versao': VERSAO_LAYOUT_EFDREINF, 'status': 0, 'processamento_codigo_resposta': 0, 'tpamb': TP_AMB, 'procemi': 1, 'verproc': VERSAO_EMENSAGERIA})
        if request.method == 'POST':
            if r1000_evtinfocontri_form.is_valid():

                dados = r1000_evtinfocontri_form.cleaned_data
                obj = r1000_evtinfocontri_form.save(request=request)
                messages.success(request, 'Salvo com sucesso!')

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
                messages.error(request, 'Erro ao salvar!')
        r1000_evtinfocontri_form = disabled_form_fields(r1000_evtinfocontri_form, permissao.permite_editar)

        if r1000_evtinfocontri_id:
            if r1000_evtinfocontri.status != 0:
                r1000_evtinfocontri_form = disabled_form_fields(r1000_evtinfocontri_form, False)
        #r1000_evtinfocontri_campos_multiple_passo3

        for field in r1000_evtinfocontri_form.fields.keys():
            r1000_evtinfocontri_form.fields[field].widget.attrs['ng-model'] = 'r1000_evtinfocontri_'+field
        if int(dict_hash['print']):
            r1000_evtinfocontri_form = disabled_form_for_print(r1000_evtinfocontri_form)

        r1000_inclusao_form = None
        r1000_inclusao_lista = None
        r1000_alteracao_form = None
        r1000_alteracao_lista = None
        r1000_exclusao_form = None
        r1000_exclusao_lista = None
        if r1000_evtinfocontri_id:
            r1000_evtinfocontri = get_object_or_404(r1000evtInfoContri.objects.using( db_slug ), excluido = False, id = r1000_evtinfocontri_id)

            r1000_inclusao_form = form_r1000_inclusao(initial={ 'r1000_evtinfocontri': r1000_evtinfocontri }, slug=db_slug)
            r1000_inclusao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_inclusao_lista = r1000inclusao.objects.using( db_slug ).filter(excluido = False, r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
            r1000_alteracao_form = form_r1000_alteracao(initial={ 'r1000_evtinfocontri': r1000_evtinfocontri }, slug=db_slug)
            r1000_alteracao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_alteracao_lista = r1000alteracao.objects.using( db_slug ).filter(excluido = False, r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
            r1000_exclusao_form = form_r1000_exclusao(initial={ 'r1000_evtinfocontri': r1000_evtinfocontri }, slug=db_slug)
            r1000_exclusao_form.fields['r1000_evtinfocontri'].widget.attrs['readonly'] = True
            r1000_exclusao_lista = r1000exclusao.objects.using( db_slug ).filter(excluido = False, r1000_evtinfocontri_id=r1000_evtinfocontri.id).all()
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
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r1000_evtinfocontri_id, tabela='r1000_evtinfocontri').all()
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

        if for_print in (0,1 ):
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

