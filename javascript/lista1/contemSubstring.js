// função que valida se uma string contém uma determinada substring
function contemSubstring(str, substr) {
    return str.includes(substr);
}

let str = "Ola, mundo!";
let substr = "mundo";
console.log(contemSubstring(str,substr)); // resultado esperado: true