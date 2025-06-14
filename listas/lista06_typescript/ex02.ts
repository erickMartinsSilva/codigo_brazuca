// Função com tipagem e parâmetro opcional

function saudacao(nome: string, idade?: number, ocupacao?: string, localOcupacao?: string): string {
    return idade ? (
        ocupacao ? (
            localOcupacao? (
                `Olá, ${nome}! Você tem ${idade} anos e é um ${ocupacao} em ${localOcupacao}.`
            ) : (
                `Olá, ${nome}! Você tem ${idade} anos e é um ${ocupacao}.`
            )
        ) : (
            `Olá, ${nome}! Você tem ${idade} anos.`
        )
    ) : (
        `Olá, ${nome}!`
    )
}

console.log(saudacao("Alice"));
console.log(saudacao("Bob",30));
console.log(saudacao("Erick",19,"Estudante"));
console.log(saudacao("Erick",19,"Estudante","Cefet/RJ"));