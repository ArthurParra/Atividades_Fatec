// Importando o Express
import express from "express";
// carregando a variavel router no express.Router() que é responsavel por gerenciar as rotas da aplicação.
const router = express.Router();
import Cliente from "../models/Cliente.js";

// lista todos os clientes
router.get("/clientes", async (req, res) => {
  try {
    const clientes = await Cliente.findAll({ order: [["id", "ASC"]] });
    res.render("clientes", { clientes });
  } catch (error) {
    console.error(error);
    res.status(500).send("Erro ao buscar clientes");
  }
});

// form para novo cliente
router.get("/clientes/new", (req, res) => {
  res.render("clientes_form", { cliente: null });
});

// criar cliente
router.post("/clientes", async (req, res) => {
  try {
    const { nome, cpf, email, telefone, endereco } = req.body;
    await Cliente.create({ nome, cpf, email, telefone, endereco });
    res.redirect("/clientes");
  } catch (error) {
    console.error(error);
    res.status(500).send("Erro ao criar cliente");
  }
});

// form para editar cliente
router.get("/clientes/:id/edit", async (req, res) => {
  try {
    const cliente = await Cliente.findByPk(req.params.id);
    if (!cliente) return res.status(404).send("Cliente não encontrado");
    res.render("clientes_form", { cliente });
  } catch (error) {
    console.error(error);
    res.status(500).send("Erro ao buscar cliente");
  }
});

// atualizar cliente
router.post("/clientes/:id/update", async (req, res) => {
  try {
    const cliente = await Cliente.findByPk(req.params.id);
    if (!cliente) return res.status(404).send("Cliente não encontrado");
    const { nome, cpf, email, telefone, endereco } = req.body;
    await cliente.update({ nome, cpf, email, telefone, endereco });
    res.redirect("/clientes");
  } catch (error) {
    console.error(error);
    res.status(500).send("Erro ao atualizar cliente");
  }
});

// deletar cliente
router.post("/clientes/:id/delete", async (req, res) => {
  try {
    const cliente = await Cliente.findByPk(req.params.id);
    if (!cliente) return res.status(404).send("Cliente não encontrado");
    await cliente.destroy();
    res.redirect("/clientes");
  } catch (error) {
    console.error(error);
    res.status(500).send("Erro ao deletar cliente");
  }
});

// exportando o objeto router.
export default router;
