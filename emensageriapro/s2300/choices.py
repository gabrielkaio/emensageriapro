#coding:utf-8


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



CHOICES_ESOCIALDEPENDENTESTIPOS = [

    ('01', u'01 - Cônjuge'),
    ('02', u'02 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável'),
    ('03', u'03 - Filho(a) ou enteado(a)'),
    ('04', u'04 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau'),
    ('06', u'06 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'),
    ('07', u'07 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, universitário(a) ou cursando escola técnica de 2° grau, do(a) qual detenha a guarda judicial'),
    ('09', u'09 - Pais, avós e bisavós'),
    ('10', u'10 - Menor pobre do qual detenha a guarda judicial'),
    ('11', u'11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'),
    ('12', u'12 - Ex-cônjuge'),
    ('99', u'99 - Agregado/Outros'),

]




CHOICES_S2300_CASADOBR = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_CATEGORIACNH = [

    ('A', u'A'),
    ('AB', u'AB'),
    ('AC', u'AC'),
    ('AD', u'AD'),
    ('AE', u'AE'),
    ('B', u'B'),
    ('C', u'C'),
    ('D', u'D'),
    ('E', u'E'),

]




CHOICES_S2300_CLASSTRABESTRANG = [

    (1, u'1 - Visto permanente'),
    (10, u'10 - Beneficiado pelo acordo entre países do Mercosul'),
    (11, u'11 - Dependente de agente diplomático e/ou consular de países que mantém convênio de reciprocidade para o exercício de atividade remunerada no Brasil'),
    (12, u'12 - Beneficiado pelo Tratado de Amizade, Cooperação e Consulta entre a República Federativa do Brasil e a República Portuguesa.'),
    (2, u'2 - Visto temporário'),
    (3, u'3 - Asilado'),
    (4, u'4 - Refugiado'),
    (5, u'5 - Solicitante de Refúgio'),
    (6, u'6 - Residente fora do Brasil'),
    (7, u'7 - Deficiente físico e com mais de 51 anos'),
    (8, u'8 - Com residência provisória e anistiado, em situação irregular'),
    (9, u'9 - Permanência no Brasil em razão de filhos ou cônjuge brasileiros'),

]




CHOICES_S2300_DEFAUDITIVA = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_DEFFISICA = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_DEFINTELECTUAL = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_DEFMENTAL = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_DEFVISUAL = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_DEPFINSPREV = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_DEPIRRF = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_DEPSF = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_FILHOSBR = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_INCTRAB = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_INDREMUNCARGO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_INFONUS = [

    (1, u'1 - Ônus do Cedente'),
    (2, u'2 - Ônus do Cessionário'),
    (3, u'3 - Ônus do Cedente e Cessionário.'),

]




CHOICES_S2300_NATESTAGIO = [

    ('N', u'N - Não Obrigatório.'),
    ('O', u'O - Obrigatório'),

]




CHOICES_S2300_NIVESTAGIO = [

    (1, u'1 - Fundamental'),
    (2, u'2 - Médio'),
    (3, u'3 - Formação Profissional'),
    (4, u'4 - Superior'),
    (8, u'8 - Especial'),
    (9, u'9 - Mãe social. (Lei 7644, de 1987).'),

]




CHOICES_S2300_OPCFGTS = [

    (1, u'1 - Optante'),
    (2, u'2 - Não Optante.'),

]




CHOICES_S2300_REABREADAP = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),

]




CHOICES_S2300_SEXODEP = [

    ('F', u'F - Feminino.'),
    ('M', u'M - Masculino'),

]




CHOICES_S2300_TPREGPREV = [

    (1, u'1 - Regime Geral da Previdência Social - RGPS'),
    (2, u'2 - Regime Próprio de Previdência Social - RPPS'),
    (3, u'3 - Regime de Previdência Social no Exterior.'),

]




CHOICES_S2300_TPREGTRAB = [

    (1, u'1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas'),
    (2, u'2 - Estatutário.'),

]




CHOICES_S2300_UNDSALFIXO = [

    (1, u'1 - Por Hora'),
    (2, u'2 - Por Dia'),
    (3, u'3 - Por Semana'),
    (4, u'4 - Por Quinzena'),
    (5, u'5 - Por Mês'),
    (6, u'6 - Por Tarefa'),
    (7, u'7 - Não aplicável - salário exclusivamente variável.'),

]




ESTADOS = [

    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AM', u'Amazonas'),
    ('AP', u'Amapá'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MG', u'Minas Gerais'),
    ('MS', u'Mato Grosso do Sul'),
    ('MT', u'Mato Grosso'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('PR', u'Paraná'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('RS', u'Rio Grande do Sul'),
    ('SC', u'Santa Catarina'),
    ('SE', u'Sergipe'),
    ('SP', u'São Paulo'),
    ('TO', u'Tocantins'),

]



