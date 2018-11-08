#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.r3010.forms import *
from emensageriapro.r3010.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


@login_required
def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r3010_outrasreceitas_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r3010_outrasreceitas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r3010_outrasreceitas_id:
        r3010_outrasreceitas = get_object_or_404(r3010outrasReceitas.objects.using( db_slug ), excluido = False, id = r3010_outrasreceitas_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if r3010_outrasreceitas_id:
        dados_evento = r3010_outrasreceitas.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r3010_outrasreceitas_apagar'] = 0
            dict_permissoes['r3010_outrasreceitas_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r3010_outrasreceitas_id:
            r3010_outrasreceitas_form = form_r3010_outrasreceitas(request.POST or None, instance = r3010_outrasreceitas, slug = db_slug)
        else:
            r3010_outrasreceitas_form = form_r3010_outrasreceitas(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if r3010_outrasreceitas_form.is_valid():
                dados = r3010_outrasreceitas_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if r3010_outrasreceitas_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #r3010_outrasreceitas_campos_multiple_passo1
                        r3010outrasReceitas.objects.using(db_slug).filter(id=r3010_outrasreceitas_id).update(**dados)
                        obj = r3010outrasReceitas.objects.using(db_slug).get(id=r3010_outrasreceitas_id)
                        #r3010_outrasreceitas_editar_custom
                        #r3010_outrasreceitas_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(r3010_outrasreceitas), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         'r3010_outrasreceitas', r3010_outrasreceitas_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #r3010_outrasreceitas_cadastrar_campos_multiple_passo1
                    obj = r3010outrasReceitas(**dados)
                    obj.save(using = db_slug)
                    #r3010_outrasreceitas_cadastrar_custom
                    #r3010_outrasreceitas_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r3010_outrasreceitas', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('r3010_outrasreceitas_apagar', 'r3010_outrasreceitas_salvar', 'r3010_outrasreceitas'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if r3010_outrasreceitas_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('r3010_outrasreceitas_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        r3010_outrasreceitas_form = disabled_form_fields(r3010_outrasreceitas_form, permissao.permite_editar)
        if r3010_outrasreceitas_id:
            if dados_evento['status'] != 0:
                r3010_outrasreceitas_form = disabled_form_fields(r3010_outrasreceitas_form, 0)
        #r3010_outrasreceitas_campos_multiple_passo3

        for field in r3010_outrasreceitas_form.fields.keys():
            r3010_outrasreceitas_form.fields[field].widget.attrs['ng-model'] = 'r3010_outrasreceitas_'+field
        if int(dict_hash['print']):
            r3010_outrasreceitas_form = disabled_form_for_print(r3010_outrasreceitas_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if r3010_outrasreceitas_id:
            r3010_outrasreceitas = get_object_or_404(r3010outrasReceitas.objects.using( db_slug ), excluido = False, id = r3010_outrasreceitas_id)
            pass
        else:
            r3010_outrasreceitas = None
        #r3010_outrasreceitas_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'r3010_outrasreceitas' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r3010_outrasreceitas_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r3010_outrasreceitas_id, tabela='r3010_outrasreceitas').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            'r3010_outrasreceitas': r3010_outrasreceitas,
            'r3010_outrasreceitas_form': r3010_outrasreceitas_form,
            'mensagem': mensagem,
            'r3010_outrasreceitas_id': int(r3010_outrasreceitas_id),
            'usuario': usuario,
       
            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
       
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r3010_outrasreceitas_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'r3010_outrasreceitas_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r3010_outrasreceitas_salvar.html',
                filename="r3010_outrasreceitas.pdf",
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
            response = render_to_response('r3010_outrasreceitas_salvar.html', context)
            filename = "r3010_outrasreceitas.xls"
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

@login_required
def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        r3010_outrasreceitas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r3010_outrasreceitas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r3010_outrasreceitas = get_object_or_404(r3010outrasReceitas.objects.using( db_slug ), excluido = False, id = r3010_outrasreceitas_id)
    dados_evento = {}
    if r3010_outrasreceitas_id:
        dados_evento = r3010_outrasreceitas.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r3010_outrasreceitas_apagar'] = 0
            dict_permissoes['r3010_outrasreceitas_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r3010_outrasreceitas), indent=4, sort_keys=True, default=str)
            r3010outrasReceitas.objects.using( db_slug ).filter(id = r3010_outrasreceitas_id).delete()
            #r3010_outrasreceitas_apagar_custom
            #r3010_outrasreceitas_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r3010_outrasreceitas', r3010_outrasreceitas_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')
   
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

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class r3010outrasReceitasList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = r3010outrasReceitas.objects.using(db_slug).all()
    serializer_class = r3010outrasReceitasSerializer
    permission_classes = (IsAdminUser,)


class r3010outrasReceitasDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = r3010outrasReceitas.objects.using(db_slug).all()
    serializer_class = r3010outrasReceitasSerializer
    permission_classes = (IsAdminUser,)


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #r3010_outrasreceitas_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r3010_outrasreceitas')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_descreceita': 1,
            'show_vlrreceita': 1,
            'show_tpreceita': 1,
            'show_r3010_boletim': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'descreceita__icontains': 'descreceita__icontains',
                'vlrreceita': 'vlrreceita',
                'tpreceita': 'tpreceita',
                'r3010_boletim': 'r3010_boletim',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'descreceita__icontains': 'descreceita__icontains',
                'vlrreceita': 'vlrreceita',
                'tpreceita': 'tpreceita',
                'r3010_boletim': 'r3010_boletim',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r3010_outrasreceitas_lista = r3010outrasReceitas.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r3010_outrasreceitas_lista) > 100:
            filtrar = True
            r3010_outrasreceitas_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #r3010_outrasreceitas_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r3010_outrasreceitas'
        context = {
            'r3010_outrasreceitas_lista': r3010_outrasreceitas_lista,
       
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
   
        }
        if for_print in (0,1):
            return render(request, 'r3010_outrasreceitas_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r3010_outrasreceitas_listar.html',
                filename="r3010_outrasreceitas.pdf",
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
            response = render_to_response('r3010_outrasreceitas_listar.html', context)
            filename = "r3010_outrasreceitas.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/r3010_outrasreceitas_csv.html', context)
            filename = "r3010_outrasreceitas.csv"
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

