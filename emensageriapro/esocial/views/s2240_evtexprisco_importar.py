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



def read_s2240_evtexprisco_string(dados, xml, validar=False):
    import untangle
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2240_evtexprisco_obj(doc, status, validar)
    return dados

def read_s2240_evtexprisco(dados, arquivo, validar=False):
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO
    dados = read_s2240_evtexprisco_obj(doc, status, validar)
    return dados



def read_s2240_evtexprisco_obj(doc, status, validar=False):
    s2240_evtexprisco_dados = {}
    s2240_evtexprisco_dados['status'] = status
    xmlns_lista = doc.eSocial['xmlns'].split('/')
    s2240_evtexprisco_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2240_evtexprisco_dados['identidade'] = doc.eSocial.evtExpRisco['Id']
    evtExpRisco = doc.eSocial.evtExpRisco

    try: s2240_evtexprisco_dados['indretif'] = evtExpRisco.ideEvento.indRetif.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['nrrecibo'] = evtExpRisco.ideEvento.nrRecibo.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['tpamb'] = evtExpRisco.ideEvento.tpAmb.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['procemi'] = evtExpRisco.ideEvento.procEmi.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['verproc'] = evtExpRisco.ideEvento.verProc.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['tpinsc'] = evtExpRisco.ideEmpregador.tpInsc.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['nrinsc'] = evtExpRisco.ideEmpregador.nrInsc.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['cpftrab'] = evtExpRisco.ideVinculo.cpfTrab.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['nistrab'] = evtExpRisco.ideVinculo.nisTrab.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['matricula'] = evtExpRisco.ideVinculo.matricula.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['codcateg'] = evtExpRisco.ideVinculo.codCateg.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['dtinicondicao'] = evtExpRisco.infoExpRisco.dtIniCondicao.cdata
    except AttributeError: pass
    try: s2240_evtexprisco_dados['dscativdes'] = evtExpRisco.infoExpRisco.infoAtiv.dscAtivDes.cdata
    except AttributeError: pass
    if 'inclusao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 1
    elif 'alteracao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 2
    elif 'exclusao' in dir(evtExpRisco.infoExpRisco): s2240_evtexprisco_dados['operacao'] = 3
    #print dados
    insert = create_insert('s2240_evtexprisco', s2240_evtexprisco_dados)
    resp = executar_sql(insert, True)
    s2240_evtexprisco_id = resp[0][0]
    dados = s2240_evtexprisco_dados
    dados['evento'] = 's2240'
    dados['id'] = s2240_evtexprisco_id
    dados['identidade_evento'] = doc.eSocial.evtExpRisco['Id']
    dados['status'] = STATUS_EVENTO_IMPORTADO

    if 'infoAmb' in dir(evtExpRisco.infoExpRisco) and evtExpRisco.infoExpRisco.infoAmb.cdata != '':
        for infoAmb in evtExpRisco.infoExpRisco.infoAmb:
            s2240_iniexprisco_infoamb_dados = {}
            s2240_iniexprisco_infoamb_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            try: s2240_iniexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
            except AttributeError: pass
            insert = create_insert('s2240_iniexprisco_infoamb', s2240_iniexprisco_infoamb_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_infoamb_id = resp[0][0]
            #print s2240_iniexprisco_infoamb_id

    if 'ativPericInsal' in dir(evtExpRisco.infoExpRisco.infoAtiv) and evtExpRisco.infoExpRisco.infoAtiv.ativPericInsal.cdata != '':
        for ativPericInsal in evtExpRisco.infoExpRisco.infoAtiv.ativPericInsal:
            s2240_iniexprisco_ativpericinsal_dados = {}
            s2240_iniexprisco_ativpericinsal_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            try: s2240_iniexprisco_ativpericinsal_dados['codativ'] = ativPericInsal.codAtiv.cdata
            except AttributeError: pass
            insert = create_insert('s2240_iniexprisco_ativpericinsal', s2240_iniexprisco_ativpericinsal_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_ativpericinsal_id = resp[0][0]
            #print s2240_iniexprisco_ativpericinsal_id

    if 'fatRisco' in dir(evtExpRisco.infoExpRisco) and evtExpRisco.infoExpRisco.fatRisco.cdata != '':
        for fatRisco in evtExpRisco.infoExpRisco.fatRisco:
            s2240_iniexprisco_fatrisco_dados = {}
            s2240_iniexprisco_fatrisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            try: s2240_iniexprisco_fatrisco_dados['codfatris'] = fatRisco.codFatRis.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['tpaval'] = fatRisco.tpAval.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['intconc'] = fatRisco.intConc.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['limtol'] = fatRisco.limTol.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['unmed'] = fatRisco.unMed.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['tecmedicao'] = fatRisco.tecMedicao.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['insalubridade'] = fatRisco.insalubridade.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['periculosidade'] = fatRisco.periculosidade.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['aposentesp'] = fatRisco.aposentEsp.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['utilizepc'] = fatRisco.epcEpi.utilizEPC.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['eficepc'] = fatRisco.epcEpi.eficEpc.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_fatrisco_dados['utilizepi'] = fatRisco.epcEpi.utilizEPI.cdata
            except AttributeError: pass
            insert = create_insert('s2240_iniexprisco_fatrisco', s2240_iniexprisco_fatrisco_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_fatrisco_id = resp[0][0]
            #print s2240_iniexprisco_fatrisco_id

            if 'epc' in dir(fatRisco.epcEpi) and fatRisco.epcEpi.epc.cdata != '':
                for epc in fatRisco.epcEpi.epc:
                    s2240_iniexprisco_epc_dados = {}
                    s2240_iniexprisco_epc_dados['s2240_iniexprisco_fatrisco_id'] = s2240_iniexprisco_fatrisco_id

                    try: s2240_iniexprisco_epc_dados['codep'] = epc.codEP.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epc_dados['dscepc'] = epc.dscEpc.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epc_dados['eficepc'] = epc.eficEpc.cdata
                    except AttributeError: pass
                    insert = create_insert('s2240_iniexprisco_epc', s2240_iniexprisco_epc_dados)
                    resp = executar_sql(insert, True)
                    s2240_iniexprisco_epc_id = resp[0][0]
                    #print s2240_iniexprisco_epc_id

            if 'epi' in dir(fatRisco.epcEpi) and fatRisco.epcEpi.epi.cdata != '':
                for epi in fatRisco.epcEpi.epi:
                    s2240_iniexprisco_epi_dados = {}
                    s2240_iniexprisco_epi_dados['s2240_iniexprisco_fatrisco_id'] = s2240_iniexprisco_fatrisco_id

                    try: s2240_iniexprisco_epi_dados['caepi'] = epi.caEPI.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epi_dados['dscepi'] = epi.dscEPI.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epi_dados['eficepi'] = epi.eficEpi.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epi_dados['medprotecao'] = epi.medProtecao.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epi_dados['condfuncto'] = epi.condFuncto.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epi_dados['usoinint'] = epi.usoInint.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epi_dados['przvalid'] = epi.przValid.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epi_dados['periodictroca'] = epi.periodicTroca.cdata
                    except AttributeError: pass
                    try: s2240_iniexprisco_epi_dados['higienizacao'] = epi.higienizacao.cdata
                    except AttributeError: pass
                    insert = create_insert('s2240_iniexprisco_epi', s2240_iniexprisco_epi_dados)
                    resp = executar_sql(insert, True)
                    s2240_iniexprisco_epi_id = resp[0][0]
                    #print s2240_iniexprisco_epi_id

    if 'respReg' in dir(evtExpRisco.infoExpRisco) and evtExpRisco.infoExpRisco.respReg.cdata != '':
        for respReg in evtExpRisco.infoExpRisco.respReg:
            s2240_iniexprisco_respreg_dados = {}
            s2240_iniexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            try: s2240_iniexprisco_respreg_dados['cpfresp'] = respReg.cpfResp.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_respreg_dados['nisresp'] = respReg.nisResp.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_respreg_dados['nmresp'] = respReg.nmResp.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_respreg_dados['ideoc'] = respReg.ideOC.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_respreg_dados['dscoc'] = respReg.dscOC.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_respreg_dados['nroc'] = respReg.nrOC.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_respreg_dados['ufoc'] = respReg.ufOC.cdata
            except AttributeError: pass
            insert = create_insert('s2240_iniexprisco_respreg', s2240_iniexprisco_respreg_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_respreg_id = resp[0][0]
            #print s2240_iniexprisco_respreg_id

    if 'obs' in dir(evtExpRisco.infoExpRisco) and evtExpRisco.infoExpRisco.obs.cdata != '':
        for obs in evtExpRisco.infoExpRisco.obs:
            s2240_iniexprisco_obs_dados = {}
            s2240_iniexprisco_obs_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            try: s2240_iniexprisco_obs_dados['meterg'] = obs.metErg.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_obs_dados['obscompl'] = obs.obsCompl.cdata
            except AttributeError: pass
            try: s2240_iniexprisco_obs_dados['observacao'] = obs.observacao.cdata
            except AttributeError: pass
            insert = create_insert('s2240_iniexprisco_obs', s2240_iniexprisco_obs_dados)
            resp = executar_sql(insert, True)
            s2240_iniexprisco_obs_id = resp[0][0]
            #print s2240_iniexprisco_obs_id

    if 'altExpRisco' in dir(evtExpRisco.infoExpRisco) and evtExpRisco.infoExpRisco.altExpRisco.cdata != '':
        for altExpRisco in evtExpRisco.infoExpRisco.altExpRisco:
            s2240_altexprisco_dados = {}
            s2240_altexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            try: s2240_altexprisco_dados['dtaltcondicao'] = altExpRisco.dtAltCondicao.cdata
            except AttributeError: pass
            insert = create_insert('s2240_altexprisco', s2240_altexprisco_dados)
            resp = executar_sql(insert, True)
            s2240_altexprisco_id = resp[0][0]
            #print s2240_altexprisco_id

            if 'infoAmb' in dir(altExpRisco) and altExpRisco.infoAmb.cdata != '':
                for infoAmb in altExpRisco.infoAmb:
                    s2240_altexprisco_infoamb_dados = {}
                    s2240_altexprisco_infoamb_dados['s2240_altexprisco_id'] = s2240_altexprisco_id

                    try: s2240_altexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    except AttributeError: pass
                    try: s2240_altexprisco_infoamb_dados['dscativdes'] = infoAmb.infoAtiv.dscAtivDes.cdata
                    except AttributeError: pass
                    insert = create_insert('s2240_altexprisco_infoamb', s2240_altexprisco_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2240_altexprisco_infoamb_id = resp[0][0]
                    #print s2240_altexprisco_infoamb_id

    if 'fimExpRisco' in dir(evtExpRisco.infoExpRisco) and evtExpRisco.infoExpRisco.fimExpRisco.cdata != '':
        for fimExpRisco in evtExpRisco.infoExpRisco.fimExpRisco:
            s2240_fimexprisco_dados = {}
            s2240_fimexprisco_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            try: s2240_fimexprisco_dados['dtfimcondicao'] = fimExpRisco.dtFimCondicao.cdata
            except AttributeError: pass
            insert = create_insert('s2240_fimexprisco', s2240_fimexprisco_dados)
            resp = executar_sql(insert, True)
            s2240_fimexprisco_id = resp[0][0]
            #print s2240_fimexprisco_id

            if 'infoAmb' in dir(fimExpRisco) and fimExpRisco.infoAmb.cdata != '':
                for infoAmb in fimExpRisco.infoAmb:
                    s2240_fimexprisco_infoamb_dados = {}
                    s2240_fimexprisco_infoamb_dados['s2240_fimexprisco_id'] = s2240_fimexprisco_id

                    try: s2240_fimexprisco_infoamb_dados['codamb'] = infoAmb.codAmb.cdata
                    except AttributeError: pass
                    insert = create_insert('s2240_fimexprisco_infoamb', s2240_fimexprisco_infoamb_dados)
                    resp = executar_sql(insert, True)
                    s2240_fimexprisco_infoamb_id = resp[0][0]
                    #print s2240_fimexprisco_infoamb_id

    if 'respReg' in dir(evtExpRisco.infoExpRisco) and evtExpRisco.infoExpRisco.respReg.cdata != '':
        for respReg in evtExpRisco.infoExpRisco.respReg:
            s2240_fimexprisco_respreg_dados = {}
            s2240_fimexprisco_respreg_dados['s2240_evtexprisco_id'] = s2240_evtexprisco_id

            try: s2240_fimexprisco_respreg_dados['dtini'] = respReg.dtIni.cdata
            except AttributeError: pass
            try: s2240_fimexprisco_respreg_dados['dtfim'] = respReg.dtFim.cdata
            except AttributeError: pass
            try: s2240_fimexprisco_respreg_dados['nisresp'] = respReg.nisResp.cdata
            except AttributeError: pass
            try: s2240_fimexprisco_respreg_dados['nroc'] = respReg.nrOc.cdata
            except AttributeError: pass
            try: s2240_fimexprisco_respreg_dados['ufoc'] = respReg.ufOC.cdata
            except AttributeError: pass
            insert = create_insert('s2240_fimexprisco_respreg', s2240_fimexprisco_respreg_dados)
            resp = executar_sql(insert, True)
            s2240_fimexprisco_respreg_id = resp[0][0]
            #print s2240_fimexprisco_respreg_id

    from emensageriapro.esocial.views.s2240_evtexprisco_verificar import validar_evento_funcao
    if validar: validar_evento_funcao(s2240_evtexprisco_id, 'default')
    return dados