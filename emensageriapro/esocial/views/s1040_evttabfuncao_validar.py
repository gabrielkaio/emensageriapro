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


def validacoes_s1040_evttabfuncao(arquivo):
    from emensageriapro.mensageiro.functions.funcoes_validacoes import validar_campo
    import untangle
    xml = ler_arquivo(arquivo).replace("s:", "")
    doc = untangle.parse(xml)
    validacoes_lista = []
    xmlns = doc.eSocial['xmlns'].split('/')
    evtTabFuncao = doc.eSocial.evtTabFuncao
    #variaveis
    
    if 'ideEvento' in dir(evtTabFuncao.ideEvento):
        for ideEvento in evtTabFuncao.ideEvento:
            
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
    
    if 'ideEmpregador' in dir(evtTabFuncao.ideEmpregador):
        for ideEmpregador in evtTabFuncao.ideEmpregador:
            
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
    
    if 'infoFuncao' in dir(evtTabFuncao.infoFuncao):
        for infoFuncao in evtTabFuncao.infoFuncao:
            
            if 'inclusao' in dir(infoFuncao.inclusao):
                for inclusao in infoFuncao.inclusao:
                    
                    if 'ideFuncao' in dir(inclusao.ideFuncao):
                        for ideFuncao in inclusao.ideFuncao:
                            
                            if 'codFuncao' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.codFuncao', 
                                                                  ideFuncao.codFuncao.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.iniValid', 
                                                                  ideFuncao.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.fimValid', 
                                                                  ideFuncao.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosFuncao' in dir(inclusao.dadosFuncao):
                        for dadosFuncao in inclusao.dadosFuncao:
                            
                            if 'dscFuncao' in dir(dadosFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosFuncao.dscFuncao', 
                                                                  dadosFuncao.dscFuncao.cdata, 
                                                                  1, u'None')
                            
                            if 'codCBO' in dir(dadosFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosFuncao.codCBO', 
                                                                  dadosFuncao.codCBO.cdata, 
                                                                  1, u'None')
            
            if 'alteracao' in dir(infoFuncao.alteracao):
                for alteracao in infoFuncao.alteracao:
                    
                    if 'ideFuncao' in dir(alteracao.ideFuncao):
                        for ideFuncao in alteracao.ideFuncao:
                            
                            if 'codFuncao' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.codFuncao', 
                                                                  ideFuncao.codFuncao.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.iniValid', 
                                                                  ideFuncao.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.fimValid', 
                                                                  ideFuncao.fimValid.cdata, 
                                                                  0, u'None')
                    
                    if 'dadosFuncao' in dir(alteracao.dadosFuncao):
                        for dadosFuncao in alteracao.dadosFuncao:
                            
                            if 'dscFuncao' in dir(dadosFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosFuncao.dscFuncao', 
                                                                  dadosFuncao.dscFuncao.cdata, 
                                                                  1, u'None')
                            
                            if 'codCBO' in dir(dadosFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'dadosFuncao.codCBO', 
                                                                  dadosFuncao.codCBO.cdata, 
                                                                  1, u'None')
                    
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
            
            if 'exclusao' in dir(infoFuncao.exclusao):
                for exclusao in infoFuncao.exclusao:
                    
                    if 'ideFuncao' in dir(exclusao.ideFuncao):
                        for ideFuncao in exclusao.ideFuncao:
                            
                            if 'codFuncao' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.codFuncao', 
                                                                  ideFuncao.codFuncao.cdata, 
                                                                  1, u'None')
                            
                            if 'iniValid' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.iniValid', 
                                                                  ideFuncao.iniValid.cdata, 
                                                                  1, u'None')
                            
                            if 'fimValid' in dir(ideFuncao):
                                validacoes_lista = validar_campo( validacoes_lista,
                                                                  'ideFuncao.fimValid', 
                                                                  ideFuncao.fimValid.cdata, 
                                                                  0, u'None')
    return validacoes_lista