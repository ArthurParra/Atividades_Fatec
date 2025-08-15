const calcularMetade = function(numero) {
    return numero / 2;
};

const numero = Number(prompt("Digite um número:"));
const resultado = calcularMetade(Number(numero));
document.write(`<p class="texto">A metade de ${numero} é ${resultado}</p>`);
