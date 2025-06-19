// função que verifica se dois números são múltiplos
function saoMultiplos(a,b) {
    if(a % b == 0 || b % a == 0) {
        return true;
    } else return false;
}

let a = 3;
let b = 6;
console.log(saoMultiplos(a,b)); // resultado esperado: true