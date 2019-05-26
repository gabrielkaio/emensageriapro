#coding:utf-8
"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos<www.emensageria.com.br>
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
from emensageriapro.padrao import ler_arquivo


def validacoes_s1070_evttabprocesso(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabProcesso = doc.eSocial.evtTabProcesso
    #variaveis
    
    if 'ideEvento' in dir(evtTabProcesso.ideEvento):
        for ideEvento in evtTabProcesso.ideEvento:
            
            if 'tpAmb' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.tpAmb', 
                                                  ideEvento.tpAmb.cdata, 
                                                  1, u'1, 2')
            
            if 'procEmi' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.procEmi', 
                                                  ideEvento.procEmi.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'verProc' in dir(ideEvento):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEvento.verProc', 
                                                  ideEvento.verProc.cdata, 
                                                  1, u'None')
    
    if 'ideEmpregador' in dir(evtTabProcesso.ideEmpregador):
        for ideEmpregador in evtTabProcesso.ideEmpregador:
            
            if 'tpInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.tpInsc', 
                                                  ideEmpregador.tpInsc.cdata, 
                                                  1, u'1, 2, 3, 4, 5')
            
            if 'nrInsc' in dir(ideEmpregador):
                validacoes_lista = validar_campo( validacoes_lista,
                                                  'ideEmpregador.nrInsc', 
                                                  ideEmpregador.nrInsc.cdata, 
                                                  1, u'None')
    
    if 'infoProcesso' in dir(evtTabProcesso.infoProcesso):
        for infoProcesso in evtTabProcesso.infoProcesso:
            
            if 'inclusao' in dir(infoProcesso.inclusao):
                for inclusao in infoProcesso.inclusao:
                    
                    if 'ideProcesso' in dir(inclusao.ideProcesso):
                        for ideProcesso in inclusao.ideProcesso:
                            
                            if 'tpProc' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.tpProc', 
                                                                  ideProcesso.tpProc.cdata, 
                                                                  1, u'1, 2, 3, 4')
                            
                            if 'nrProc' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.nrProc', 
                                                                  ideProcesso.nrProc.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.iniValid', 
                                                                  ideProcesso.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.fimValid', 
                                                                  ideProcesso.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosProc' in dir(inclusao.dadosProc):
                        for dadosProc in inclusao.dadosProc:
                            
                            if 'indAutoria' in dir(dadosProc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosProc.indAutoria', 
                                                                  dadosProc.indAutoria.cdata, 
                                                                  0, u'1, 2')
                            
                            if 'indMatProc' in dir(dadosProc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosProc.indMatProc', 
                                                                  dadosProc.indMatProc.cdata, 
                                                                  1, u'1, 2, 3, 4, 5, 6, 7, 8, 99')
                            
                            if 'observacao' in dir(dadosProc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosProc.observacao', 
                                                                  dadosProc.observacao.cdata, 
                                                                  0, u'None')
                            
                            if 'dadosProcJud' in dir(dadosProc.dadosProcJud):
                                for dadosProcJud in dadosProc.dadosProcJud:
                                    
                                    if 'ufVara' in dir(dadosProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosProcJud.ufVara', 
                                                                          dadosProcJud.ufVara.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codMunic' in dir(dadosProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosProcJud.codMunic', 
                                                                          dadosProcJud.codMunic.cdata, 
                                                                          1, u'None')
                                    
                                    if 'idVara' in dir(dadosProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosProcJud.idVara', 
                                                                          dadosProcJud.idVara.cdata, 
                                                                          1, u'None')
                            
                            if 'infoSusp' in dir(dadosProc.infoSusp):
                                for infoSusp in dadosProc.infoSusp:
                                    
                                    if 'codSusp' in dir(infoSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSusp.codSusp', 
                                                                          infoSusp.codSusp.cdata, 
                                                                          1, u'None')
                                    
                                    if 'indSusp' in dir(infoSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSusp.indSusp', 
                                                                          infoSusp.indSusp.cdata, 
                                                                          1, u'01, 02, 03, 04, 05, 08, 09, 10, 11, 12, 13, 14, 90, 92')
                                    
                                    if 'dtDecisao' in dir(infoSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSusp.dtDecisao', 
                                                                          infoSusp.dtDecisao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'indDeposito' in dir(infoSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSusp.indDeposito', 
                                                                          infoSusp.indDeposito.cdata, 
                                                                          1, u'S, N')
            
            if 'alteracao' in dir(infoProcesso.alteracao):
                for alteracao in infoProcesso.alteracao:
                    
                    if 'ideProcesso' in dir(alteracao.ideProcesso):
                        for ideProcesso in alteracao.ideProcesso:
                            
                            if 'tpProc' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.tpProc', 
                                                                  ideProcesso.tpProc.cdata, 
                                                                  1, u'1, 2, 3, 5')
                            
                            if 'nrProc' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.nrProc', 
                                                                  ideProcesso.nrProc.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.iniValid', 
                                                                  ideProcesso.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.fimValid', 
                                                                  ideProcesso.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosProc' in dir(alteracao.dadosProc):
                        for dadosProc in alteracao.dadosProc:
                            
                            if 'indAutoria' in dir(dadosProc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosProc.indAutoria', 
                                                                  dadosProc.indAutoria.cdata, 
                                                                  0, u'1, 2')
                            
                            if 'indMatProc' in dir(dadosProc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosProc.indMatProc', 
                                                                  dadosProc.indMatProc.cdata, 
                                                                  1, u'1, 2, 3, 4, 5, 6, 7, 8, 99')
                            
                            if 'observacao' in dir(dadosProc):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosProc.observacao', 
                                                                  dadosProc.observacao.cdata, 
                                                                  0, u'None')
                            
                            if 'dadosProcJud' in dir(dadosProc.dadosProcJud):
                                for dadosProcJud in dadosProc.dadosProcJud:
                                    
                                    if 'ufVara' in dir(dadosProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosProcJud.ufVara', 
                                                                          dadosProcJud.ufVara.cdata, 
                                                                          1, u'None')
                                    
                                    if 'codMunic' in dir(dadosProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosProcJud.codMunic', 
                                                                          dadosProcJud.codMunic.cdata, 
                                                                          1, u'None')
                                    
                                    if 'idVara' in dir(dadosProcJud):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'dadosProcJud.idVara', 
                                                                          dadosProcJud.idVara.cdata, 
                                                                          1, u'None')
                            
                            if 'infoSusp' in dir(dadosProc.infoSusp):
                                for infoSusp in dadosProc.infoSusp:
                                    
                                    if 'codSusp' in dir(infoSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSusp.codSusp', 
                                                                          infoSusp.codSusp.cdata, 
                                                                          1, u'None')
                                    
                                    if 'indSusp' in dir(infoSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSusp.indSusp', 
                                                                          infoSusp.indSusp.cdata, 
                                                                          1, u'01, 02, 03, 04, 05, 08, 09, 10, 11, 12, 13, 14, 90, 92')
                                    
                                    if 'dtDecisao' in dir(infoSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSusp.dtDecisao', 
                                                                          infoSusp.dtDecisao.cdata, 
                                                                          1, u'None')
                                    
                                    if 'indDeposito' in dir(infoSusp):
                                        validacoes_lista = validar_campo( validacoes_lista,
                                                                          'infoSusp.indDeposito', 
                                                                          infoSusp.indDeposito.cdata, 
                                                                          1, u'S, N')
                    
                    if 'novaValidade' in dir(alteracao.novaValidade):
                        for novaValidade in alteracao.novaValidade:
                            
                            if 'iniValid' in dir(novaValidade):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'novaValidade.iniValid', 
                                                                  novaValidade.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(novaValidade):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'novaValidade.fimValid', 
                                                                  novaValidade.fimValid.cdata, 
                                                                  0, u'None')
            
            if 'exclusao' in dir(infoProcesso.exclusao):
                for exclusao in infoProcesso.exclusao:
                    
                    if 'ideProcesso' in dir(exclusao.ideProcesso):
                        for ideProcesso in exclusao.ideProcesso:
                            
                            if 'tpProc' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.tpProc', 
                                                                  ideProcesso.tpProc.cdata, 
                                                                  1, u'1, 2, 3, 6')
                            
                            if 'nrProc' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.nrProc', 
                                                                  ideProcesso.nrProc.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.iniValid', 
                                                                  ideProcesso.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideProcesso):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideProcesso.fimValid', 
                                                                  ideProcesso.fimValid.cdata, 
                                                                  0, u'None')
    return validacoes_lista