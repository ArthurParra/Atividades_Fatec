// const express = require("express");
// //importando o Express (framework):
import express from "express"; // ES6 Modules

const app = express(); //Iniciando o Express na vaiavel "APP":

// importando os controllers (onde estão as rotas e onde é tratadoas requisições)
import ClientesController from "./controllers/ClientesController.js";
// import PedidosController from "./controllers/PedidosController.js";
import ProdutosController from "./controllers/ProdutosController.js";

// configurando o EJS:
app.set("view engine", "ejs");

// definindo a pasta PUBLIC para Arquivos Estáticos
app.use(express.static("public"));

// Definindo o uso das rotas que estão nos controllers
app.use("/", ClientesController);
// app.use("/", PedidosController)
app.use("/", ProdutosController);

//criando a primeira rota do site (rota principal):
// REQ = trata a REQUISIÇÂO
// RES = trata a RESPOSTA
app.get("/", (req, res) => {
  res.render("index");
});

//rota de perfil
// :user -> É um parametro da rota (OBRIGATORIO)
// :user? -> É um parametro da rota (OPCIONAL)
app.get("/perfil/:user", (req, res) => {
  //criando a variavel que sera enviada para a pagina
  const user = req.params.user;

  res.render("perfil", {
    //enviando variavei para a pagina:
    user: user,
  });
});

//Iniciando o servidor HTTP
const port = 8080; //O servidor escutará na porta 8080

app.listen(
  port,
  (
    error //o "error" ira capturar o erro que acontecer
  ) => {
    if (error) {
      console.log(
        `Não foi possivel iniciar o servidor. Ocorreu um ERRO! ${error}`
      );
    } else {
      console.log(`Servidor iniciado com sucesso em:
            http://localhost:${port}`);
    }
  }
);
