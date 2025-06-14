# com base numa lista informada pelo usuário, exibe o maior número, menor número e a média

lista = []
soma = 0
num = None

while(num != -1):
  num = int(input("Insira numeros para compor uma lista (-1 para encerrar): "))
  lista.append(num)

maior = lista[0]
menor = lista[0]

for i in range(len(lista)):
  if lista[i] > maior:
    maior = lista[i]
  elif lista[i] < menor:
    menor = lista[i]
  soma += lista[i]

print("Maior numero da lista:", maior)
print("Menor numero da lista:", menor)
print("Media dos numeros da lista:", soma/len(lista))
