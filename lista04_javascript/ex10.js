// função que retorna a quantidade de vogias de uma palavra
function qtdVogais(str) {
    let contador = 0;
    str.split('');
    for(let i = 0; i < str.length; i++) {
        if(str[i].toLowerCase() == 'a' || str[i].toLowerCase() == 'e' || str[i].toLowerCase() == 'i' || str[i].toLowerCase() == 'o' || str[i].toLowerCase() == 'u') {
            contador++;
        }
    }
    return contador;
}

let str = "Ola!";
console.log(qtdVogais(str)); // resultado esperado: 2