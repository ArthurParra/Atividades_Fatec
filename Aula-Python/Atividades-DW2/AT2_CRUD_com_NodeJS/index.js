// const express = require("express");
// //importando o Express (framework):
import express from "express"; // ES6 Modules

// importanto sequelize:
import connection from "./config/sequelizeConfig.js";

const app = express(); //Iniciando o Express na vaiavel "APP":

// importando os controllers (onde estão as rotas e onde é tratadoas requisições)
import ClientesController from "./controllers/ClientesController.js";
// import PedidosController from "./controllers/PedidosController.js";
import AlbumControllers from "./controllers/AlbumControllers.js";

// configurando o EJS:
app.set("view engine", "ejs");

// definindo a pasta PUBLIC para Arquivos Estáticos
app.use(express.static("public"));

// middleware para ler body de formulários
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Definindo o uso das rotas que estão nos controllers
app.use("/", ClientesController);
// app.use("/", PedidosController)
app.use("/", AlbumControllers);

//criando a primeira rota do site (rota principal):
// REQ = trata a REQUISIÇÂO
// RES = trata a RESPOSTA
app.get("/", (req, res) => {
  res.render("index");
});

//rota de perfil
// :user -> É um parametro da rota (OBRIGATORIO)
// :user? -> É um parametro da rota (OPCIONAL)
// Perfil removido — o app agora expõe apenas Clientes e Álbuns

// Iniciando o servidor HTTP apenas após criar DB e sincronizar tabelas
const port = 8080; //O servidor escutará na porta 8080

connection
  .query(`CREATE DATABASE IF NOT EXISTS atv2_avaliativa`)
  .then(() => {
    console.log("Banco de dados criado com sucesso");
  // sincroniza tabelas (cria tabelas definidas pelos models)
  // usamos `alter: true` para ajustar o esquema da tabela existente
  // adicionando/alterando colunas para ficar compatível com os models.
  // Em ambiente de produção prefira migrations; aqui é para desenvolvimento.
  return connection.sync({ alter: true });
  })
  .then(() => {
    console.log("Tabelas sincronizadas");

    // Inicia o servidor somente depois que DB estiver pronto
    app.listen(port, (error) => {
      if (error) {
        console.log(`Não foi possivel iniciar o servidor. Ocorreu um ERRO! ${error}`);
      } else {
        console.log(`Servidor iniciado com sucesso em:\n            http://localhost:${port}`);
      }
    });
  })
  .catch((error) => {
    console.error("Erro ao preparar o banco de dados:", error);
    process.exit(1);
  });
