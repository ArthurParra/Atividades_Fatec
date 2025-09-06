//Segunda lista de atividades:

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
document.write(`<h2>Esta é a nossa lista de clientes: </h2>`)
ListaClientes.forEach((pessoa) => {
  document.write(`
        <p>
            Nome do Cliente: ${pessoa.nome}<br>
            Endereço: ${pessoa.endereco}<br>
            CPF: ${pessoa.cpf}<br><br>
        </p>
        `);
});

ListaClientes.push({
  nome: "Mike Star",
  endereco: "Rua Mario Games da Silva, 012",
  cpf: 27439190493,
});

document.write(`<h2>Esta é a nova lista de Clientes: </h2>`)

ListaClientes.forEach((pessoa) => {
  document.write(`
        <p>
            Nome do Cliente: ${pessoa.nome}<br>
            Endereço: ${pessoa.endereco}<br>
            CPF: ${pessoa.cpf}<br><br>
        </p>
        `);
});

ListaClientes.unshift({
  nome: "Layne Stanley",
  endereco: "Rua Calçada do Rock, 234",
  cpf: 28402639052,
});

document.write(`<h2>Esta é a nova lista de Clientes: </h2>`)

ListaClientes.forEach((pessoa) => {
  document.write(`
        <p>
            Nome do Cliente: ${pessoa.nome}<br>
            Endereço: ${pessoa.endereco}<br>
            CPF: ${pessoa.cpf}<br><br>
        </p>
        `);
});