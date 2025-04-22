// Tipagem básica

let nome: string = "Erick";
let idade: number = 25;
let ativo: boolean = true;
let hobbies: string[] = ["Leitura", "Jogos eletrônicos", "Música"];
let endereco: {
    rua: string;
    numero: number;
    bairro: string;
    cidade: string;
    estado: string;
} = {
    rua: "Avenida Monsenhor Félix",
    numero: 1502,
    bairro: "Irajá",
    cidade: "Rio de Janeiro",
    estado: "RJ"
};

console.log(`Nome: ${nome}, Idade: ${idade}, Ativo: ${ativo}`);
console.log(`Hobbies: ${hobbies.join(", ")}`);
console.log(`Endereço: ${endereco.rua}, ${endereco.numero} - ${endereco.bairro}, ${endereco.cidade}, ${endereco.estado}`);
