"use strict";
// Enums e Funções
var DiasSemana;
(function (DiasSemana) {
    DiasSemana["Segunda"] = "Segunda-feira";
    DiasSemana["Terca"] = "Ter\u00E7a-feira";
    DiasSemana["Quarta"] = "Quarta-feira";
    DiasSemana["Quinta"] = "Quinta-feira";
    DiasSemana["Sexta"] = "Sexta-feira";
    DiasSemana["Sabado"] = "S\u00E1bado";
    DiasSemana["Domingo"] = "Domingo";
    DiasSemana["Pascoa"] = "P\u00E1scoa";
    DiasSemana["Tiradentes"] = "Tiradentes";
    DiasSemana["SaoJorge"] = "S\u00E3o Jorge";
})(DiasSemana || (DiasSemana = {}));
function ehFeriado(dia) {
    return dia === DiasSemana.Pascoa || dia === DiasSemana.Tiradentes || dia === DiasSemana.SaoJorge;
}
console.log(ehFeriado(DiasSemana.Pascoa)); // true
console.log(ehFeriado(DiasSemana.Quinta)); // false
console.log(ehFeriado(DiasSemana.Tiradentes)); // true
