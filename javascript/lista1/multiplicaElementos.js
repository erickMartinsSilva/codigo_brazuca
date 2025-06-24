// função que multiplica todos os elementos de uma lista
function multiplicaElementos(lista) {
    return lista.reduce((acc, current) => acc * current, 1);
}

let lista = [1,2,3,4,5];
console.log(multiplicaElementos(lista)); // resultado esperado: 120