// função que transforma as vogais numa string para asteriscos
function vogaisToAsterisk(str) {
    const vogais = ['a', 'e', 'i', 'o', 'u']
    let splitStr = str.toLowerCase().split('')

    for(let i = 0; i < splitStr.length; i++) {
        if(vogais.includes(splitStr[i])) {
            splitStr[i] = '*'
        }
    }
    return splitStr.join('');
}

let str = "Ola mundo!";
console.log(vogaisToAsterisk(str)); // resultado esperado: "*l* m*nd*!"