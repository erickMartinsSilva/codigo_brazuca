// Enums e Funções

enum DiasSemana {
    Segunda = "Segunda-feira",
    Terca = "Terça-feira",
    Quarta = "Quarta-feira",
    Quinta = "Quinta-feira",
    Sexta = "Sexta-feira",
    Sabado = "Sábado",
    Domingo = "Domingo",
    Pascoa = "Páscoa",
    Tiradentes = "Tiradentes",
    SaoJorge = "São Jorge"
}

function ehFeriado(dia: DiasSemana): boolean {
    return dia === DiasSemana.Pascoa || dia === DiasSemana.Tiradentes || dia === DiasSemana.SaoJorge;
}

console.log(ehFeriado(DiasSemana.Pascoa)); // true
console.log(ehFeriado(DiasSemana.Quinta)); // false
console.log(ehFeriado(DiasSemana.Tiradentes)); // true