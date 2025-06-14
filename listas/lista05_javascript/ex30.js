// função que retorna a quantidade de números ímpares numa lista
function qtdNumerosImpares(lista) {
    let contador = 0;
    for(let i = 0; i < lista.length; i++) {
        if(lista[i] % 2 != 0) {
            contador++;
        }
    }
    return contador;
}

let lista = [1,2,3,4,5];
console.log(qtdNumerosImpares(lista)); // resultado esperado: 3