// função que verifica se um número está numa lista
function estaNaLista(a, lista) {
    return lista.includes(a);
}

let a = 2;
let lista = [1,2,3,4,5];
console.log(estaNaLista(a,lista)); // resultado esperado: true