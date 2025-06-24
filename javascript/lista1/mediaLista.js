// função que retorna a média de uma lista de números
function media(lista) {
    return lista.reduce((acc, current) => acc + current, 0)/lista.length;
}

let lista = [2, 3, 4, 5, 6, 7, 8];
console.log(media(lista)); // resultado esperado: 5