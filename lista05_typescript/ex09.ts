// Trabalhando com Generics

function reverterArray<T>(items: T[]): T[] {
    return items.reverse();
}

console.log(reverterArray([1,2,3])); // [3,2,1]
console.log(reverterArray(["a", "b", "c"])) // ["c", "b", "a"]