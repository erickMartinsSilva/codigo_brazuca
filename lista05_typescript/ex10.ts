// Manipulação de Dados com Map e Filter

function filtrarPrecosAltos(precos: number[]): number[] {
    return precos.filter(preco => preco > 200);
}

console.log(filtrarPrecosAltos([50, 150, 200, 30].map(num => num * 2))); // [300, 400]