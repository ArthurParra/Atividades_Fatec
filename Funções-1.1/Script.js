const user = prompt(`Olá! Qual seu nome?`)

function saudacaoPersoalizada(user){
    document.write(`<h1 class="texto">Prazer em conhecer você ${user}!</h1>`);
    document.write(`<h3 class="texto">Bem Vindo(a) a Caculadora Universal!</h3>`)
}
saudacaoPersoalizada(user);