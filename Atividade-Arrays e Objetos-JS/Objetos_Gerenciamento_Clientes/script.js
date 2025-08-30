//criando uma variavel atribuido a um objeto
const pessoa = {
  constructor(nome, endereco, cpf) {
    this.nome = nome;
    this.endereco = endereco;
    this.cpf = cpf;
  },
};
const ListaClientes = [
  {
    nome: "João Vitor",
    endereco: "Rua Vereador Aércio, 123",
    cpf: 12345678901,
  },
  {
    nome: "Elias Pinheiro",
    endereco: "Rua Nadador Franco, 456",
    cpf: 23456789012,
  },
  {
    nome: "Myrella Castellani",
    endereco: "Rua Reverendo Silva, 789",
    cpf: 34567890123,
  },
];
ListaClientes.forEach((pessoa) => {
  document.write(`
        <p>
            Nome do Cliente: ${pessoa.nome}<br>
            Endereço: ${pessoa.endereco}<br>
            CPF: ${pessoa.cpf}<br>
        </p>
        `);
});
