// função que retorna a lista de divisores de um número
function divisores(a) {
    let divisores = [];
    for(let i = a; i > 0; i--) {
        if(a % i == 0) {
            divisores.push(i);
        }
    }
    return divisores;
}

let a = 20;
console.log(divisores(a)); // resultado esperado: [20, 10, 5, 4, 2, 1]