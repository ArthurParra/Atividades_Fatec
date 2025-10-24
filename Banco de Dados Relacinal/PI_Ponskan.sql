-- criando a database do Projeto Integrador
create database PI_Ponkan;
use PI_Ponkan;

-- iniciando criação das tabelas
create table usuarios(
    id int auto_increment primary key,
    nome varchar(100),
    faculdade varchar(100),
    curso varchar(100) not null,
    email varchar(255),
    senha varchar(20) not null,
    telefone varchar(15),
    data_nasci date not null,
    tipo_acesso varchar(50) not null,
    endereco varchar(255),
    cnpj varchar(20) not null
);

-- tabela de doenças e sintomas relacionadas
create table doencas(
    id int auto_increment primary key,
    nome_doenca varchar(100) not null,
    descricao varchar(255),
    agente varchar(100),
    tratamento varchar(255),
    profilaxia varchar(255)
);

create table sintomas(
    id int auto_increment primary key,
    doenca_id int,
    nome varchar(100) not null,
    descricao varchar(255),
    foreign key (doenca_id) references doencas(id)
);

-- usuario pesquisa na biblioteca de doenças
-- entidade associativa entre usuario e doenças
create table pesquisa_biblioteca(
    id int auto_increment primary key,
    usuario_id int,
    doencas_id int,
    foreign key (usuario_id) references usuarios(id),
    foreign key (doencas_id) references doencas(id)
);

-- usuario carrega/captura fotos, que gera classificações
-- fotos capturam dados momentaneos 
create table fotos(
    id int auto_increment primary key,
    usuario_id int,
    caminho varchar(255) not null,
    data datetime,
    hora time,
    coordenadas varchar(50),
    caso int,
    foreign key (usuario_id) references usuarios(id)
);

-- classificações produzem diagnosticos
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
    foreign key(foto_id) references fotos(id)
);

-- usuario produz/atualiza plano de ação
-- plano de ação atualiza diagnosticos
create table planos_acao(
    id int auto_increment primary key,
    usuario_id int,
    avaliacao varchar(255),
    valor_final decimal(10,2),
    validade date,
    foreign key (usuario_id) references usuarios(id)
);

create table diagnosticos(
    id int auto_increment primary key,
    classificacao_id int,
    plano_id int,
    problema varchar(150),
    gravidade varchar(50),
    foreign key (classificacao_id) references classificacoes(id),
    foreign key (plano_id) references planos_acao(id)
);

-- ações possuem planos de ação e consultam dados temporais
create table acoes(
    id_acao int auto_increment primary key,
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
    foreign key (plano_id) references planos_acao(id)
);

/*
Criando a tabela de dados temporais que servirá como tabela pai para:
- momentaneo
- historico
- previsivo
*/
create table dados_temporais(
    id_dado int auto_increment primary key,
    latitude decimal(10,6),
    longitude decimal(10,6),
    dt_hora_coleta datetime,
    fonte varchar(100)
);

/*
Momentaneo é a unica sem auto_increment pois esta diretamente ligado aos dados temporais
Já as outras terão seu proprio id unico, por isso o auto_increment
*/
create table momentaneo(
    id_dado int primary key,
    temperatura decimal(5,2),
    umidade decimal(5,2),
    prec decimal(5,2),
    velocidade_vento decimal(5,2),
    direcao_vento varchar(10),
    id_rota int,
    foreign key (id_dado) references dados_temporais(id_dado)
);

create table historico(
    id_historico int auto_increment primary key,
    id_dado int,
    media_temperatura decimal(5,2),
    media_umidade decimal(5,2),
    media_prec decimal(5,2),
    data_inicio datetime,
    data_fim datetime,
    foreign key (id_dado) references dados_temporais(id_dado)
);

create table previsivo(
    id_previsivo int auto_increment primary key,
    id_dado int,
    data_inicio datetime,
    data_fim datetime,
    temp decimal(5,2),
    umid decimal(5,2),
    prec decimal(5,2),
    probabilidade_prec decimal(5,2),
    vel_vento decimal(5,2),
    direcao_vento varchar(10),
    foreign key (id_dado) references dados_temporais(id_dado)
);

-- entidade associativa entre as ações e dados temporais
create table consulta_temporal(
    id_consulta int auto_increment primary key,
    id_acao int,
    id_dado_previsivo int,
    id_dado_historico int,
    foreign key (id_acao) references acoes(id_acao),
    foreign key (id_dado_previsivo) references previsivo(id_previsivo),
    foreign key (id_dado_historico) references historico(id_historico)
);

-- populando a tabela usuarios com exemplos
insert into usuarios (nome, faculdade, curso, email, senha, telefone, data_nasci, tipo_acesso, endereco, cnpj) values
('Ademar Robson Silva', 'Fatec DSM','Análise e Desenvolvimento de Sistemas','ademar.100@gmail.com','ademar123','(11)98765-4321','2000-05-10','aluno','Rua Antonio das Cruzes, 123','00.000.000/0001-00'),
('Mariano Neves', 'Fatec DSM','Análise e Desenvolvimento de Sistemas','NevesMariano@gmail.com','profsenha','(11)98888-7777','1990-03-20','professor','Av Boulevard Fonseca, 456','11.111.111/0001-11'),
('Myrella Dias', 'Universidade X','Biomedicina','MymyDias@gmail.com','Dokidoki456','(11)97654-3210','1998-11-30','aluno','Rua DomCastellani, 789','22.222.222/0001-33');

-- Próximo passo: popular as tabelas: doenças, sintomas, planos_ação e dados_temporais