-- Criando banco de dados
create database if not exists logistica_db;
use logistica_db;

--Criando tabelas
create table clientes(
    id_cliente int auto_increment primary key,
    razao_social_cliente varchar(50),
    cnpj_cliente varchar(20),
    telefone_cliente varchar(15),
    cidade_cliente varchar(50),
    uf_cliente varchar(2)
);

create table motoristas(
    id_motorista int auto_increment primary key,
    nome_motorista varchar(50),
    cpf_motorista varchar(15),
    cnh_motorista varchar(10),
    status_motorista enum('Ativo', 'Férias', 'Desativado') default 'Ativo'
);

create table veiculos(
    id_veiculo int auto_increment primary key,
    placa_veiculo varchar(7),
    tipo_veiculo varchar(50),
    capacidade_veiculo decimal(10, 2),
    ano_veiculo year,
    status_veiculo enum('Em Rota', 'Disponível', 'Manutenção') default 'Disponível'
);

create table pedidos_transportes(
    id_pedido int auto_increment primary key,
    descricao_carga_pedido varchar(255),
    peso_total_pedido decimal(10, 2),
    volume_pedido decimal(10, 2),
    origem_cidade_pedido varchar(50),
    origem_uf_pedido varchar(2),
    destino_cidade_pedido varchar(50),
    destino_uf_pedido varchar(2),
    data_pedido date,
    prazo_pedido date,
    valor_pedido decimal(10, 2),
    
    id_cliente int,
    constraint fk_id_cliente_pedidos_transportes
    foreign key (id_cliente) references clientes(id_cliente)
);

create table entregas(
    id_entrega int auto_increment primary key,
    destino_entrega varchar(50),
    data_saida_entrega datetime,
    data_entrega datetime,
    status_entrega enum('Entregue', 'Em Rota', 'Atrasada') default 'Em Rota',
    km_percorridos_entrega decimal(10,2),
    ocorrencia_entrega varchar(255),
    
    id_pedido int,
    constraint fk_id_pedido_entregas
    foreign key (id_pedido) references pedidos_transportes(id_pedido),
    
    id_motorista int,
    constraint fk_id_motorista_entregas
    foreign key (id_motorista) references motoristas(id_motorista),
    
    id_veiculo int,
    constraint fk_id_veiculo_entregas
    foreign key (id_veiculo) references veiculos(id_veiculo)
);

-- Fazendo os Inserts das tabelas
insert into clientes(razao_social_cliente, cnpj_cliente, telefone_cliente, cidade_cliente, uf_cliente) values
('Supermercados BomPreço LTDA', '12.345.678/0001-90', '(13)3821-1100', 'Registro', 'SP'),
('Frigirífico Vale do Ribeira S/A', '98.765.432/0001-55', '(13)3822-9988', 'Pariquera-Açu', 'SP'),
('Bananas Ouro do Vale ME', '45.111.222/0001-33', '(13)99777-2211', 'Sete Barras', 'SP'),
('Farmácia Popular Ribeirinha LTDA', '22.333.444/0001-12', '(13)3848-1122', 'Eldorado', 'SP');

insert into motoristas(nome_motorista, cpf_motorista, cnh_motorista, status_motorista) values
('Carlos Alberto da Silva', '123.456.789-00', 'E', 'Ativo'),
('Marcos Souza Ferreira', '987.654.321-11', 'D', 'Ativo'),
('Jonas Pereira Santos', '111.222.333-44', 'C', 'Férias'),
('Renata Oliveira Lima', '555.666.777-88', 'D', 'Ativo');

insert into veiculos(placa_veiculo, tipo_veiculo, capacidade_veiculo, ano_veiculo, status_veiculo) values
('ABC1D23', 'Carreta', 32000.00, 2022, 'Em Rota'),
('FGH4I56', 'Truck', 14000.00, 2021, 'Disponível'),
('JKL7M89', '3/4', 3500.00, 2020, 'Manutenção'),
('NOP0Q12', 'Van', 1200.00, 2023, 'Disponível');

insert into pedidos_transportes
(id_cliente, descricao_carga_pedido, peso_total_pedido, volume_pedido, origem_cidade_pedido, origem_uf_pedido,
 destino_cidade_pedido, destino_uf_pedido, data_pedido, prazo_pedido, valor_pedido)values
