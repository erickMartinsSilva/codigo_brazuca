"use strict";
// Classes e Herança
class Animal {
    constructor(nome, som) {
        this.nome = nome;
        this.som = som;
    }
    emitirSom() {
        {
            return `${this.nome} faz ${this.som}`;
        }
    }
}
class Cachorro extends Animal {
    constructor(nome, som, raca) {
        super(nome, som); // chama o constructor da classe pai (nesse caso, Animal)
        this.raca = raca;
    }
    latirForte(raca) {
        raca == "Pitbull" ? (this.som = "ruff ruff") : (this.som = "au au");
        return this.emitirSom();
    }
}
const rex = new Cachorro("Rex", "au au", "Labrador");
console.log(rex.emitirSom());
console.log(`Raça: ${rex.raca}`);
const thor = new Cachorro("Thor", "au au", "Pitbull");
console.log(thor.latirForte(thor.raca));
console.log(`Raça: ${thor.raca}`);
