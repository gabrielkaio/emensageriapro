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



CHOICES_S2200_CASADOBR = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_CATEGORIACNH = [

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




CHOICES_S2200_CLASSTRABESTRANG = [

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




CHOICES_S2200_CODMOTAFAST = [

    ('01', u'01 - Acidente/Doença do trabalho'),
    ('03', u'03 - Acidente/Doença não relacionada ao trabalho'),
    ('05', u'05 - Afastamento/licença prevista em regime próprio (estatuto), sem remuneração'),
    ('06', u'06 - Aposentadoria por invalidez'),
    ('07', u'07 - Acompanhamento - Licença para acompanhamento de membro da família enfermo'),
    ('08', u'08 - Afastamento do empregado para participar de atividade do Conselho Curador do FGTS - art. 65, §6º, Dec. 99.684/90 (Regulamento do FGTS)'),
    ('10', u'10 - Afastamento/licença prevista em regime próprio (estatuto), com remuneração'),
    ('11', u'11 - Cárcere'),
    ('12', u'12 - Cargo Eletivo - Candidato a cargo eletivo - Lei 7.664/1988. art. 25°, parágrafo único - Celetistas em geral'),
    ('13', u'13 - Cargo Eletivo - Candidato a cargo eletivo - Lei Complementar 64/1990. art. 1°, inciso II, alínea “l” - Servidor público, estatutário ou não, dos órgãos ou entidades da Administração Direta ou Indireta da União, dos Estados, do Distrito Federal, dos Municípios e dos Territórios, inclusive das fundações mantidas pelo Poder Público'),
    ('14', u'14 - Cessão / Requisição'),
    ('15', u'15 - Gozo de férias ou recesso - Afastamento temporário para o gozo de férias ou recesso'),
    ('16', u'16 - Licença remunerada - Lei, liberalidade da empresa ou Acordo/Convenção Coletiva de Trabalho'),
    ('17', u'17 - Licença Maternidade - 120 dias e suas prorrogações/antecipações, inclusive para o cônjuge sobrevivente'),
    ('17', u'17 - Licença Maternidade - 120 dias, inclusive para o cônjuge sobrevivente'),
    ('18', u'18 - Licença Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidadã), inclusive para o cônjuge sobrevivente'),
    ('19', u'19 - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso'),
    ('20', u'20 - Licença Maternidade - Afastamento temporário por motivo de licença- maternidade decorrente de adoção ou guarda judicial de criança, inclusive para o cônjuge sobrevivente'),
    ('21', u'21 - Licença não remunerada ou Sem Vencimento'),
    ('22', u'22 - Mandato Eleitoral - Afastamento temporário para o exercício de mandato eleitoral, sem remuneração'),
    ('23', u'23 - Mandato Eleitoral - Afastamento temporário para o exercício de mandato eleitoral, com remuneração'),
    ('24', u'24 - Mandato Sindical - Afastamento temporário para exercício de mandato sindical'),
    ('25', u'25 - Mulher vítima de violência - Lei 11.340/2006 - art. 9º §2o, II - Lei Maria da Penha'),
    ('26', u'26 - Participação de empregado no Conselho Nacional de Previdência Social-CNPS (art. 3º, Lei 8.213/1991)'),
    ('27', u'27 - Qualificação - Afastamento por suspensão do contrato de acordo com o art 476-A da CLT'),
    ('28', u'28 - Representante Sindical - Afastamento pelo tempo que se fizer necessário, quando, na qualidade de representante de entidade sindical, estiver participando de reunião oficial de organismo internacional do qual o Brasil seja membro'),
    ('29', u'29 - Serviço Militar - Afastamento temporário para prestar serviço militar obrigatório'),
    ('30', u'30 - Suspensão disciplinar - CLT, art. 474'),
    ('31', u'31 - Servidor Público em Disponibilidade'),
    ('33', u'33 - Licença Maternidade - de 180 dias, Lei 13.301/2016'),
    ('34', u'34 - Inatividade do trabalhador avulso (portuário ou não portuário) por período superior a 90 dias'),
    ('35', u'35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico'),
    
]




CHOICES_S2200_DEFAUDITIVA = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_DEFFISICA = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_DEFINTELECTUAL = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_DEFMENTAL = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_DEFVISUAL = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_DEPFINSPREV = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_DEPIRRF = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_DEPSF = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_DIA = [

    (1, u'1 - Segunda-Feira'),
    (2, u'2 - Terça-Feira'),
    (3, u'3 - Quarta-Feira'),
    (4, u'4 - Quinta-Feira'),
    (5, u'5 - Sexta-Feira'),
    (6, u'6 - Sábado'),
    (7, u'7 - Domingo'),
    (8, u'8 - Dia variável.'),
    
]




CHOICES_S2200_FILHOSBR = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_HIPLEG = [

    (1, u'1 - Necessidade de substituição transitória de pessoal permanente'),
    (2, u'2 - Demanda complementar de serviços.'),
    
]




CHOICES_S2200_INCTRAB = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_INDABONOPERM = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_INDADMISSAO = [

    (1, u'1 - Normal'),
    (2, u'2 - Decorrente de Ação Fiscal'),
    (3, u'3 - Decorrente de Decisão Judicial.'),
    
]




CHOICES_S2200_INDPARCREMUN = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_INDPROVIM = [

    (1, u'1 - Normal'),
    (2, u'2 - Decorrente de Decisão Judicial.'),
    
]




CHOICES_S2200_INDTETORGPS = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_INFOCOTA = [

    ('N', u'N - Não'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_NATATIVIDADE = [

    (1, u'1 - Trabalho Urbano'),
    (2, u'2 - Trabalho Rural.'),
    
]




CHOICES_S2200_OPCFGTS = [

    (1, u'1 - Optante'),
    (2, u'2 - Não Optante.'),
    
]




CHOICES_S2200_REABREADAP = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
]




CHOICES_S2200_SEXODEP = [

    ('F', u'F - Feminino.'),
    ('M', u'M - Masculino'),
    
]




CHOICES_S2200_TMPPARC = [

    (0, u'0 - Não é contrato em tempo parcial'),
    (1, u'1 - Limitado a 25 horas semanais'),
    (2, u'2 - Limitado a 30 horas semanais'),
    (3, u'3 - Limitado a 26 horas semanais.'),
    
]




CHOICES_S2200_TPADMISSAO = [

    (1, u'1 - Admissão'),
    (2, u'2 - Transferência de empresa do mesmo grupo econômico'),
    (3, u'3 - Transferência de empresa consorciada ou de consórcio'),
    (4, u'4 - Transferência por motivo de sucessão, incorporação, cisão ou fusão'),
    (5, u'5 - Transferência do empregado doméstico para outro representante da mesma unidade familiar'),
    (6, u'6 - Mudança de CPF.'),
    
]




CHOICES_S2200_TPDEP = [

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




CHOICES_S2200_TPINCLCONTR = [

    (1, u'1 - Locais sem filiais'),
    (2, u'2 - Estudo de mercado'),
    (3, u'3 - Contratação superior a 3 meses.'),
    
]




CHOICES_S2200_TPINSC = [

    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (5, u'5 - CGC'),
    
]




CHOICES_S2200_TPINSCANT = [

    (1, u'1 - CNPJ'),
    (2, u'2 - CPF'),
    (3, u'3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)'),
    (4, u'4 - CNO (Cadastro Nacional de Obra)'),
    (5, u'5 - CGC'),
    
]




CHOICES_S2200_TPJORNADA = [

    (1, u'1 - Jornada com horário diário e folga fixos'),
    (2, u'2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)'),
    (3, u'3 - Jornada com horário diário fixo e folga variável'),
    (9, u'9 - Demais tipos de jornada.'),
    
]




CHOICES_S2200_TPPLANRP = [

    (1, u'1 - Plano previdenciário ou único'),
    (2, u'2 - Plano financeiro.'),
    
]




CHOICES_S2200_TPPROV = [

    (1, u'1 - Nomeação em cargo efetivo'),
    (2, u'2 - Nomeação em cargo em comissão'),
    (3, u'3 - Incorporação (militar)'),
    (4, u'4 - Matrícula (militar)'),
    (5, u'5 - Reinclusão (militar)'),
    (6, u'6 - Diplomação'),
    (99, u'99 - Outros não relacionados acima.'),
    
]




CHOICES_S2200_TPREGJOR = [

    (1, u'1 - Submetidos a Horário de Trabalho (Cap. II da CLT)'),
    (2, u'2 - Atividade Externa especificada no Inciso I do Art. 62 da CLT'),
    (3, u'3 - Funções especificadas no Inciso II do Art. 62 da CLT'),
    (4, u'4 - Teletrabalho, previsto no Inciso III do Art. 62 da CLT.'),
    
]




CHOICES_S2200_TRABAPOSENT = [

    ('N', u'N - Não.'),
    ('S', u'S - Sim'),
    
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



