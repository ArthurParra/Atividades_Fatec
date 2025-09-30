create database SysLivros;
use SysLivros;

create table Autores(
    autorID int auto_increment primary key,
    nome varchar(255) not null,
    pais varchar(50)
);

create table livros(
    livroId int auto_increment primary key,
    autorID int,
    titulo varchar(255),
    preco decimal(10,2)null,
    estoque int default 0,
    constraint fk_autorid_livros foreign key (autorID) references autores(autorID)
);

create table vendas(
    vendaId int auto_increment primary key,
    livroId int,
    data_venda date,
    quantidade int not null,
    valor_total decimal (10,2),
    constraint fk_livroId_vendas foreign key(livroId) references livros(livroId)
);

insert into Autores (nome, pais) values
('Machado de Assis', 'Brasil'),
('Clarice Linspector', 'Brasil'),
('Jorge Amado', 'Brasil');

insert into livros (titulo, autorID, preco, estoque) values
('Dmom Casmurro', 1, 34.90, 12),
('A Hora da Estrela', 2, 29.90,7),
('Capitaes de Areia', 3, 39.90,9);

insert into vendas (livroId, data_venda, quantidade, valor_total) values
(1, '2024-09-01', 3, 104.70),
(2, '2024-09-02', 2, 59.80),
(3, '2024-09-02', 1, 39.90);


-- Criando uma função no Banco de Dados:

/*
delimiter //
create function nomeFunção() returns Tipo_dado
begin
------
----
------
-----

end //
*/

-- Mudando o delimitador:
DELIMITER //
CREATE FUNCTION TotalGeral()
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE total DECIMAL(10,2);
    SELECT SUM(valor_total) INTO total FROM vendas;
    RETURN IFNULL(total, 0);
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION TotalVendasPorLivro(p_livroId INT)
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE total DECIMAL(10,2);
    SELECT SUM(valor_total) INTO total
    FROM vendas
    WHERE livroId = p_livroId;
    RETURN IFNULL(total, 0);
END //
DELIMITER ;


select TotalGeral() as "total";

-- Função Calcula Vendas:

delimiter //
create function calculaVenda (ID int, quantidade int) returns decimal (10,2)
begin
    declare valor_total decimal (10,2);
    declare prec decimal(10,2);
    -- Buscar o preço do livro na tabela
    select preco into prec from livros where livros.livroId = ID limit 1;
    if prec is null then
        return 0;
        end if;
    -- Calcular o valor total de venda:
    set valor_total = prec * quantidade;
    return valor_total;
end //
delimiter ;

select calculaVenda(1,5);
select preco from livros where livroId=1;

-- Criando registro de vendas:

delimiter //
create procedure RegistrarVenda (in id int, in quantidade int)
begin
    declare valor_total decimal(10,2);

    set valor_total = calculaVenda(id,quantidade);
    insert into vendas (livroId, data_venda,quantidade, valor_total) values
    (id,curdate(),quantidade, valor_total);
end //
delimiter ;

call RegistrarVenda(2,8);
select * from vendas;