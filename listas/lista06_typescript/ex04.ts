// Manipulação de arrays com TypeScript

function calcularMedia(numeros: number[]): number {
    const total = numeros.reduce((acc, numero) => acc + numero, 0); // soma todos os elementos do array
    return total / numeros.length;
}

console.log(calcularMedia([10, 20, 30, 40, 50.5, -60])); // ~ 15.083