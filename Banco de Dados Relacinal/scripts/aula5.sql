-- 16/09/2025
create database joins;
use joins;
 
create table departamentos(
	id int primary key auto_increment,
    nome varchar(80)
);
 
create table pessoas(
	id int primary key auto_increment,
    nome varchar(100),
    id_gestor int null,
    dept_id int null,
    constraint fk_pessoas_dept foreign key(dept_id) references departamentos(id),
    constraint fk_pessoas_gestor foreign key(id_gestor) references pessoas(id)
);
 
create table tarefas(
	id int primary key auto_increment,
    descricao varchar(120),
    status enum("Pendente","Em andamento","Concluída") default "Pendente",
    pessoa_id int null,
    constraint fk_tarefas_pessoa foreign key (pessoa_id) references pessoas(id)
);
 
create table projetos(
	id int primary key auto_increment,
    nome varchar(120)
);
 
create table alocacoes(
	id int primary key auto_increment, 
    pessoa_id int,
    projeto_id int,
    horas_semana tinyint,
    constraint fk_aloc_pessoa foreign key (pessoa_id) references pessoas(id),
    constraint fk_aloc_projeto foreign key (projeto_id) references projetos(id)
);
 
# Inserção de dados
insert into departamentos(nome) values("Ti"),("Financeiro"),("RH");
 
insert into pessoas (nome, id_gestor, dept_id) values 
("Ana", null, 1),
("Bruno", 1, 1),
("Carla", 1, 1),
("Diego",2, null),
("Eduardo", null, 3),
("Fernanda",5,2);
 
insert into tarefas (descricao, status, pessoa_id) values
("Levantar requisitos","Concluída",2),
("Desenhar protótipo","Em andamento",3),
("Configurar servidor","Pendente",null),
("Reunião com cliente","Concluída",1),
("Aprovar orçamento","Pendente",null);
 
insert into projetos (nome) values 
("Projeto Alfa"),
("Projeto Beta"),
("Projeto Gama");
 
insert into alocacoes(pessoa_id, projeto_id, horas_semana) values
(1,1,10),
(2,1,20),
(3,2,15);

-- inner join
/*
Pessoas com Tarefas atribuidas
(somente quem tem correspondencia em ambas as tabelas)
*/
select * from tarefas;

-- inner joint
select 
pessoas.id, 
pessoas.nome, 
tarefas.id,
tarefas.descricao, 
tarefas.status 
from pessoas inner join tarefas on tarefas.id = pessoas.id;

-- 17/09/2025


-- Equi join
/*
- Definição: É um INNER JOIN em que a condição de junção usa apenas igualdade (=).
- Observação: Todo INNER JOIN padrão é u EQUI JOIN, mas o termo é usado para diferenciar de joins
que usam outros operadores (>, <, !=, etc).
- Exemplo prático: Pessoas ligadas a tarefas pela chave estrangeira (igualdade de ID).

invés de usar:
from pessoas inner join tarefas on tarefas.id = pessoas.id;
você usaria USING, desse modo - from pessoas inner join tarefas using (id);
*/
select 
pessoas.id, 
pessoas.nome, 
tarefas.id,
tarefas.descricao, 
tarefas.status 
from pessoas inner join tarefas using (id);

-- Left Join
/*
- Definição: Retorna todos os registros da tabela da esquerda
(a primeira citada no FROM), e os registros correspondentes da tabela da direita.
Se não houver correspondências, os campos da tabela da direita vêm como NULL.
- Exemplo prático: Listar todas as pessoas, mesmo as que não possuem tarefas.
*/

Select p.id, p.nome, t.id as "Tarefas ID", t.descricao, t.status
from pessoas p left join tarefas t on p.id = t.pessoa_id order by p.id, t.id;

-- para saber qual JOIN (left, right) vai depender de como esta disposto as entidades da query


-- Não quero mostrar os registros de quem não tem tarefas
Select p.id, p.nome, t.id as "Tarefas ID", t.descricao, t.status
from pessoas p left join tarefas t
on p.id = t.pessoa_id
where t.id is null;
-- o "where t.id id null" serve como uma condicional, mostrando apenas quem não tem tarefas

-- Mostrando os registros com relacionamentos com tarefas.
Select p.id, p.nome, t.id as "Tarefas ID", t.descricao, t.status
from pessoas p left join tarefas t
on p.id = t.pessoa_id
where t.id is not null;
-- o diferencial aqui é o "IS NOT NULL" que mostra apenas os que tem relacionamento com tarefas.

-- Right join:
/*
- Definição: É o inverso do LEFT JOIN. Retorna todos os registros da tabela da direita e os
correspondentes da tabela da esquerda.
Se não houver correspondência, os campos da tabela da esquerda vêm como NULL.
Exemplo prático: Listar todas as tarefas, mesmo aquelas que ainda não tem pessoas atribuidas.
*/

select t.id as "Tarefa ID", t.descricao, t.status, p.id as "Pessoa ID", p.nome
from pessoas p right join tarefas t
on p.id = t.pessoa_id;

-- mostrar tarefas sem pessoas atribuida
select t.id as "Tarefa ID", t.descricao, t.status, p.id as "Pessoa ID", p.nome
from pessoas p right join tarefas t
on p.id = t.pessoa_id
where t.id id null;
