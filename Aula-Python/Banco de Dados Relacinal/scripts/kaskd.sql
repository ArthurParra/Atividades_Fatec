CREATE DATABASE gestao_projetos_dani;
USE gestao_projetos_dani;

CREATE TABLE projeto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_inicio DATE NOT NULL,
    data_fim DATE
);

create table pessoa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE papel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    funcao varchar(100) 
);

CREATE TABLE alocacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    projeto_id INT NOT NULL,
    pessoa_id INT NOT NULL,
    papel_id INT NOT NULL,
    constraint fk_alocacao_projeto FOREIGN KEY (projeto_id) REFERENCES projeto(id),
    constraint fk_alocacao_pessoa FOREIGN KEY (pessoa_id) REFERENCES pessoa(id),
    constraint fk_alocacao_papel FOREIGN KEY (papel_id) REFERENCES papel(id)
);

CREATE TABLE tarefa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    projeto_id INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT,
    status ENUM('Planejada','Em andamento','Concluída') NOT NULL,
    responsavel_id INT,
    FOREIGN KEY (projeto_id) REFERENCES projeto(id),
    FOREIGN KEY (responsavel_id) REFERENCES pessoa(id)
);

INSERT INTO projeto (nome, descricao, data_inicio, data_fim) VALUES
('Sistema de Vendas Online', 'Projeto de e-commerce com carrinho de compras e pagamentos online.', '2025-02-01', '2025-07-30'),
('Aplicativo de Agenda Médica', 'Aplicativo para gerenciamento de consultas e pacientes.', '2025-03-10', '2025-09-15'),
('Plataforma de Cursos EAD', 'Sistema de cursos online com área do aluno e módulos de estudo.', '2025-01-20', '2025-08-05'),
('Sistema de Gestão Escolar', 'Plataforma para controle acadêmico e notas escolares.', '2025-04-01', '2025-11-20');


INSERT INTO pessoa (nome_completo, email) VALUES
('Ana Souza', 'ana.souza@email.com'),
('Bruno Lima', 'bruno.lima@email.com'),
('Carla Mendes', 'carla.mendes@email.com'),
('Daniel Oliveira', 'daniel.oliveira@email.com'),
('Fernanda Costa', 'fernanda.costa@email.com'),
('Gustavo Pereira', 'gustavo.pereira@email.com'),
('Helena Rocha', 'helena.rocha@email.com'),
('Igor Santos', 'igor.santos@email.com');




INSERT INTO papel (nome) VALUES
('Desenvolvedor'),
('Analista'),
('Testador'),
('Designer'),
('Gerente de Projetos'),
('DevOps');

// ALOCAÇÕES 

-- Projeto 1: Sistema de Vendas Online
INSERT INTO alocacao (projeto_id, pessoa_id, papel_id) VALUES
(1, 1, 1), -- Ana Souza – Desenvolvedor
(1, 2, 2), -- Bruno Lima – Analista
(1, 3, 3), -- Carla Mendes – Testador
(1, 4, 5); -- Daniel Oliveira – Gerente de Projetos

-- Projeto 2: Aplicativo de Agenda Médica
INSERT INTO alocacao (projeto_id, pessoa_id, papel_id) VALUES
(2, 5, 1), -- Fernanda Costa – Desenvolvedor
(2, 6, 6), -- Gustavo Pereira – DevOps
(2, 7, 4), -- Helena Rocha – Designer
(2, 4, 5); -- Daniel Oliveira – Gerente de Projetos

-- Projeto 3: Plataforma de Cursos EAD
INSERT INTO alocacao (projeto_id, pessoa_id, papel_id) VALUES
(3, 8, 1), -- Igor Santos – Desenvolvedor
(3, 1, 2), -- Ana Souza – Analista
(3, 3, 3), -- Carla Mendes – Testador
(3, 7, 4); -- Helena Rocha – Designer

-- Projeto 4: Sistema de Gestão Escolar
INSERT INTO alocacao (projeto_id, pessoa_id, papel_id) VALUES
(4, 2, 1), -- Bruno Lima – Desenvolvedor
(4, 5, 2), -- Fernanda Costa – Analista
(4, 6, 3), -- Gustavo Pereira – Testador
(4, 8, 6); -- Igor Santos – DevOps

// TAREFAS 
-- Projeto 1: Sistema de Vendas Online
INSERT INTO tarefa (projeto_id, titulo, descricao, status, responsavel_id) VALUES
(1, 'Criar tela de login', 'Desenvolver a tela inicial de login do sistema.', 'Planejada', 1),
(1, 'Modelar banco de dados', 'Criar modelo lógico e físico do banco.', 'Concluída', 2),
(1, 'Implementar carrinho de compras', 'Programar o fluxo de carrinho.', 'Em andamento', 1),
(1, 'Testar fluxo de pagamento', 'Validar pagamentos simulados.', 'Planejada', 3),
(1, 'Configurar ambiente de produção', 'Preparar o servidor e deploy inicial.', 'Em andamento', 4);

-- Projeto 2: Aplicativo de Agenda Médica
INSERT INTO tarefa (projeto_id, titulo, descricao, status, responsavel_id) VALUES
(2, 'Criar cadastro de pacientes', 'Tela e lógica de cadastro de pacientes.', 'Em andamento', 5),
(2, 'Implementar agendamento online', 'Permitir marcação de consultas online.', 'Planejada', 6),
(2, 'Criar protótipo de interface', 'Mockup e protótipo visual.', 'Concluída', 7),
(2, 'Validar integração com calendário', 'Conectar app com calendários externos.', 'Em andamento', 5);

-- Projeto 3: Plataforma de Cursos EAD
INSERT INTO tarefa (projeto_id, titulo, descricao, status, responsavel_id) VALUES
(3, 'Criar módulo de cadastro de cursos', 'Permitir cadastro de cursos no sistema.', 'Planejada', 8),
(3, 'Implementar área do aluno', 'Área restrita com acesso a conteúdos.', 'Em andamento', 1),
(3, 'Criar testes automáticos', 'Testes unitários e de integração.', 'Planejada', 3),
(3, 'Desenvolver design responsivo', 'Interface adaptável a dispositivos.', 'Em andamento', 7),
(3, 'Ajustar autenticação com e-mail', 'Corrigir login via email.', 'Concluída', 8);

-- Projeto 4: Sistema de Gestão Escolar
INSERT INTO tarefa (projeto_id, titulo, descricao, status, responsavel_id) VALUES
(4, 'Criar cadastro de alunos', 'Tela e lógica de cadastro de alunos.', 'Em andamento', 2),
(4, 'Desenvolver boletim online', 'Gerar boletim para cada aluno.', 'Planejada', 5),
(4, 'Testar módulo de presença', 'Validação do registro de presenças.', 'Planejada', 6),
(4, 'Implementar relatórios de notas', 'Gerar relatórios detalhados de notas.', 'Em andamento', 2);