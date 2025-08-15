const operacaoMatematica = (num1, opera, num2) =>{
    const expressao = `${num1}${opera}${num2}`;

    const resultado = eval(expressao);

    document.write(`<p class="texto">O resultado da operação de ${num1} ${opera} ${num2} é igual a: ${resultado}</p>`)
};

const primeiroNum = Number(prompt("DIgite o primeiro número: "));
const escolhaOpera = prompt('Digite a operação a ser realizada: "+", "-", "*" ou "/"');
const segundoNum = Number(prompt("Digite o segundo número: "));

operacaoMatematica(primeiroNum, escolhaOpera, segundoNum);