// função que remove espaços de uma string
function removerEspacos(str) {
    return str.split(' ').join('');
}

let str = "Hello world!";
console.log(removerEspacos(str)); // resultado esperado: "Helloworld!"