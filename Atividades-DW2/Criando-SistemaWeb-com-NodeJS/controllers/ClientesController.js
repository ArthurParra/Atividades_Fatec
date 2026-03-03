// Importando o Express
import express from "express";
// carregando a variavel router no express.Router() que é responsavel por gerenciar as rotas da aplicação.
const router = express.Router();

// criando a rota de clientes
router.get("/clientes", (req, res) => {
  const clientes = [
    {
      nome: "Shimada",
      CPF: "123.456.789-22",
      endereco: "Rua Dona Gertrudes, 190",
    },
    {
      nome: "Myrella",
      CPF: "125.456.134-45",
      endereco: "Rua Marcelo Gomes, 231",
    },
    {
      nome: "Matt",
      CPF: "879.768.435-87",
      endereco: "Rua Pindamonhngaba, 600",
    },
    {
      nome: "Ravi",
      CPF: "132.542.645-11",
      endereco: "Rua Lero Covas, 32",
    },
    {
      nome: "Ingrid",
      CPF: "243.645.234-87",
      endereco: "Rua Marcelo Barros, 534",
    },
  ];
  res.render("clientes", {
    clientes: clientes,
  });
});

// exportando o objeto router.
export default router;
