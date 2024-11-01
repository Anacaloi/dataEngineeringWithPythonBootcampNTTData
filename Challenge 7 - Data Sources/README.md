# Integração de MySQL no Azure com Power BI

## Descrição do Projeto

Este projeto consiste na criação de uma instância do MySQL Server na nuvem, seguida pela criação e inserção de dados em tabelas usando o Azure Data Studio e, finalmente, na conexão e importação dessas tabelas no Power BI para análise e visualização de dados.

## Passos do Projeto

### 1. Criação da Instância MySQL Server na Nuvem

- Criação de um recurso de **Banco de Dados do Azure para MySQL** no [Portal do Azure](https://portal.azure.com) e configuração da instância conforme necessário.
  ![instance](https://github.com/Anacaloi/dataEngineeringWithPythonBootcampNTTData/blob/main/Challenge%207%20-%20Data%20Sources/img/instance.png)

### 2. Criação e Inserção de Dados nas Tabelas

- Instalação do **Azure Data Studio** e conexão com a instância MySQL.
- Criação das tabelas e inserção dos dados.

```sql
-- Recriar o esquema
CREATE SCHEMA azure_company;
USE azure_company;

-- Criar as tabelas sem constraints

-- Tabela "employee"
CREATE TABLE employee (
    Fname VARCHAR(15) NOT NULL,
    Minit CHAR,
    Lname VARCHAR(15) NOT NULL,
    Ssn CHAR(9) NOT NULL,
    Bdate DATE,
    Address VARCHAR(30),
    Sex CHAR,
    Salary DECIMAL(10,2),
    Super_ssn CHAR(9),
    Dno INT NOT NULL
);

-- Tabela "departament"
CREATE TABLE departament (
    Dname VARCHAR(15) NOT NULL,
    Dnumber INT NOT NULL,
    Mgr_ssn CHAR(9) NOT NULL,
    Mgr_start_date DATE,
    Dept_create_date DATE
);

-- Tabela "dept_locations"
CREATE TABLE dept_locations (
    Dnumber INT NOT NULL,
    Dlocation VARCHAR(15) NOT NULL
);

-- Tabela "project"
CREATE TABLE project (
    Pname VARCHAR(15) NOT NULL,
    Pnumber INT NOT NULL,
    Plocation VARCHAR(15),
    Dnum INT NOT NULL
);

-- Tabela "works_on"
CREATE TABLE works_on (
    Essn CHAR(9) NOT NULL,
    Pno INT NOT NULL,
    Hours DECIMAL(3,1) NOT NULL
);

-- Tabela "dependent"
CREATE TABLE dependent (
    Essn CHAR(9) NOT NULL,
    Dependent_name VARCHAR(15) NOT NULL,
    Sex CHAR,
    Bdate DATE,
    Relationship VARCHAR(8)
);
```

### 3. Conexão e Importação de Tabelas no Power BI

- Importação dos dados no **Power BI Desktop** no caminho **Obter Dados** > **Banco de Dados** > **MySQL**.
  ![import](https://github.com/Anacaloi/dataEngineeringWithPythonBootcampNTTData/blob/main/Challenge%207%20-%20Data%20Sources/img/import.png)
  ![schema](https://github.com/Anacaloi/dataEngineeringWithPythonBootcampNTTData/blob/main/Challenge%207%20-%20Data%20Sources/img/schema.png)

## Referências

- [Documentação do Azure MySQL](https://docs.microsoft.com/pt-br/azure/mysql/)
- [Documentação do Power BI](https://docs.microsoft.com/pt-br/power-bi/)
