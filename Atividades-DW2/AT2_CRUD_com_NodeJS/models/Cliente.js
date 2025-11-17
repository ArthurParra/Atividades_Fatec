import connection from "../config/sequelizeConfig.js";
import Sequelize from "sequelize";

const Cliente = connection.define(
    "Cliente",
    {
        nome: {
            type: Sequelize.STRING,
            allowNull: false,
        },
        cpf: {
            type: Sequelize.STRING,
            allowNull: false,
            unique: true,
        },
        email: {
            type: Sequelize.STRING,
            allowNull: true,
        },
        telefone: {
            type: Sequelize.STRING,
            allowNull: true,
        },
        endereco: {
            type: Sequelize.STRING,
            allowNull: true,
        },
    },
    {
        tableName: "clientes",
        timestamps: true,
    }
);

export default Cliente;