# original: organiza uma lista de três elementos informados pelo usuário em ordem crescente por meio do algoritmo de bubble sort
# modificado para permitir que o usuário crie uma lista com quantos elementos quiser

lista = []
num = None

while(num != 0):
  num = int(input("Insira um número para compor a lista (0 para encerrar): "))
  if num != 0: lista.append(num)

for j in range(len(lista)):
  for k in range(len(lista)-1-j):
    if lista[k] > lista[k+1]:
      aux = lista[k]
      lista[k] = lista[k+1]
      lista[k+1] = aux
      k += 1
  j += 1

if len(lista) != 0: print(lista)
