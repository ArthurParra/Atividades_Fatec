#Criando um banco de dados
create database livraria_teste;

#para selecionar/mudar o bando de dados utiliza-se "use"+nome da database
use livraria_teste;

#criar uma tabela chamdas Clientes para o banco de dados "Livraria_teste"
#para selecionar/mudar o bando de dados utiliza-se "use"+nome da database
use livraria_teste;

#criar uma tabela chamada Clientes para o banco de dados "Livraria_teste"
/*
Para criar uma tabela no banco de dados precisamos de algumas informações:
- Nome da tabela(boas praticas no plural)
- Atributos:
--- Nome do atributo (singular)
--- Tipo de dado para o atributo
--- Tamanho do atributo
--- Restrições do atributo
---- PrimaryKey
---- Auto_increment
---- Not Null
*/

#criando tabela:
create table Clientes (
id_Cli int auto_increment primary key,
nome_Cli varchar(50) not null,
idade_Cli int(3)
);

#inserir dados na tabela clientes
/*
Para inserir dados na tabela devemos utlizar a query "insert into" e o nome da tabela a ser inserido os dados.
Devemos informar os campos que serão alimentadosn pelos dados, e depois informar os dados a serem inseridos.
*/
#nserindo dados:
insert into Clientes (nome_Cli, idade_Cli) values ("Arthur Parra",18);
insert into Clientes (nome_Cli, idade_Cli) values (19,"Joao Vitor");

insert into Clientes (idade_Cli, nome_Cli ) values (19,"Joao Vitor");

insert into Clientes (nome_Cli) values ("Shimada");

insert into Clientes (idade_Cli) values (19);

insert into Clientes (nome_Cli, idade_Cli) values (60);

select * from Clientes;
/*
Crie uma tabela chamada Autores com os  seguintes atributos: 
id_autor int auto increment primary key
nome_autor varchar de 100 espaços não aceitando nulo.
*/

/*
inserir os dados na tabela
1. J.K Rowling
2. Geoge R.R Martin
*/

create table Autores (
id_autor int auto_increment primary key,
nome_autor varchar(100) not null
);

insert into Autores (nome_autor) values ("J.K Rowling");
insert into Autores (nome_autor) values ("George R.R Martin");

select * from Autores;

/*
Crie uma tabela chamada Livros com os seguintes atributos: idLivro, tituloLivro 200 espaços idAutor sendo relacionado atraves de foreign key.
*/

create table Livros(
id_livros int auto_increment primary key,
titulo_livro varchar(200) not null,
id_autor int,
foreign key(id_autor) references Autores(id_autor)
);

-- dia 26/08/2025:

/*
criando a tabela Pedidos
*/

create table Pedidos(
id_pedido int auto_increment primary key,
data_pedido date not null,
valor_total decimal (10, 2) not null,
id_Cli int,
foreign key (id_Cli) references Clientes(id_Cli)
);

create table Itens_pediddo (
id_item int auto_increment primary key,
quantidade int not null,
preco_unitario decimal(10, 2) not null,
id_pedido int,
id_livros int,
foreign key (id_pedido) references Pedidos(id_pedido),
foreign key (id_livros) references Livros(id_livros)
);

alter table clientes add column(
rua varchar (250),
cidade varchar(150),
cep varchar(10),
data_nasci date
);

alter table livros add column(
autor varchar (100)
);

-- Inserção de dados na tabela clientes:
insert into Clientes (nome_Cli, rua, cidade, cep, data_nasci) values 
('Ana Silva', 'Rua das Flores, 123', 'São Paulo', '01001-000', '1985-05-15'),
('Carlos Pereira', 'Avenida Paulisra, 456', 'São Paulo', '01310-000', '1990-08-22'),
('Maria Costa', 'Rua dos Pinheiros, 789', 'Rio d Janeiro', '20040-000', '1978-11-30');

insert into autores (nome_autor) values
('J.R.R Tolkien'),('George Orwell'),('Machado de Assis');

insert into livros (titulo_livro, id_autor, preco, categoria) values 
('O senhor dos aneis', 3, 59.90, 'Fantasia'),
('1984', 4, 39.90, 'Ficcao Cientifica'),
('Dom Casmurro', 5, 29.90, 'Literatura Brasileira');

DROP TABLE livros;

create database BD_Bike;
use BD_Bike;

create table Clientes(
    id_cliente int auto_increment primary key,
    nome varchar(100) not null,
    telefone int(11),
    email varchar(100),
    endereco varchar(250)
    );

