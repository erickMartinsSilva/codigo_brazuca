// função que verifica se uma string é um palíndromo
function verificaPalindromo(str) {
    let strInversa = str.split('').reverse().join('');
    if(str == strInversa) {
        return true;
    } else return false;
}

let str = "arara";
console.log(verificaPalindromo(str)); // resultado esperado: true
