===== DESAFIO 1: Desvendando o código secreto da Polkadot =====

O código funciona da seguinte forma:

No início, uma variável "total" é declarada e inicializada para uso futuro. Logo depois, o programa pede para o 
usuário entrar com dois números. O primeiro número escrito será utilizado como início de um intervalo de números, enquanto o
segundo será utilizado como fim do mesmo intervalo de números.

Após ter o intervalo definido, ele será utilizado como parâmetro em uma estrutura de repetição for, a fim de percorrer os
números presentes no intervalo. Cada número sofrerá três testes condicionais, sendo estes, respectivamente: Se o número for
múltiplo de 3, ele será somado à variável "total" declarada no início do código. Se o número for múltiplo de 5, ele será 
subtraído da variável "total". Por fim, se o número for múltiplo de 3 e de 5 ao mesmo tempo, utilizaremos "continue" para dar
sequência à estrutura de repetição, pois aquele número não será utilizado em nossas operações.

Chegando ao fim do intervalo, o programa sai da estrutura de repetição for e imprime na tela o valor total das operações
efetuadas dentro daquele intervalo.
