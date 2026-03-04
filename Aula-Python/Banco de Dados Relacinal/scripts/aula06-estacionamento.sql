create database estacionamento;
use estacionamento;

Create table Clientes(
    id int primary key auto_increment,
    nome varchar(100) not null,
    telefone varchar(20)
);

create table veiculos(
    id int primary key auto_increment,
    placa varchar(10) unique,
    modelo varchar(20),
    cliente_id int,
    constraint fk_veiculo_cliente foreign key(cliente_id) references Clientes(id)
);

create table vagas(
    id int primary key auto_increment,
    codigo varchar(10),
    tipo enum('Carro', 'Moto')
);

create table movimentacoes(
    id int primary key auto_increment,
    veiculo_id int,
    vaga_id int,
    entrada datetime,
    saida datetime,
    constraint fk_mov_veiculo foreign key (veiculo_id) references veiculos(id),
    constraint fk_mov_vaga foreign key (vaga_id) references vagas(id)
);

create table funcionarios(
    id int primary key auto_increment,
    nome varchar(100) not null,
    cargo varchar(50) not null,
    id_supervisor int,
    constraint fk_func_supervisor foreign key (id_supervisor) references funcionarios(id)
);

-- setando valor a tabela clientes:
insert into Clientes (nome, telefone) values
('Ana Silva', '1199999-1111'),
('Bruno Souza', '1198888-2222'),
('Carlos Lima', '1197777-3333');

-- setando veiculos a tabela vagas:
insert into veiculos (placa, modelo, cliente_id) values 
('abc1234', 'Fiat UNO', 1),
('xyz9876', 'Honda Civic', 2),
('mno3456', 'Yamaha Fazer', 3),
('asd2534', 'Veiculo Desconhecido', null);

-- setando valor a tabela vagas:
insert into vagas (codigo, tipo) values
('c1','carro'), ('c2','carro'), ('m1','moto');

-- setando valor a tabela funcionarios:
insert into funcionarios (nome, cargo, id_supervisor) values
('Diego', 'Gerente', null),
('Fernanda', 'Atendente', 1),
('Paulo', 'Manobrista', 1),
('Juliana', 'Estagiaria', 2);

-- setando valor em movimentações:
insert into movimentacoes (veiculo_id, vaga_id, entrada, saida) values
(1,1, '2025-09-20 08:00:00', '2025-09-20 12:00:00'),
(2,2, '2025-09-20 09:00:00', null),
(3,3, '2025-09-20 10:00:00', null);

-- Exemplo de Aplicação Inner Join:
/*
1- Elabore uma consulta SQL que retorne o nome dos clientes juntamente com a
placa e o modelo dos veiculos que estão associados a eles.
Considere que os dados estão distribuidos em duas tabelas:
Clientes (com a coluna id como chave primaria) e
Veiculos (com a coluna clientes_id como chave estrangeira que referencia a tabela clientes).
Utilize um INNER JOIN para relacionar as duas tabelas e selecione as colunas nome do cliente,
placa e modelo do veiculo.
Renomeie a coluna nome como clietnte no resultado da consulta.
*/

select c.nome as "Cliente", v.placa, v.modelo from clientes c
inner join veiculos v on c.id = v.cliente_id;

select c.nome as "Cliente", v.placa, v.modelo as "Modelo" from clientes c
inner join veiculos v on c.id = v.cliente_id;

/*
2- Liste o nome dos Clientes e as placas dos veiculos que lhe pertencem.
*/

select c.nome as "Clientes", v.placa as "Placa" from clientes c
inner join veiculos v using (id);

/*
3- Liste as placas e os modelos dos veiculos, juntamente com o nome do cliente (caso exista).
*/

select v.placa as "Placa", v.modelo as "Modelo",  c.nome as "Cliente" from veiculos v
left join clientes c on v.cliente_id = c.id;

/*
4- Liste o ID das movimentações, as placas e modelos dos veiculos, além das datas de entrada e saída,
incluindo movimentações sem veiculos cadastrados.
*/

select m.id, v.placa, v.modelo, m.entradas, m.saida from veiculos v 
right join movimentacoes m on v.id = m.veiculo_id;

/*
5- Liste as placas dos veiculos com as suas respectivas
datas de entrada e saida, incluindo tabém as movimentações
sem veiculos cadastrados.
*/

select v.placa, m.entrada, m.saida from veiculos v
left join movimentacoes m on v.id = m.veiculo_id
union
select v.placa, m.entrada, m.saida from veiculos v
right join movimentacoes m on v.id = m.veiculo_id
where v.id is null;

/*
6- Liste os nomes dos funcionarios juntamente com os nomes dos cargos atribuidos a eles.
*/

select f.nome as "Funcionario", s.nome as "Supervisor" from funcionarios 