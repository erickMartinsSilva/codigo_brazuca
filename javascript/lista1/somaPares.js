// função que soma todos os números pares numa lista
function somaPares(lista) {
    return lista.reduce((acc, current) => {
        return current % 2 == 0 ? acc + current : acc;
    }, 0)
}

let lista = [1,2,3,4,5];
console.log(somaPares(lista)); // resultado esperado: 2 + 4 = 6