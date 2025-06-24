// função que retorna se um número é par ou ímpar
function parOuImpar(a) {
    return a % 2 == 0 ? "Par" : "Ímpar";
}

let a = 3;
console.log(parOuImpar(a)); // resultado esperado: Impar