// função que transforma as vogais numa string para asteriscos
function vogaisToAsterisk(str) {
    stringSeparada = str.split('');
    for(let i = 0; i < str.length; i++) {
        if(str[i].toLowerCase() == 'a' || str[i].toLowerCase() == 'e' || str[i].toLowerCase() == 'i' || str[i].toLowerCase() == 'o' || str[i].toLowerCase() == 'u') {
            stringSeparada[i] = '*';
        }
    }
    return stringSeparada.join('');
}

let str = "Ola mundo!";
console.log(vogaisToAsterisk(str)); // resultado esperado: "*l* m*nd*!"