create database bd_transaction;
use bd_transaction;

create table clientes(
    id int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(255)
);

create table contas(
    id int auto_increment primary key,
    cliente_id int,
    saldo decimal(10,2),
    foreign key (cliente_id) references clientes(id)
);

create table transacoes(
    id int auto_increment primary key,
    conta_id int,
    valor decimal(10,2),
    tipo_transacao varchar(10),
    data_transacao datetime,
    foreign key (conta_id) references contas(id)
);

insert into clientes (nome, email) values
("João Silva", "joao@gmail.com"),
("Maria Santos","maria@gmail.com"),
("Carlos Pereira", "carlos@gmail.com");

insert into contas (cliente_id, saldo)values
(1, 1000),
(2, 500),
(3, 1200);

insert into transacoes (conta_id, valor, tipo_transacao, data_transacao) values
(1, 500, "deposito", "2024-09-18 10:00:00"),
(1, 200, "saque", "2024-09-18 11:00:00"),
(1, 300, "deposito", "2024-09-18 12:00:00");

select * from clientes;
select * from contas;
select * from transacoes;


#Index
/*
Suponha que você faça muitas consultas na base de dados, baseada em nome.
Um indice na coluna nome ira acelerar essas consultas.
*/

#Consulta sem Index
select * from clientes where nome="João Silva";

#Criando Index na coluna nome
create index idx_cliente_nome on clientes(nome);

#Consulta com Index
select * from clientes where nome="João Silva";

# Index em colunas para busca completa
/*
Se as consultas frequentemente buscam por combinações de saldo e cliente_id,
deve criar um indice composto pode melhorar o desempenho.
*/

#Consulta sem Index
select * from contas where cliente_id=1 and saldo>500;

#Criar o Index
create index idx_cliente_saldo on contas(cliente_id, saldo);

#Index para melhorar o Order By
/*
Ao usar a clausula Order By em uma coluna especifica, o uso de indice
pode acelerar o processo de ordenação.
*/

-- Criando o Index
create index idx_transacoes_data on transacoes(data_transacao);

#Transações  - Transaction

-- Transação que deu tudo certo (transferencia de valores entre contas)
start transaction;
update contas set saldo = saldo - 100 where id = 1; -- Conta do João / Retirando valor
update contas set saldo = saldo + 100 where id = 2; -- Conta da Maria / Depositando valor
commit;

select * from contas;

-- Transação que falhou (transferencia de valores entre contas)
start transaction;
update contas set saldo = saldo - 1100 where id=1; -- Conta do João / Retirando valor
update contas set saldo = saldo + 1100 where id=2; -- Conta da Maria / Depositando valor
select * from contas;
rollback;
select * from contas;

-- Transacao sem o uso de transaction (Trqanferencia de valores entre contas)
update contas set saldo = saldo - 1100 where id=1;
update contas set saldo = saldo + 1100 where id=2;
select * from contas;
rollback; -- rollback só funciona se o start transaction estiver ativado.
select * from contas;

select * from transacoes;

start transaction;
update contas set saldo = saldo + 300 where id=1;
insert into transacoes (conta_id, valor, tipo_transacao, data_transacao) values
(1, 300, "deposito", now());
commit;

select * from contas;
select * from transacoes;

start transaction;
update contas set saldo = saldo - 300 where id=2;
insert into transacoes (conta_id, valor, tipo_transacao, data_transacao) values
(2, 300, "saque", now()); -- na aula o professor escreveu (1, 300, "saque", now()), não sei se foi erro, mas qualquer coisa só corrigir e dar rollback pra "cancelar"

select * from contas;
select * from transacoes;

rollback; -- se não era isso que era pra acontecer, dê um rollback