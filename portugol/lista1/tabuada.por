programa {
  funcao inicio() {
    inteiro num
    escreva("Insira um numero: ")
    leia(num)
    para(inteiro i = 1; i <= 10; i++) {
      escreva(num, " * ", i," = ", num*i, "\n")
    }
  }
}
