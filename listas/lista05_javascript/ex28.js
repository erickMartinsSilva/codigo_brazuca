// função que multiplica todos os elementos de uma lista
function multiplicaElementos(lista) {
    let mult = 1;
    for(let i = 0; i < lista.length; i++) {
        mult *= lista[i];
    }
    return mult;
}

let lista = [1,2,3,4,5];
console.log(multiplicaElementos(lista)); // resultado esperado: 120