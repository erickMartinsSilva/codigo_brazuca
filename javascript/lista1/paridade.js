// função que retorna se um número é par ou ímpar
function parOuImpar(a) {
    if(a % 2 == 0) {
        return "Par";
    } else return "Impar";
}

let a = 3;
console.log(parOuImpar(a)); // resultado esperado: Impar