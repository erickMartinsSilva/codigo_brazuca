// função que retorna quantas vezes um caractere aparece numa string
function frequencia(char,str) {
    let contador = 0;
    str.split('');
    for(let i = 0; i < str.length; i++) {
        if(str[i] == char) {
            contador++;
        }
    }
    return contador;
}

let str = "Banana";
let char = 'a';
console.log(frequencia(char,str)); // resultado esperado: 3