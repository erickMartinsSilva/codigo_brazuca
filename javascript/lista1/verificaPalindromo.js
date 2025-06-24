// função que verifica se uma string é um palíndromo
function verificaPalindromo(str) {
    return str == str.split('').reverse().join('') ? true : false;
}

let str = "arara";
console.log(verificaPalindromo(str)); // resultado esperado: true
