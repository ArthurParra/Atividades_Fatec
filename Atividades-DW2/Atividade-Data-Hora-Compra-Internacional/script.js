// Exibir a data e hora atual
const data_atual = new Date();
document.write(`<p>Data e Hora: ${data_atual.toLocaleString()}</p>`);

// Criando variavel para Compra Internacional
let compra_internacional = 500.75;
document.write(
  `<p>Valor da compra internacional: $${compra_internacional.toFixed(2)}</p>`
);

// Conversão para Real (BRL) supondo que 1 USD = 5.20 BRL
let taxa_cambio = 5.2;
let valor_reais = compra_internacional * taxa_cambio;
document.write(`<p>Valor em Reais R$${valor_reais.toFixed(2)}</p>`);

// calcular a data de entrega a partir de 12 dias apos a compra
let dias_entrega = 12;
let data_entrega = new Date();
data_entrega.setDate(data_atual.getDate() + dias_entrega);

document.write(
  `<p>Data estimada para entrega de: ${data_entrega.toLocaleDateString()}`
);
