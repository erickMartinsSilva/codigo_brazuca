"use strict";
// Tipagem básica
let nome = "Erick";
let idade = 25;
let ativo = true;
let hobbies = ["Leitura", "Jogos eletrônicos", "Música"];
let endereco = {
    rua: "Avenida Monsenhor Félix",
    numero: 1502,
    bairro: "Irajá",
    cidade: "Rio de Janeiro",
    estado: "RJ"
};
console.log(`Nome: ${nome}, Idade: ${idade}, Ativo: ${ativo}`);
console.log(`Hobbies: ${hobbies.join(", ")}`);
console.log(`Endereço: ${endereco.rua}, ${endereco.numero} - ${endereco.bairro}, ${endereco.cidade}, ${endereco.estado}`);
