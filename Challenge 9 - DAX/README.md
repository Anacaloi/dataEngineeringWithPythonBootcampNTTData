# Desafio de Projeto: Modelo de Dados Star Schema

Este projeto é parte do desafio de construção de um modelo de dados utilizando a tabela `Financial Sample` como base para criar tabelas dimensão e fato em um esquema estrela (star schema). A abordagem tem como objetivo fornecer insights organizados e de fácil acesso para análises financeiras.

## Objetivo do Projeto

Criar um modelo de dados estruturado no formato star schema, que envolve a construção de tabelas de dimensão e fato com base em uma tabela única (`Financial Sample`). O projeto visa a criação de uma estrutura para armazenar e analisar informações de vendas, produtos, descontos, calendário e demais detalhes, conforme descrito abaixo.

## Estrutura do Projeto

O projeto consiste nas seguintes tabelas:

- **Financials_origem**: Backup da tabela original, em modo oculto.
- **D_Produtos**: Dimensão com informações agregadas de produtos.
  - **Campos**: `ID_produto`, `Produto`, `Média de Unidades Vendidas`, `Médias do valor de vendas`, `Mediana do valor de vendas`, `Valor máximo de Venda`, `Valor mínimo de Venda`
- **D_Produtos_Detalhes**: Dimensão com detalhes adicionais de produtos.
  - **Campos**: `ID_produtos`, `Discount Band`, `Sale Price`, `Units Sold`, `Manufacturing Price`
- **D_Descontos**: Dimensão com detalhes de descontos.
  - **Campos**: `ID_produto`, `Discount`, `Discount Band`
- **D_Detalhes**: Tabela auxiliar contendo informações adicionais sobre vendas, conforme necessário.
- **D_Calendário**: Dimensão de calendário, criada com a função `DAX CALENDAR()`.
- **F_Vendas**: Tabela fato com informações de vendas.
  - **Campos**: `SK_ID`, `ID_Produto`, `Produto`, `Units Sold`, `Sales Price`, `Discount Band`, `Segment`, `Country`, `Sellers`, `Profit`, `Date`

## Etapas de Construção do Projeto

1. **Criação da Tabela de Backup**:

   - **Tabela Financials_origem**: A tabela original foi copiada e oculta para servir como backup.

2. **Criação das Tabelas Dimensão**:

   - **D_Produtos**: Criada com base em agregações, como média, mediana, máximo e mínimo de vendas.
   - **D_Produtos_Detalhes**: Contém detalhes de produtos, como preço de fabricação e unidades vendidas.
   - **D_Descontos**: Armazena dados de desconto e band de desconto.
   - **D_Calendário**: Gerada via `DAX CALENDAR()` para uso nas análises temporais.
   - **D_Detalhes**: Criada para armazenar informações adicionais sobre vendas não contempladas nas demais tabelas.

3. **Criação da Tabela Fato**:

   - **F_Vendas**: Contém as informações de vendas e é conectada a todas as tabelas de dimensão para completar o star schema.

4. **Transformações e Cálculos DAX**:
   - Foram utilizadas funções DAX para agregações e filtros, além de condicional para criação de índices e organização de colunas.

## Imagem do Esquema em Estrela

![Star Schema Diagram](link-para-imagem)

## Funcionalidades e DAX Utilizadas

- **CALENDAR()**: Criação da tabela de calendário para análises temporais.
- **Agregações**: Média, mediana, máximo e mínimo das vendas para criar agregados em `D_Produtos`.
- **Condicionais**: Condicional para calcular índices de produto e categorizações diversas.

## Considerações Finais

Este projeto foi desenvolvido para aprimorar as habilidades em modelagem de dados e organização de dados em um esquema estrela, com o objetivo de facilitar a análise e interpretação dos dados financeiros. A estrutura organizada permite que outras pessoas revisem o projeto e compreendam as decisões de modelagem tomadas.

## Como Contribuir

Sinta-se à vontade para abrir um _pull request_ com sugestões ou melhorias. Este repositório também pode servir como portfólio para interessados em ciência de dados e análises financeiras.
