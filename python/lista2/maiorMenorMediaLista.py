# com base numa lista informada pelo usuário, exibe o maior número, menor número e a média

lista = []
soma = 0
num = None

print(" --- Maior, Menor e Média de uma Lista --- ")

while(num != -1):
  num = int(input("Insira numeros para compor uma lista (-1 para encerrar): "))
  if num != -1: lista.append(num)

maior = lista[0]
menor = lista[0]

for i in lista:
  if i > maior:
    maior = i
  elif i < menor:
    menor = i
  soma += i

print("Maior número da lista:", maior)
print("Menor número da lista:", menor)
print("Média dos números da lista:", f"{soma/len(lista):.2f}")
