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
from emensageriapro.r3010.forms import *
from emensageriapro.r3010.models import *
from emensageriapro.controle_de_acesso.models import *


@login_required
def apagar(request, hash):
    from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO
    
    
    try: 
        usuario_id = request.user.id 
        dict_hash = get_hash_url( hash )
        r3010_outrasreceitas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
        
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='r3010_outrasreceitas')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r3010_outrasreceitas = get_object_or_404(r3010outrasReceitas, id = r3010_outrasreceitas_id)
    dados_evento = {}
    if r3010_outrasreceitas_id:
        dados_evento = r3010_outrasreceitas.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['r3010_outrasreceitas_apagar'] = 0
            dict_permissoes['r3010_outrasreceitas_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == STATUS_EVENTO_CADASTRADO:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r3010_outrasreceitas), indent=4, sort_keys=True, default=str)
            obj = r3010outrasReceitas.objects.get(id = r3010_outrasreceitas_id)
            obj.delete(request=request)
            #r3010_outrasreceitas_apagar_custom
            #r3010_outrasreceitas_apagar_custom
            messages.success(request, u'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '', 
                             'r3010_outrasreceitas', r3010_outrasreceitas_id, usuario_id, 3)
        else:
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
            
        if request.session['retorno_pagina']== 'r3010_outrasreceitas_salvar':
            return redirect('r3010_outrasreceitas', hash=request.session['retorno_hash'])
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
    return render(request, 'r3010_outrasreceitas_apagar.html', context)