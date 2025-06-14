programa {
  funcao inicio() {
    inteiro num, fatorial = 1
    escreva("Insira um numero: ")
    leia(num)
    para(inteiro i = num; i > 0; i--) {
      fatorial *= i
    }
    escreva(num,"! = ", fatorial)
  }
}
