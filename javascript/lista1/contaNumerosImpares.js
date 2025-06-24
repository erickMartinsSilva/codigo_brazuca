// função que retorna a quantidade de números ímpares numa lista
function qtdNumerosImpares(lista) {
    return lista.filter(item => item % 2 == 0).length;
}

let lista = [1,2,3,4,5];
console.log(qtdNumerosImpares(lista)); // resultado esperado: 2