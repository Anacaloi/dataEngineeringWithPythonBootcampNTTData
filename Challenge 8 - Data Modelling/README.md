# Projeto de Modelagem Dimensional para Análise de Professores, Cursos e Disciplinas

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um modelo dimensional utilizando o esquema estrela (Star Schema) para análise dos dados dos professores, cursos ministrados e disciplinas oferecidas em uma instituição de ensino. O foco principal da análise é o desempenho e as atividades dos professores, permitindo obter insights detalhados sobre a atuação dos docentes em diversos cursos e departamentos.

## Estrutura do Projeto

### 1. Objetivo

Criar um modelo dimensional baseado em um esquema estrela com as seguintes características:

- **Tabela Fato**: Centralizar as métricas e relacionamentos necessários para a análise dos dados dos professores.
- **Tabelas Dimensão**: Incluir informações adicionais sobre professores, cursos, departamentos, disciplinas e datas.
- **Dimensão de Data**: Adicionar uma tabela de datas para facilitar a análise temporal.

### 2. Diagrama do Modelo de Dados

**Esquema Estrela**

![Diagrama Esquema Estrela](https://github.com/Anacaloi/dataEngineeringWithPythonBootcampNTTData/blob/main/Challenge%208%20-%20Data%20Modelling/img/starSchema.png)

### 3. Estrutura das Tabelas

#### Tabela Fato: `Fato_ProfessorCurso`

| Coluna              | Tipo    | Descrição                                              |
| ------------------- | ------- | ------------------------------------------------------ |
| idProfessor         | INT     | Chave estrangeira para identificar o professor         |
| idCurso             | INT     | Chave estrangeira para identificar o curso             |
| idDepartamento      | INT     | Chave estrangeira para identificar o departamento      |
| idData              | Date    | Data de oferta da disciplina/curso                     |
| quantidade_de_aulas | INT     | Número de aulas ministradas pelo professor             |
| carga_horaria       | INT     | Carga horária total ministrada pelo professor no curso |
| salario_professor   | DECIMAL | Salário do professor                                   |

#### Dimensão Professor: `Dim_Professor`

| Coluna         | Tipo    | Descrição                        |
| -------------- | ------- | -------------------------------- |
| idProfessor    | INT     | Identificador único do professor |
| nome_professor | VARCHAR | Nome do professor                |
| idDepartamento | INT     | Departamento do professor        |
| titulação      | VARCHAR | Titulação acadêmica do professor |

#### Dimensão Curso: `Dim_Curso`

| Coluna         | Tipo    | Descrição                     |
| -------------- | ------- | ----------------------------- |
| idCurso        | INT     | Identificador único do curso  |
| nome_curso     | VARCHAR | Nome do curso                 |
| carga_horaria  | INT     | Carga horária do curso        |
| idDepartamento | INT     | Identificador do departamento |

#### Dimensão Departamento: `Dim_Departamento`

| Coluna            | Tipo    | Descrição                             |
| ----------------- | ------- | ------------------------------------- |
| idDepartamento    | INT     | Identificador único do departamento   |
| nome_departamento | VARCHAR | Nome do departamento                  |
| campus            | VARCHAR | Campus onde o departamento está local |
| idProfessor_chefe | INT     | Identificador do professor chefe      |

#### Dimensão Disciplina: `Dim_Disciplina`

| Coluna          | Tipo    | Descrição                         |
| --------------- | ------- | --------------------------------- |
| idDisciplina    | INT     | Identificador único da disciplina |
| nome_disciplina | VARCHAR | Nome da disciplina                |
| carga_horaria   | INT     | Carga horária total da disciplina |
| idCurso         | INT     | Identificador do curso            |

#### Dimensão Data: `Dim_Data`

| Coluna          | Tipo    | Descrição                            |
| --------------- | ------- | ------------------------------------ |
| idData          | Date    | Data única                           |
| ano             | INT     | Ano                                  |
| mes             | INT     | Mês                                  |
| nome_mes        | VARCHAR | Nome do mês                          |
| trimestre       | INT     | Trimestre do ano                     |
| ano_mes         | VARCHAR | Ano e mês no formato `YYYY-MM`       |
| dia_semana      | INT     | Dia da semana (1=Segunda, 7=Domingo) |
| nome_dia_semana | VARCHAR | Nome do dia da semana                |

### 4. Relacionamentos do Modelo

- `Fato_ProfessorCurso` está ligado às tabelas de dimensão `Dim_Professor`, `Dim_Curso`, `Dim_Departamento`, `Dim_Disciplina` e `Dim_Data` pelas respectivas chaves estrangeiras.
- A tabela `Dim_Data` permite a análise temporal, enquanto `Dim_Professor`, `Dim_Curso`, `Dim_Departamento` e `Dim_Disciplina` detalham a atuação dos professores nos cursos e disciplinas.

### 5. Dados Fictícios para Testes

Para validação e testes do modelo, foram gerados dados fictícios para cada tabela. Os dados representam uma amostra genérica das atividades dos professores em seus respectivos cursos e disciplinas, permitindo análises de carga horária, distribuição dos cursos por departamentos e desempenho por período.

### 6. Ferramentas e Linguagens Utilizadas

- **Power BI Desktop**: Criação do modelo de dados, geração de visualizações e análises.
- **DAX**: Criação da dimensão de data e medidas no Power BI.
- **Power Query Editor**: Inserção e transformação de dados fictícios.

### 7. Possíveis Expansões

- Adicionar métricas de desempenho dos professores, como avaliação de aulas.
- Incluir uma tabela fato secundária para registrar mais detalhes das aulas, como presença de alunos e notas.
- Expandir a tabela `Dim_Data` para análises sazonais mais detalhadas.

## Como Usar o Projeto

1. Abra o arquivo `.pbix` no Power BI Desktop.
2. Visualize o modelo de dados para entender os relacionamentos entre as tabelas.
3. Utilize as visualizações sugeridas para análise de desempenho de professores e cursos.
4. Teste novas análises e dashboards conforme as métricas desejadas.
