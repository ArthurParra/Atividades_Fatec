/*criando tabela no postgreSQL*/
create table Clientes
(
id_Cli serial primary key,
nome_Cli varchar(50) not null,
idade_Cli int
);

/*inserndo dados na tabela*/
insert into Clientes (nome_Cli, idade_Cli) values ('Arnaldo Fritz', 33);

/*listando/verificando os dados*/
select * from Clientes;

create table Autores(
id_autor serial primary key,
nome_autor varchar(100) not null
);

insert into Autores (nome_autor) values ('J.K Rowling');
insert into Autores (nome_autor) values ('George R.R Martin');

select * from Autores;