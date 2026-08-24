import { Request, Response } from 'express';
import { User } from '../models/User';

export class UserController {
  // GET /api/users - Listar todos os usuarios
  public static async index(req: Request, res: Response): Promise<Response> {
    try {
      const users = await User.findAll({
        attributes: ['id', 'nome', 'email', 'createdAt', 'updatedAt']
      });
      return res.status(200).json(users);
    } catch (error: any) {
      return res.status(500).json({ erro: 'Erro ao listar usuarios.', detalhe: error.message });
    }
  }

  // GET /api/users/:id - Buscar um usuario por ID
  public static async show(req: Request, res: Response): Promise<Response> {
    try {
      const { id } = req.params;
      const user = await User.findByPk(Number(id), {
        attributes: ['id', 'nome', 'email', 'createdAt', 'updatedAt']
      });

      if (!user) {
        return res.status(404).json({ erro: 'Usuario nao encontrado.' });
      }

      return res.status(200).json(user);
    } catch (error: any) {
      return res.status(500).json({ erro: 'Erro ao buscar usuario.', detalhe: error.message });
    }
  }

  // POST /api/users - Cadastrar um novo usuario
  public static async create(req: Request, res: Response): Promise<Response> {
    try {
      const { nome, email, senha_hash } = req.body;

      if (!nome || !email || !senha_hash) {
        return res.status(400).json({ erro: 'Os campos nome, email e senha_hash sao obrigatorios.' });
      }

      const novoUser = await User.create({ nome, email, senha_hash });

      // Retorna 201 Created com os dados do usuario criado
      return res.status(201).json({
        id: novoUser.id,
        nome: novoUser.nome,
        email: novoUser.email,
        createdAt: novoUser.createdAt
      });
    } catch (error: any) {
      return res.status(500).json({ erro: 'Erro ao cadastrar usuario.', detalhe: error.message });
    }
  }

  // PUT /api/users/:id - Atualizar um usuario existente
  public static async update(req: Request, res: Response): Promise<Response> {
    try {
      const { id } = req.params;
      const { nome, email } = req.body;

      const user = await User.findByPk(Number(id));

      if (!user) {
        return res.status(404).json({ erro: 'Usuario nao encontrado para atualizacao.' });
      }

      // Atualiza os campos fornecidos
      if (nome) user.nome = nome;
      if (email) user.email = email;

      await user.save();

      return res.status(200).json({
        id: user.id,
        nome: user.nome,
        email: user.email,
        updatedAt: user.updatedAt
      });
    } catch (error: any) {
      return res.status(500).json({ erro: 'Erro ao atualizar usuario.', detalhe: error.message });
    }
  }

  // DELETE /api/users/:id - Remover um usuario
  public static async delete(req: Request, res: Response): Promise<Response> {
    try {
      const { id } = req.params;

      const user = await User.findByPk(Number(id));

      if (!user) {
        return res.status(404).json({ erro: 'Usuario nao encontrado para exclusao.' });
      }

      await user.destroy();

      // 204 No Content: operacao concluida com sucesso sem conteudo de retorno
      return res.status(204).send();
    } catch (error: any) {
      return res.status(500).json({ erro: 'Erro ao excluir usuario.', detalhe: error.message });
    }
  }
}