// função que retorna a quantidade de vogias de uma palavra

function qtdVogais(str) {
    const vogais = ['a','e','i','o','u']

    return str.toLowerCase().split('').filter(item => vogais.includes(item)).length;
}

let str = "Ola!";
console.log(qtdVogais(str)); // resultado esperado: 2