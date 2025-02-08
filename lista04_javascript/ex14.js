// função que remove espaços de uma string
function removerEspacos(str) {
    let strNova = str.split(' ').join('');
    return strNova;
}

let str = "Hello world!";
console.log(removerEspacos(str)); // resultado esperado: "Helloworld!"