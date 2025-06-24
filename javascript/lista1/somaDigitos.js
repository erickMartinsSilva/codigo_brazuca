// função que soma os dígitos de um número
function somaDigitos(num) {
    let algarismos = num.toString().split('').map(Number);

    return algarismos.reduce((acc, current) => acc + current, 0)
}

let num = 12345;
console.log(somaDigitos(num)); // resultado esperado: 15