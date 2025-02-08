// função que retorna a raiz de quadrada de um número ou uma mensagem de erro se o número for negativo 
function raizQuadrada(a) {
    if(a<0) {
        return -1;
    }
    else {
        return a ** 0.5;
    }
}

let a = 25;
if(raizQuadrada(a) != -1) {
    console.log(raizQuadrada(a)); // resultado esperado: 5
} else console.log("Erro! Número negativo")