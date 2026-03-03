/*
Restruções e INtegridade de dados.

O que são restrições de integridade?:
São regras que grantem a confiabilidade e consistencia
dos dados em um banco de dados.
Tipos de Restrições:
-- Integridade de Entidade: Garante que cada registro de uma tabela seja unico
--- PK (Primary key);
--- Unique
--- Not Null

-- Integridade Referencial: Mantém os relacionamentos entre tabelas válidos.
--- FK (foreign key)
--- On delete Cascate -> Se um cliente for excluido, seus pedidos
--- On delete Restrict -> impede a exclusão se houver pedidos vinculados.alter

-- Integridade de Dominio: Define valores permitidos para um campo.
--- Check(preco > 0) -> Preço não poderá ser negtivo
--- ENUM ('Pendente', 'Pago',  'Cancelado') ->  O atributo receberá somente os valores pré-definidos
--- Default -> Valores padrão se nenhum valor for informado para o atributo.
*/ 

create database if not exists bd_cursos;
use bd_cursos;

create table alunos(
id int primary key auto_increment, /*PRIMARY KEY -> identifica cada linha*/
nome varchar(100) not null, /*campo obrigatorio*/
email varchar(100) unique not null,/*UNIQUE -> Evita Duplicidade de dado*/
genero enum('M', 'F', 'Não Informado') default 'Não informado',/*Aceita somente os valores pré-definidos*/
data_nascimento date not null,
status_ativo boolean default true
);

create table cursos (
id int primary key auto_increment,
nome_curso varchar(100) not null unique,
carga_horaria int not null check(carga_horaria >= 10 and carga_horaria <=200),
nivel enum('Basico', 'Intermediario', 'Avançado') not null,
ativo boolean default true
);

create table matriculas(
id int primary key auto_increment,
aluno_id int not null,
curso_id int not null,
data_matricula date not null default current_timestamp,
-- Restrições de Integridade:
constraint fk_idAluno_matricula foreign key (aluno_id) references alunos(id)
on delete cascade, -- Se um aluno for excluido, irá apagar a matricula tambem.
constraint fk_idCurso_matricula foreign key (curso_id) references cursos(id)
on delete restrict -- Irá impedir a exclusão do curso que estiver na matricula.
);

insert into alunos (nome,email,genero,data_nascimento) values
('Ana Silva', 'ana.silva@gmail', 'F', '2000-05-20' ),
('Carlos Souza', 'carlos.souza@gmail', 'M', '1998-03-10' );

insert into cursos (nome_curso, carga_horaria, nivel) values
('Introdução a Programação', 40, 'Basico'),
('Banco de Dados Avançado', 80, 'Avançado');

insert into matriculas (aluno_id,curso_id) values
(1,2),
(2,1);

select * from alunos;
select * from cursos;
select * from matriculas;

-- Erro: Duplicando o campo email (violando o UNIQUE)
insert into alunos (nome,email,fata_nascimento) values
('Ana C. Silva', 'ana.silva@gmail.com', 'F', '2001-01-01');
/*Ele da erro, pois ja existe o valor "ana.silva@gmail.com" na tabela coluna email*/

-- Erro: Nulo em campo Not Null
insert into cursos (nome, carga_horaria, nivel) values
(Null, 40, 'Basico');
/*O erro se da por não poder ter um valor "nulo" na coluna*/

-- Erro: Violando Check (carga_horaria invalida)
insert into cursos (nome,carga_horaria,nivel) values
('Curso Invalido', 5, 'Intermediario');
/*O valor da carga horaria não bate com os valores colocados no CHECK anteriormente, então dará erro*/

-- Erro: apagar cursos com matricula (on delete restrict)
delete from cursos where id = 1;
/*ele da erro, pois não pode apagar um curso que tem matricula*/