(1, 'Carga seca - alimentos não perecíveis', 12000.50, 38.2, 'Registro', 'SP', 'Cajati', 'SP', '2025-10-20', '2025-10-21', 3500.00),
(2, 'Carnes resfriadas bovinas', 18000.00, 45.0, 'Pariquera-Açu', 'SP', 'Curitiba', 'PR', '2025-10-19', '2025-10-20', 5200.00),
(3, 'Caixas de banana nanica premium', 8000.00, 60.0, 'Sete Barras', 'SP', 'São Paulo', 'SP', '2025-10-18', '2025-10-19', 4100.00),
(4, 'Medicamentos e dermocosméticos', 1500.00, 12.5, 'Eldorado', 'SP', 'Registro', 'SP', '2025-10-20', '2025-10-20', 900.00);

insert into entregas(id_pedido, id_motorista, id_veiculo, destino_entrega, data_saida_entrega, data_entrega, status_entrega, km_percorridos_entrega, ocorrencia_entrega) values
(1, 1, 2, 'Atacadão Cajati - CD Principal', '2025-10-20 07:30:00', '2025-10-20 10:10:00', 'Entregue', 85, null),
(1, 1, 2, 'Supermercado BomPreço - Filial Cajati', '2025-10-20 10:30:00', '2025-10-20 11:20:00', 'Entregue', 18, 'Pequeno atraso por trânsito urbano'),
(2, 2, 1, 'Rede Churrasqueiras Sul - Curitiba', '2025-10-19 06:00:00', '2025-10-19 14:40:00', 'Entregue', 240, 'Temperatura mantida 4°C'),
(3, 4, 2, 'Ceagesp - Módulo Frutas SP', '2025-10-18 23:15:00', null, 'Em Rota', 180, null),
(4, 4, 4, 'Farmácia Popular Ribeirinha - Matriz Registro', '2025-10-20 08:00:00', '2025-10-20 09:40:00', 'Atrasada', 42, 'Blitz sanitária na BR-116');

-- CONSULTAS
-- 4.1 Visualizar entregas não concluidas
select id_entrega, destino_entrega, status_entrega, data_saida_entrega, data_entrega from entregas where status_entrega != 'Entregue';

-- 4.2 Priorizar cargas caras e urgentes
select id_pedido, descricao_carga_pedido, valor_pedido, prazo_pedido from pedidos_transportes
order by valor_pedido desc, prazo_pedido asc;

-- 4.3 Nome e km de cada motorista
select nome_motorista, sum(km_percorridos_entrega) as km_percorridos from entregas
inner join motoristas on entregas.id_motorista = motoristas.id_motorista
group by nome_motorista;

-- 4.4 Movimento entre 18 e 20 de outubro
select id_entrega, data_saida_entrega, status_entrega, km_percorridos_entrega from entregas
where data_saida_entrega between '2025-10-18 00:00:00' and '2025-10-20 23:59:59';

-- 4.5 Relatório de entregas concluídas
select id_entrega, destino_entrega, data_entrega, nome_motorista, placa_veiculo, descricao_carga_pedido, razao_social_cliente from entregas
inner join motoristas on entregas.id_motorista = motoristas.id_motorista
inner join veiculos on entregas.id_veiculo = veiculos.id_veiculo
inner join pedidos_transportes on entregas.id_pedido = pedidos_transportes.id_pedido
inner join clientes on pedidos_transportes.id_cliente = clientes.id_cliente
where status_entrega = 'Entregue';

-- 4.6 Uso de veículos 
select veiculos.id_veiculo, placa_veiculo, tipo_veiculo, status_veiculo, count(id_entrega) as quantidade_entregas from veiculos
left join entregas on veiculos.id_veiculo = entregas.id_veiculo
group by id_veiculo
order by id_veiculo asc;

-- Fazendo triggers
-- 5.1 Trigger monitoramento de atraso
create table log_atraso(
    id_log int auto_increment primary key,
    momento_log datetime,
    mensagem_log varchar(255),
    id_entrega int,
    constraint fk_id_entrega_log_atraso
    foreign key (id_entrega) references entregas(id_entrega)
);

DELIMITER //
create trigger atraso
after update on entregas for each row 
begin
    if new.status_entrega = 'Atrasada' then
        insert into log_atraso(momento_log, mensagem_log, id_entrega)values
        (now(), old.destino_entrega, old.id_entrega);
    end if;
