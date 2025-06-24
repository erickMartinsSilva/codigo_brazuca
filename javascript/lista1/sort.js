// função que organiza uma lista de números em ordem crescente utilizando o algoritmo de bubble sort

function listaOrdenada(lista) {
    return lista.sort((a,b) => a - b);
}

let lista = [3, 2, 1];

console.log(listaOrdenada(lista))