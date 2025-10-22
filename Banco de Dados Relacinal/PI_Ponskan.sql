create database PI_Ponskan;
use PI_Ponskan;

create table usuarios(
    id int auto_increment primary key,
    faculdade varchar(100),
    curso varchar(100) not null,
    email varchar(255),
    senha varchar(20) not null,
    telefone varchar(15),
    data_nasci date not null,
    tipo_acesso varchar(50) not null,
    endereco varchar(255),
    cnpj varchar(20) not null,
);

create table doencas(
    id int auto_increment primary key,
    nome_doenca varchar(100) not null,
    descricao varchar(255),
    agente varchar(100),
    tratamento varchar(255),
    profilaxia varchar(255),
);

create table sintomas(
    id int auto_increment primary key,
    doenca_id int,
    nome varchar(100) not null,
    descricao varchar(255),
    foreign key (doenca_id) references doencas(id),
);

create table pesquisa_biblioteca(
    id int auto_increment primary key,
    usuario_id int,
    doencas_id int,
    foreign key (usuario_id) references usuarios(id),
    foreign key (doencas_id) references doencas(id),
);

create table fotos(
    id int auto_increment primary key,
    usuario_id int,
    caminho varchar(10) not null,
    data datetime,
    hora time,
    coordenadas varchar(50),
    caso int,
    foreign key (usuario_id) references usuarios(id),
);

create table planos_acao(
    id int auto_increment primary key,
    usuario_id int,
    avaliacao varchar(255),
    valor_final decimal(10,2),
    validade date,
    foreign key (usuario_id) references usuarios(id)
);

create table classificacoes(
    id int auto_increment primary key,
    foto_id int,
    man_trincada varchar(50),
    falsa_melanose varchar(50),
    tempo varchar(10),
    pinta_preta varchar(50),
    saudavel varchar(50),
    man_preta varchar(50),
    man_sardenta varchar(50),
    foreign key(foto_id)references fotos(id),
);

create table diagnosticos(
    id int auto_increment primary key,
    classificacao_id int,
    plano_id int,
    problema varchar(150),
    gravidade varchar(50),
    foreign key (classificacao_id) references classificacoes(id),
    foreign key (plano_id) references planos_acao(id),
);

create table acoes(
    id int auto_increment primary key,
    plano_id int,
    dt_hr_inicio datetime,
    dt_hr_fim datetime,
    coordenadas varchar(50),
    tipo varchar(100),
    fonte varchar(100),
    titulo varchar(100),
    descricao varchar(255),
    prioridade varchar(50),
    justificativa varchar(255),
    valor decimal(10,2),
    foreign ke (plano_id) references planos_acao(id),
);
