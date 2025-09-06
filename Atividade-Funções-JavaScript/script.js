//Primeira Lista de Atividades

const user = prompt(`Ola! Por favor me informe seu nome:`);

function saudacaoPersoalizada(user) {
  document.write(`<p class="texto">Seja Bem vindo(a) ${user}!</p>`);
  document.write(`<p class="texto">Esta é a super Calculadora Universal!</p>`);
}
saudacaoPersoalizada(user);

const operacaoMatematica = (num1, opera, num2) => {
  const expressao = `${num1}${opera}${num2}`;
  const resultado = eval(expressao);

  document.write(
    `<p class="texto">O resultado da operação de ${num1} ${opera} ${num2} é  igual a: ${resultado}</p>`
  );
};

const primeiroNum = Number(prompt(`Informe o primeiro número a ser usado:`));
const segundoNum = Number(prompt(`Informe o segundo número a ser usado:`));
const escolhaOpera = prompt(
  `Agora informe a operação desejada como "+", "-", "*" ou "/":`
);

operacaoMatematica(primeiroNum, escolhaOpera, segundoNum);

const calcularDobro = function (num) {
  return num * 2;
};

const numeroDobro = Number(
  prompt(`Agora, informe o número que deseja saber o dobro: `)
);
const resultDoboro = calcularDobro(Number(numeroDobro));
document.write(
  `<p class="texto">O Dobro de ${numeroDobro} é: ${resultDoboro} </p>`
);

const calcularMetade = function (num) {
  return num / 2;
};

const numero = Number(
  prompt(`Agora, informe o número que deseja saber a Metade: `)
);
const resultMetade = calcularMetade(Number(numero));
document.write(
  `<p class="texto">A Metade de ${numero} é: ${resultMetade} </p>`
);

(() => {
  document.write(
    `<P class="texto">A Calculadora universal está pronta e funcionando como esperado! Volte Sempre :) </p>`
  );
})();
