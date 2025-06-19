"use strict";
// Interface para tipagem de objetos
function filtrarDisponiveis(produtos) {
    return produtos.filter(produto => produto.disponivel);
}
function filtrarHardware(produtos) {
    return produtos.filter(produto => produto.categoria == "Hardware");
}
const produtos = [
    { nome: "Teclado", preco: 100, disponivel: true, categoria: "Periférico" },
    { nome: "Mouse", preco: 50, disponivel: false, categoria: "Periférico" },
    { nome: "Monitor", preco: 300, disponivel: true, categoria: "Periférico" },
    { nome: "Processador", preco: 700, disponivel: true, categoria: "Hardware" },
    { nome: "Placa de vídeo", preco: 1000, disponivel: false, categoria: "Hardware" }
];
console.log(filtrarDisponiveis(produtos));
console.log(filtrarHardware(produtos));
