// função que retorna true se um número é primo e false se não for
function primo(a) {
    if(a <= 1) {
        return false;
    }
    for(let i = 3; i < (Math.pow(a,0.5)+1); i++) {
        if(a % i == 0) {
            return false;
        }
    }
    return true;
}

let a = 2;
console.log(primo(a)); // resultado esperado: true