end //
DELIMITER ;

-- Testando triggers
update entregas set status_entrega = 'Atrasada' where id_entrega = 1;
select * from log_atraso;

-- Restaurando valores
update entregas set status_entrega = 'Entregue' where id_entrega = 1;
select * from entregas;

-- 5.2 Função para cálculo de atrasos (em horas) 
DELIMITER //
create function calcula_atraso_hora(entrega_id int) returns time
begin
    declare prazo datetime;
    declare data_entrega datetime;
    declare horas_atraso time;
    
    select prazo_pedido into prazo from entregas
    inner join pedidos_transportes on entregas.id_pedido = pedidos_transportes.id_pedido
    where id_entrega = entrega_id limit 1;
    select data_entrega into data_entrega from entregas where id_entrega = entrega_id limit 1;
    
    if(data_entrega is null) then
        set horas_atraso = null;
    elseif(data_entrega <= prazo) then
        set horas_atraso = '00:00:00';
    else 
        set horas_atraso = sec_to_time(timestampdiff(second, prazo, data_entrega));
    end if;
    
    return horas_atraso;
end //
DELIMITER ;

-- Testando a função
select calcula_atraso_hora(5);
update entregas set data_entrega = '2025-10-25 03:15:00' where id_entrega = 5; 

-- Restaurando valores
update entregas set data_entrega = '2025-10-20 09:40:00' where id_entrega = 5;
select * from entregas;

-- 5.3 Gerar relatório geral de pedido para cliente
DELIMITER //
create procedure relatorio_cliente(cliente_id int)
begin
    select pedidos_transportes.id_pedido, descricao_carga_pedido, valor_pedido, 
    count(id_entrega) as quantidade_entregas, 
    max(data_entrega) as ultima_data_entrega, 
    max(calcula_atraso_hora(id_entrega)) as maior_atraso
    from clientes
    inner join pedidos_transportes on clientes.id_cliente = pedidos_transportes.id_cliente
    inner join entregas on pedidos_transportes.id_pedido = entregas.id_pedido
    where clientes.id_cliente = cliente_id
    group by pedidos_transportes.id_pedido, descricao_carga_pedido, valor_pedido
    order by pedidos_transportes.id_pedido;
end //
DELIMITER ;

-- Testando procedures
call relatorio_cliente(1);
call relatorio_cliente(2);

-- 6 Garantindo que duas operações dependentes entre si, sejam confirmadas juntas

-- Cenário de sucesso (commit)
start transaction;
insert into entregas(id_pedido, id_motorista, id_veiculo, destino_entrega, data_saida_entrega, data_entrega, status_entrega, km_percorridos_entrega, ocorrencia_entrega) values
(4, 4, 4, 'Farmácia RegisPharma LTDA', '2025-10-20 07:50:00', '2025-10-20 10:00:00', 'Em Rota', 100, "Trânsito embargado, carga refrigerada corretamente");
update veiculos set status_veiculo = "Em Rota" where id_veiculo = 4;
commit;

select id_pedido, id_motorista, entregas.id_veiculo, status_veiculo, destino_entrega, data_saida_entrega, data_entrega, status_entrega, km_percorridos_entrega, ocorrencia_entrega from entregas
left join veiculos on entregas.id_veiculo = veiculos.id_veiculo
where id_entrega = 6;

-- Cenário de falha (rollback)
start transaction;
insert into entregas(id_pedido, id_motorista, id_veiculo, destino_entrega, data_saida_entrega, data_entrega, status_entrega, km_percorridos_entrega, ocorrencia_entrega) values
(3, 3, 3, 'Varejinho Hexatombe LTDA', '2025-10-20 07:50:00', '2025-10-20 10:00:00', 'Entregue', 90, "Acidente na pista.");
update veiculos set status_veiculo = "Em Rota" where id_veiculo = 3;
rollback;

select id_pedido, id_motorista, entregas.id_veiculo, status_veiculo, destino_entrega, data_saida_entrega, data_entrega, status_entrega, km_percorridos_entrega, ocorrencia_entrega from entregas
left join veiculos on entregas.id_veiculo = veiculos.id_veiculo
where id_entrega = 7;