#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos <www.emensageria.com.br>
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
import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo, create_insert, executar_sql


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO



def read_r2098_evtreabreevper_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2098_evtreabreevper_obj(doc, status, validar)
    return dados

def read_r2098_evtreabreevper(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_r2098_evtreabreevper_obj(doc, status, validar)
    return dados



def read_r2098_evtreabreevper_obj(doc, status, validar=False):
    r2098_evtreabreevper_dados = {}
    r2098_evtreabreevper_dados['status'] = status
    xmlns_lista = doc.Reinf['xmlns'].split('/')
    r2098_evtreabreevper_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    r2098_evtreabreevper_dados['identidade'] = doc.Reinf.evtReabreEvPer['id']
    evtReabreEvPer = doc.Reinf.evtReabreEvPer

    try: r2098_evtreabreevper_dados['perapur'] = evtReabreEvPer.ideEvento.perApur.cdata
    except AttributeError: pass
    try: r2098_evtreabreevper_dados['tpamb'] = evtReabreEvPer.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: r2098_evtreabreevper_dados['procemi'] = evtReabreEvPer.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: r2098_evtreabreevper_dados['verproc'] = evtReabreEvPer.ideEvento.verProc.cdata
    except AttributeError: pass
    try: r2098_evtreabreevper_dados['tpinsc'] = evtReabreEvPer.ideContri.tpInsc.cdata
    except AttributeError: pass
    try: r2098_evtreabreevper_dados['nrinsc'] = evtReabreEvPer.ideContri.nrInsc.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtReabreEvPer.ideContri): r2098_evtreabreevper_dados['operacao'] = 1
    elif 'alteracao' in dir(evtReabreEvPer.ideContri): r2098_evtreabreevper_dados['operacao'] = 2
    elif 'exclusao' in dir(evtReabreEvPer.ideContri): r2098_evtreabreevper_dados['operacao'] = 3
    #print dados
    insert = create_insert('r2098_evtreabreevper', r2098_evtreabreevper_dados)
    resp = executar_sql(insert, True)
    r2098_evtreabreevper_id = resp[0][0]
    dados = r2098_evtreabreevper_dados
    dados['evento'] = 'r2098'
    dados['id'] = r2098_evtreabreevper_id
    dados['identidade_evento'] = doc.Reinf.evtReabreEvPer['id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    from emensageriapro.efdreinf.views.r2098_evtreabreevper_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(r2098_evtreabreevper_id, 'default')
    return dados