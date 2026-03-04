import express from "express";
const router = express.Router();

// ROTA de produtos
router.get("/produtos", (req, res) => {
  // const produtos = ["Computador", "Celular", "Tablet", "Notebook"];

  //array de objetos com os produtos:
  const produtos = [
    { nome: "Celular", preco: 3000 },
    { nome: "Computador", preco: 5000 },
    { nome: "Tablet", preco: 2500 },
    { nome: "Notebook", preco: 3000 },
  ];
  res.render("produtos", {
    produtos: produtos,
  });
});

export default router;
