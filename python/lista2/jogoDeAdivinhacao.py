# simples jogo de adivinhação onde o jogador precisa adivinhar que número entre 1 e 100 foi escolhido pelo programa

import random

numero = random.randint(1, 100)
print("Estou pensando em um número entre 1 e 100. Você consegue adivinhá-lo?")

tentativa = 0
while(tentativa != numero):
  tentativa = int(input())
  if (tentativa > numero):
    print("O número que eu estou pensando é menor, tente novamente: ")
  elif (tentativa < numero):
    print("O número que eu estou pensando é maior, tente novamente: ")

print("Parabéns! Você adivinhou o número!")
