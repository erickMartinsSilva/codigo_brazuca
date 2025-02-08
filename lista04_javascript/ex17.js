// função que organiza uma lista de números em ordem crescente utilizando o algoritmo de bubble sort
function ordenaLista(lista) {
    let aux;
    for(let i = 0; i < lista.length; i++) {
        for(let j = i+1; j < lista.length; j++) {
            if(lista[i] > lista[j]) {
                aux = lista[i];
                lista[i] = lista[j];
                lista[j] = aux;
            }
        }
    }
}

let lista = [3, 2, 1];

ordenaLista(lista);
console.log(lista);