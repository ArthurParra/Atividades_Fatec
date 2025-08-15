const calcularDobro = function(numero) {
    return numero * 2;
};

const numero = Number(prompt("Digite um número:"));
const resultado = calcularDobro(Number(numero));
document.write(`<p class="texto">O dobro de ${numero} é ${resultado}</p>`);
