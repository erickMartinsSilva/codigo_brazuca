// função que soma os dígitos de um número
function somaDigitos(num) {
    let soma = 0;
    let algarismos = num.toString().split('').map(Number);
    for(let i = 0; i < algarismos.length; i++) {
        soma += algarismos[i];
    }
    return soma;
}

let num = 12345;
console.log(somaDigitos(num)); // resultado esperado: 15