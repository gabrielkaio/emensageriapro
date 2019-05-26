#coding:utf-8

import xmltodict
import pprint
import json
import psycopg2
from emensageriapro.padrao import ler_arquivo
from emensageriapro.esocial.models import *
from emensageriapro.s2190.models import *



def read_s2190_evtadmprelim_string(dados, xml, validar=False):

    import untangle
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO
    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2190_evtadmprelim_obj(doc, status, validar)
    return dados



def read_s2190_evtadmprelim(dados, arquivo, validar=False):

    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)

    if validar:
        status = STATUS_EVENTO_IMPORTADO

    else:
        status = STATUS_EVENTO_CADASTRADO

    dados = read_s2190_evtadmprelim_obj(doc, status, validar)
    return dados



def read_s2190_evtadmprelim_obj(doc, status, validar=False):

    xmlns_lista = doc.eSocial['xmlns'].split('/')

    s2190_evtadmprelim_dados = {}
    s2190_evtadmprelim_dados['status'] = status
    s2190_evtadmprelim_dados['versao'] = xmlns_lista[len(xmlns_lista)-1]
    s2190_evtadmprelim_dados['identidade'] = doc.eSocial.evtAdmPrelim['Id']
    evtAdmPrelim = doc.eSocial.evtAdmPrelim
    
    try:
        s2190_evtadmprelim_dados['tpamb'] = evtAdmPrelim.ideEvento.tpAmb.cdata
    except AttributeError: 
        pass
    
    try:
        s2190_evtadmprelim_dados['procemi'] = evtAdmPrelim.ideEvento.procEmi.cdata
    except AttributeError: 
        pass
    
    try:
        s2190_evtadmprelim_dados['verproc'] = evtAdmPrelim.ideEvento.verProc.cdata
    except AttributeError: 
        pass
    
    try:
        s2190_evtadmprelim_dados['tpinsc'] = evtAdmPrelim.ideEmpregador.tpInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2190_evtadmprelim_dados['nrinsc'] = evtAdmPrelim.ideEmpregador.nrInsc.cdata
    except AttributeError: 
        pass
    
    try:
        s2190_evtadmprelim_dados['cpftrab'] = evtAdmPrelim.infoRegPrelim.cpfTrab.cdata
    except AttributeError: 
        pass
    
    try:
        s2190_evtadmprelim_dados['dtnascto'] = evtAdmPrelim.infoRegPrelim.dtNascto.cdata
    except AttributeError: 
        pass
    
    try:
        s2190_evtadmprelim_dados['dtadm'] = evtAdmPrelim.infoRegPrelim.dtAdm.cdata
    except AttributeError: 
        pass
        
    s2190_evtadmprelim = s2190evtAdmPrelim.objects.create(**s2190_evtadmprelim_dados)    
    s2190_evtadmprelim_dados['evento'] = 's2190'
    s2190_evtadmprelim_dados['id'] = s2190_evtadmprelim.id
    s2190_evtadmprelim_dados['identidade_evento'] = doc.eSocial.evtAdmPrelim['Id']
    s2190_evtadmprelim_dados['status'] = STATUS_EVENTO_IMPORTADO


    from emensageriapro.esocial.views.s2190_evtadmprelim_validar_evento import validar_evento_funcao
    if validar:
        validar_evento_funcao(s2190_evtadmprelim.id)
    return s2190_evtadmprelim_dados