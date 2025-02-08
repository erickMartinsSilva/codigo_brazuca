// função que verifica se uma lista está em ordem crescente
function estaEmOrdemCrescente(lista) {
    for(let i = 0; i < lista.length; i++) {
        if(lista[i] > lista[i+1]) {
            return false;
        }
    }
    return true;
}

let lista = [1,3,2];
console.log(estaEmOrdemCrescente(lista)); // resultado esperado: false