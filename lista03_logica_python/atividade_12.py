import random

numero = random.randint(1, 100)
print("Estou pensando em um número entre 1 e 100. Você consegue adivinhá-lo?")

tentativa = None
while(tentativa != numero):
  tentativa = int(input())
  if (tentativa > numero):
    print("O numero que eu estou pensando é menor, tente novamente: ")
  elif (tentativa < numero):
    print("O numero que eu estou pensando é maior, tente novamente: ")

print("Parabéns! Você adivinhou o número!")