create table Bicicletas(
	id_bike int auto_increment primary key,
	marca varchar (10) not null,
	modelo varchar(20),
	ano int (4),
	tipo_bike varchar(10),
	numero_serie varchar(10),
	id_cliente int,
	foreign key (id_cliente) references Clientes(id_cliente)
);

create table Servicos(
    id_servico int auto_increment primary key,
    nome varchar(100) not null,
    descricao varchar(300),
    preco_base int not null,
    tempo_estima time
);

create table Produtos(
    id_produ int auto_increment primary key,
    nome varchar (100) not null,
    descricao varchar (300),
    preco_unitario int,
    estoque int not null
);

create table Ordem_Servicos(
    id_ordem int auto_increment primary key,
    data_entrada date not null,
    data_saida date not null,
    status varchar(100) not null,
    observacoes varchar(300),
    id_bike int,
    foreign key (id_bike) references Bicicletas(id_bike)
);

create table item_OrdemDeServi(
    id_item int auto_increment primary key,
    tipo_ordem varchar(100) not null,
    quantidade int not null,
    preco_total decimal (10, 2),
    id_referencia int,
    id_ordem int,
    foreign key (id_ordem) references Ordem_Servicos(id_ordem),
    foreign key (id_referencia) references Produtos(id_produ)
);

create table Personalizacao(
    id_persona int auto_increment primary key,
    data date,
    descricao varchar(150),
    preco decimal(10, 2),
    id_bike int,
    foreign key (id_bike) references Bicicletas(id_bike)
);

create table Vendas(
    id_venda int auto_increment primary key,
    data_venda date,
    total int(10) not null,
    id_cliente int,
    foreign key (id_cliente) references Clientes(id_cliente)
);

create table Item_Vendas(
    id_item_venda int auto_increment primary key,
    quantidade int(20) not null,
    preco_unitario decimal(10, 2) not null,
    id_venda int,
    id_produ int,
    foreign key (id_venda) references Vendas(id_venda),
    foreign key (id_produ) references Produtos(id_produ)
);


INSERT INTO Clientes (nome, telefone, email, endereco) VALUES
('Joao da Silva', '(11) 91234-5678', 'joao.silva@email.com', 'Rua das Flores, 123 - São Paulo'),
('Maria Oliveira', '(21) 99876-5432', 'maria.oliveira@gmail.com', 'Av. Atlântica, 456 - Rio de Janeiro'),
('Pedro Santos', '(31) 98765-4321', 'pedro.santos@gmail.com', 'R. Minas Gerais, 89 - Belo Horizonte');


INSERT INTO Bicicletas ( marca, modelo, ano, tipo_bike, numero_serie) VALUES
('Caloi', 'Elite 30', 2023, 'MTB', 'C123456789'),
('Trek', 'Domane AL 2', 2023, 'Speed', 'T987654321'),
('Oggi', 'Hacker Sport', 2021, 'Urbana', 'O654321987');

INSERT INTO Servicos (nome, descricao, preco_base, tempo_estima) VALUES
('Revisao Geral', 'Revisão completa da bicicleta', 150.00, '02:30:00'),
('Troca de Freio', 'Substituicao dos freios dianteiros e traseiros', 80.00, '01:00:00'),
('Alinhamento de Roda', 'Alinhamento das rodas dianteira/traseira', 60.00, '00:45:00');

INSERT INTO Produtos (nome, descricao, preco_unitario, estoque) VALUES
('Pneu 29"', 'Pneu MTB 29x2.10', 120.00, 10),
('Câmbio Shimano Altus', 'Câmbio traseiro 8v', 180.00, 5),
('Pastilha de Freio', 'Pastilha de freio hidráulico', 40.00, 20),
('Guidão Flat', 'Guidão de alumínio 720mm', 90.00, 7);

INSERT INTO Ordem_Servicos ( data_entrada, data_saida, status, observacoes) VALUES
( '2025-08-19', '2025-08-20', 'Concluído', 'Revisão completa'),
( '2025-08-23', NULL, 'Em andamento', 'Troca de freio');

INSERT INTO Item_OrdemDeServi (tipo_ordem, quantidade, preco_total) VALUES
('Servico', 1, 150.00),
('Produto', 2, 80.00),
('Servico', 1, 60.00),
('Servico', 1, 80.00);

INSERT INTO Personalizacao (data, descricao, preco) VALUES
('2025-08-18', 'Pintura personalizada + guidão novo', 250.00);

INSERT INTO Vendas (data_venda, total) VALUES
('2025-08-19', 210.00),
('2025-08-25', 120.00);

INSERT INTO Item_Vendas (quantidade, preco_unitario) VALUES
(1, 120.00),
(2, 40.00),
(1, 120.00);

select * from Ordem_Servicos;


###############################################
 