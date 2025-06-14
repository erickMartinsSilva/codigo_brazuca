// Tipos Personalizados (Union Types)

function formatarEntrada(valor: string | number | boolean): string | number | boolean {
    switch(typeof valor) {
        case "string": return valor.toUpperCase();
        case "number": return valor * 10;
        case "boolean": return !valor;
    }
}

console.log(formatarEntrada("typescript")); // "TYPESCRIPT"
console.log(formatarEntrada(5)); // 50
console.log(formatarEntrada(true)); // false