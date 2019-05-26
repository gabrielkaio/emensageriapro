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
from emensageriapro.r2010.forms import *
from emensageriapro.r2010.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def listar(request, hash):
    for_print = 0
    
    try: 
        usuario_id = request.user.id   
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #r2010_infotpserv_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='r2010_infotpserv')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    

    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = { 
            'show_r2010_nfs': 1,
            'show_tpservico': 1,
            'show_vlrbaseret': 1,
            'show_vlrretencao': 1,
            'show_vlrretsub': 0,
            'show_vlrnretprinc': 0,
            'show_vlrservicos15': 0,
            'show_vlrservicos20': 0,
            'show_vlrservicos25': 0,
            'show_vlradicional': 0,
            'show_vlrnretadic': 0, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = { 
                'r2010_nfs__icontains': 'r2010_nfs__icontains',
                'tpservico__icontains': 'tpservico__icontains',
                'vlrbaseret__icontains': 'vlrbaseret__icontains',
                'vlrretencao__icontains': 'vlrretencao__icontains',
                'vlrretsub__icontains': 'vlrretsub__icontains',
                'vlrnretprinc__icontains': 'vlrnretprinc__icontains',
                'vlrservicos15__icontains': 'vlrservicos15__icontains',
                'vlrservicos20__icontains': 'vlrservicos20__icontains',
                'vlrservicos25__icontains': 'vlrservicos25__icontains',
                'vlradicional__icontains': 'vlradicional__icontains',
                'vlrnretadic__icontains': 'vlrnretadic__icontains', }
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = { 
                    'r2010_nfs__icontains': 'r2010_nfs__icontains',
                    'tpservico__icontains': 'tpservico__icontains',
                    'vlrbaseret__icontains': 'vlrbaseret__icontains',
                    'vlrretencao__icontains': 'vlrretencao__icontains',
                    'vlrretsub__icontains': 'vlrretsub__icontains',
                    'vlrnretprinc__icontains': 'vlrnretprinc__icontains',
                    'vlrservicos15__icontains': 'vlrservicos15__icontains',
                    'vlrservicos20__icontains': 'vlrservicos20__icontains',
                    'vlrservicos25__icontains': 'vlrservicos25__icontains',
                    'vlradicional__icontains': 'vlradicional__icontains',
                    'vlrnretadic__icontains': 'vlrnretadic__icontains', }
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r2010_infotpserv_lista = r2010infoTpServ.objects.filter(**dict_qs).filter().exclude(id=0).all()
        if not post and len(r2010_infotpserv_lista) > 100:
            filtrar = True
            r2010_infotpserv_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')
        #[VARIAVEIS_LISTA_FILTRO_RELATORIO]
        #r2010_infotpserv_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r2010_infotpserv'
        context = {
            'r2010_infotpserv_lista': r2010_infotpserv_lista, 
            
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
            #[VARIAVEIS_FILTRO_RELATORIO]
        }
        if for_print in (0,1):
            return render(request, 'r2010_infotpserv_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/r2010_infotpserv_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2010_infotpserv_listar.html',
                filename="r2010_infotpserv.pdf",
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
            response = render_to_response('r2010_infotpserv_listar.html', context)
            filename = "r2010_infotpserv.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('csv/r2010_infotpserv.csv', context)
            filename = "r2010_infotpserv.csv"
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