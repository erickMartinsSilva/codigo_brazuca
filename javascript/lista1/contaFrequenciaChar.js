// função que retorna quantas vezes um caractere aparece numa string

// função que divide a string num array de chars, filtra o array para conter apenas as ocorrências da letra e então
// retorna o tamanho do array filtrado
function frequencia(char,str) {
    return str.split('').filter(item => item == char).length;
}

let str = "Banana";
let char = 'a';
console.log(frequencia(char,str)); // resultado esperado: 3