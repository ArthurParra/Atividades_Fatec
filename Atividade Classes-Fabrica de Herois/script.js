// Atividade Classes: Fabrica de Herois
class Heroi {
    constructor(nome, vida, velocidade, forca) {
        this.nome = nome;
        this.vida = vida;
        this.velocidade = velocidade;
        this.forca = forca;
    }

    correr() {
        return `${this.nome} está correndo!`;
    }
    andar() {
        return `${this.nome} está andando!`;
    }
    atacar() {
        return `${this.nome} está atacando!`;
    }
    defender() {
        return `${this.nome} está se defendendo!`;
    }
}

class HomemAranha extends Heroi {
    constructor(nome, vida, velocidade, forca, teia) {
        super(nome, vida, velocidade, forca);
        this.teia = teia; 
    }

    sentidoAranha() {
        return `${this.nome} <p>Detectou um perigo com seu sentido aranha!</p>`;
    }
}

class Superman extends Heroi {
    constructor(nome, vida, velocidade, forca, podeVoar) {
        super(nome, vida, velocidade, forca);
        this.podeVoar = podeVoar; 
    }

    visaoCalor() {
        return `${this.nome} <p>Está usando sua visão de calor!</p>`;
    }
}

class Batman extends Heroi {
    constructor(nome, vida, velocidade, forca, esconder) {
        super(nome, vida, velocidade, forca);
        this.esconder = esconder; 
    }

    investigar() {
        return `${this.nome} <p>Está investigando um crime!</p>`;
    }
}

let homemAranha = new HomemAranha(`<p>Homem-Aranha`, 100, 80, 70, 1);
let superman = new Superman(`<p>Superman`, 200, 90, 100, 1);
let batman = new Batman(`<p>Batman`, 120, 70, 85, 0);

document.write(`<h3>Testando os Heróis:</h3>`);
document.write(homemAranha.sentidoAranha() + "<br>");
document.write(superman.visaoCalor() + "<br>");
document.write(batman.investigar() + "<br>");
document.write(batman.correr() + "<br>");