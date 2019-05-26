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



CHOICES_S1000_CLASSTRIB_ALTERACAO = [

    ('01', u'01 - Empresa  enquadrada  no  regime  de  tributação  Simples  Nacional  com  tributação  previdenciária substituída'),
    ('02', u'02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída'),
    ('03', u'03 - Empresa  enquadrada  no  regime  de  tributação  Simples  Nacional  com  tributação  previdenciária substituída e não substituída'),
    ('04', u'04 - MEI - Micro Empreendedor Individual'),
    ('06', u'06 - Agroindústria'),
    ('07', u'07 - Produtor Rural Pessoa Jurídica'),
    ('08', u'08 - Consórcio Simplificado de Produtores Rurais'),
    ('09', u'09 - Órgão Gestor de Mão de Obra'),
    ('10', u'10 - Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('11', u'11 - Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('13', u'13 - Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91'),
    ('14', u'14 - Sindicatos em geral, exceto aquele classificado no código [10]'),
    ('21', u'21 - Pessoa Física, exceto Segurado Especial'),
    ('22', u'22 - Segurado Especial'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
    
]




CHOICES_S1000_CLASSTRIB_INCLUSAO = [

    ('01', u'01 - Empresa  enquadrada  no  regime  de  tributação  Simples  Nacional  com  tributação  previdenciária substituída'),
    ('02', u'02 - Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída'),
    ('03', u'03 - Empresa  enquadrada  no  regime  de  tributação  Simples  Nacional  com  tributação  previdenciária substituída e não substituída'),
    ('04', u'04 - MEI - Micro Empreendedor Individual'),
    ('06', u'06 - Agroindústria'),
    ('07', u'07 - Produtor Rural Pessoa Jurídica'),
    ('08', u'08 - Consórcio Simplificado de Produtores Rurais'),
    ('09', u'09 - Órgão Gestor de Mão de Obra'),
    ('10', u'10 - Entidade Sindical a que se refere a Lei 12.023/2009'),
    ('11', u'11 - Associação Desportiva que mantém Clube de Futebol Profissional'),
    ('13', u'13 - Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91'),
    ('14', u'14 - Sindicatos em geral, exceto aquele classificado no código [10]'),
    ('21', u'21 - Pessoa Física, exceto Segurado Especial'),
    ('22', u'22 - Segurado Especial'),
    ('60', u'60 - Missão Diplomática ou Repartição Consular de carreira estrangeira'),
    ('70', u'70 - Empresa de que trata o Decreto 5.436/2005'),
    ('80', u'80 - Entidade Beneficente de Assistência Social isenta de contribuições sociais'),
    ('85', u'85 - Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas'),
    ('99', u'99 - Pessoas Jurídicas em Geral'),
    
]




CHOICES_S1000_ESFERAOP_ALTERACAO = [

    (1, u'1 - Federal'),
    (2, u'2 - Estadual ou distrital'),
    (3, u'3 - Municipal.'),
    
]




CHOICES_S1000_ESFERAOP_INCLUSAO = [

    (1, u'1 - Federal'),
    (2, u'2 - Estadual ou distrital'),
    (3, u'3 - Municipal.'),
    
]




CHOICES_S1000_IDEEFR_ALTERACAO = [

    ('N', u'N - Não é EFR.'),
    ('S', u'S - É EFR'),
    
]




CHOICES_S1000_IDEEFR_INCLUSAO = [

    ('N', u'N - Não é EFR.'),
    ('S', u'S - É EFR'),
    
]




CHOICES_S1000_INDACORDOISENMULTA_ALTERACAO = [

    (0, u'0 - Sem acordo'),
    (1, u'1 - Com acordo.'),
    
]




CHOICES_S1000_INDACORDOISENMULTA_INCLUSAO = [

    (0, u'0 - Sem acordo'),
    (1, u'1 - Com acordo.'),
    
]




CHOICES_S1000_INDCONSTR_ALTERACAO = [

    (0, u'0 - Não é Construtora'),
    (1, u'1 - Empresa Construtora.'),
    
]




CHOICES_S1000_INDCONSTR_INCLUSAO = [

    (0, u'0 - Não é Construtora'),
    (1, u'1 - Empresa Construtora.'),
    
]




CHOICES_S1000_INDCOOP_ALTERACAO = [

    (0, u'0 - Não é cooperativa'),
    (1, u'1 - Cooperativa de Trabalho'),
    (2, u'2 - Cooperativa de Produção'),
    (3, u'3 - Outras Cooperativas.'),
    
]




CHOICES_S1000_INDCOOP_INCLUSAO = [

    (0, u'0 - Não é cooperativa'),
    (1, u'1 - Cooperativa de Trabalho'),
    (2, u'2 - Cooperativa de Produção'),
    (3, u'3 - Outras Cooperativas.'),
    
]




CHOICES_S1000_INDDESFOLHA_ALTERACAO = [

    (0, u'0 - Não Aplicável'),
    (1, u'1 - Empresa enquadrada nos art. 7º a 9º da Lei 12.546/2011.'),
    
]




CHOICES_S1000_INDDESFOLHA_INCLUSAO = [

    (0, u'0 - Não Aplicável'),
    (1, u'1 - Empresa enquadrada nos art. 7º a 9º da Lei 12.546/2011.'),
    
]




CHOICES_S1000_INDENTED_ALTERACAO = [

    ('N', u'N - Não'),
    ('S', u'S - Sim.'),
    
]




CHOICES_S1000_INDENTED_INCLUSAO = [

    ('N', u'N - Não'),
    ('S', u'S - Sim.'),
    
]




CHOICES_S1000_INDETT_ALTERACAO = [

    ('N', u'N - Não é Empresa de Trabalho Temporário'),
    ('S', u'S - Empresa de Trabalho Temporário.'),
    
]




CHOICES_S1000_INDETT_INCLUSAO = [

    ('N', u'N - Não é Empresa de Trabalho Temporário'),
    ('S', u'S - Empresa de Trabalho Temporário.'),
    
]




CHOICES_S1000_INDOPCCP_ALTERACAO = [

    (1, u'1 - Sobre a comercialização da sua produção'),
    (2, u'2 - Sobre a folha de pagamento.'),
    
]




CHOICES_S1000_INDOPCCP_INCLUSAO = [

    (1, u'1 - Sobre a comercialização da sua produção'),
    (2, u'2 - Sobre a folha de pagamento.'),
    
]




CHOICES_S1000_INDOPTREGELETRON_ALTERACAO = [

    (0, u'0 - Não optou pelo registro eletrônico de empregados'),
    (1, u'1 - Optou pelo registro eletrônico de empregados.'),
    
]




CHOICES_S1000_INDOPTREGELETRON_INCLUSAO = [

    (0, u'0 - Não optou pelo registro eletrônico de empregados'),
    (1, u'1 - Optou pelo registro eletrônico de empregados.'),
    
]




CHOICES_S1000_INDRPPS_ALTERACAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S1000_INDRPPS_INCLUSAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S1000_INDSITPF_ALTERACAO = [

    (0, u'0 - Situação Normal'),
    (1, u'1 - Encerramento de espólio'),
    (2, u'2 - Saída do país em caráter permanente.'),
    
]




CHOICES_S1000_INDSITPF_INCLUSAO = [

    (0, u'0 - Situação Normal'),
    (1, u'1 - Encerramento de espólio'),
    (2, u'2 - Saída do país em caráter permanente.'),
    
]




CHOICES_S1000_INDSITPJ_ALTERACAO = [

    (0, u'0 - Situação Normal'),
    (1, u'1 - Extinção'),
    (2, u'2 - Fusão'),
    (3, u'3 - Cisão'),
    (4, u'4 - Incorporação.'),
    
]




CHOICES_S1000_INDSITPJ_INCLUSAO = [

    (0, u'0 - Situação Normal'),
    (1, u'1 - Extinção'),
    (2, u'2 - Fusão'),
    (3, u'3 - Cisão'),
    (4, u'4 - Incorporação.'),
    
]




CHOICES_S1000_INDUGRPPS_ALTERACAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S1000_INDUGRPPS_INCLUSAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S1000_PODEROP_ALTERACAO = [

    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (4, u'4 - Ministério Público'),
    (5, u'5 - Tribunal de Contas'),
    (6, u'6 - Defensoria Pública.'),
    
]




CHOICES_S1000_PODEROP_INCLUSAO = [

    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (4, u'4 - Ministério Público'),
    (5, u'5 - Tribunal de Contas'),
    (6, u'6 - Defensoria Pública.'),
    
]




CHOICES_S1000_PREVCOMP_ALTERACAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S1000_PREVCOMP_INCLUSAO = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S1000_SUBTETO_ALTERACAO = [

    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (9, u'9 - Todos os poderes.'),
    
]




CHOICES_S1000_SUBTETO_INCLUSAO = [

    (1, u'1 - Executivo'),
    (2, u'2 - Judiciário'),
    (3, u'3 - Legislativo'),
    (9, u'9 - Todos os poderes.'),
    
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




PERIODOS = [

    ('2017-01', u'Janeiro/2017'),
    ('2017-02', u'Fevereiro/2017'),
    ('2017-03', u'Março/2017'),
    ('2017-04', u'Abril/2017'),
    ('2017-05', u'Maio/2017'),
    ('2017-06', u'Junho/2017'),
    ('2017-07', u'Julho/2017'),
    ('2017-08', u'Agosto/2017'),
    ('2017-09', u'Setembro/2017'),
    ('2017-10', u'Outubro/2017'),
    ('2017-11', u'Novembro/2017'),
    ('2017-12', u'Dezembro/2017'),
    ('2018-01', u'Janeiro/2018'),
    ('2018-02', u'Fevereiro/2018'),
    ('2018-03', u'Março/2018'),
    ('2018-04', u'Abril/2018'),
    ('2018-05', u'Maio/2018'),
    ('2018-06', u'Junho/2018'),
    ('2018-07', u'Julho/2018'),
    ('2018-08', u'Agosto/2018'),
    ('2018-09', u'Setembro/2018'),
    ('2018-10', u'Outubro/2018'),
    ('2018-11', u'Novembro/2018'),
    ('2018-12', u'Dezembro/2018'),
    ('2019-01', u'Janeiro/2019'),
    ('2019-02', u'Fevereiro/2019'),
    ('2019-03', u'Março/2019'),
    ('2019-04', u'Abril/2019'),
    ('2019-05', u'Maio/2019'),
    ('2019-06', u'Junho/2019'),
    ('2019-07', u'Julho/2019'),
    ('2019-08', u'Agosto/2019'),
    ('2019-09', u'Setembro/2019'),
    ('2019-10', u'Outubro/2019'),
    ('2019-11', u'Novembro/2019'),
    ('2019-12', u'Dezembro/2019'),
    
]



