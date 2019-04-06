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



def read_s2260_evtconvinterm_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2260_evtconvinterm_obj(doc, status, validar)
    return dados

def read_s2260_evtconvinterm(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2260_evtconvinterm_obj(doc, status, validar)
    return dados



def read_s2260_evtconvinterm_obj(doc, status, validar=False):
    s2260_evtconvinterm_dados = {}
    s2260_evtconvinterm_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2260_evtconvinterm_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2260_evtconvinterm_dados['identidade'] = doc.eSocial.evtConvInterm['Id']
    evtConvInterm = doc.eSocial.evtConvInterm

    try: s2260_evtconvinterm_dados['indretif'] = evtConvInterm.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['nrrecibo'] = evtConvInterm.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['tpamb'] = evtConvInterm.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['procemi'] = evtConvInterm.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['verproc'] = evtConvInterm.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['tpinsc'] = evtConvInterm.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['nrinsc'] = evtConvInterm.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['cpftrab'] = evtConvInterm.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['nistrab'] = evtConvInterm.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['matricula'] = evtConvInterm.ideVinculo.matricula.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['codconv'] = evtConvInterm.infoConvInterm.codConv.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['dtinicio'] = evtConvInterm.infoConvInterm.dtInicio.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['dtfim'] = evtConvInterm.infoConvInterm.dtFim.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['dtprevpgto'] = evtConvInterm.infoConvInterm.dtPrevPgto.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['codhorcontrat'] = evtConvInterm.infoConvInterm.jornada.codHorContrat.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['dscjornada'] = evtConvInterm.infoConvInterm.jornada.dscJornada.cdata
    except AttributeError: pass
    try: s2260_evtconvinterm_dados['indlocal'] = evtConvInterm.infoConvInterm.localTrab.indLocal.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['operacao'] = 1
    elif 'alteracao' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['operacao'] = 2
    elif 'exclusao' in dir(evtConvInterm.infoConvInterm): s2260_evtconvinterm_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2260_evtconvinterm', s2260_evtconvinterm_dados)
    resp = executar_sql(insert, True)
    s2260_evtconvinterm_id = resp[0][0]
    dados = s2260_evtconvinterm_dados
    dados['evento'] = 's2260'
    dados['id'] = s2260_evtconvinterm_id
    dados['identidade_evento'] = doc.eSocial.evtConvInterm['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'localTrabInterm' in dir(evtConvInterm.infoConvInterm.localTrab) and evtConvInterm.infoConvInterm.localTrab.localTrabInterm.cdata != '':
        for localTrabInterm in evtConvInterm.infoConvInterm.localTrab.localTrabInterm:
            s2260_localtrabinterm_dados = {}
            s2260_localtrabinterm_dados['s2260_evtconvinterm_id'] = s2260_evtconvinterm_id

            try: s2260_localtrabinterm_dados['tplograd'] = localTrabInterm.tpLograd.cdata
            except AttributeError: pass
            try: s2260_localtrabinterm_dados['dsclograd'] = localTrabInterm.dscLograd.cdata
            except AttributeError: pass
            try: s2260_localtrabinterm_dados['nrlograd'] = localTrabInterm.nrLograd.cdata
            except AttributeError: pass
            try: s2260_localtrabinterm_dados['complem'] = localTrabInterm.complem.cdata
            except AttributeError: pass
            try: s2260_localtrabinterm_dados['bairro'] = localTrabInterm.bairro.cdata
            except AttributeError: pass
            try: s2260_localtrabinterm_dados['cep'] = localTrabInterm.cep.cdata
            except AttributeError: pass
            try: s2260_localtrabinterm_dados['codmunic'] = localTrabInterm.codMunic.cdata
            except AttributeError: pass
            try: s2260_localtrabinterm_dados['uf'] = localTrabInterm.uf.cdata
            except AttributeError: pass
            insert = create_insert('s2260_localtrabinterm', s2260_localtrabinterm_dados)
            resp = executar_sql(insert, True)
            s2260_localtrabinterm_id = resp[0][0]
            #print s2260_localtrabinterm_id

    from emensageriapro.esocial.views.s2260_evtconvinterm_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2260_evtconvinterm_id, 'default')
    return dados