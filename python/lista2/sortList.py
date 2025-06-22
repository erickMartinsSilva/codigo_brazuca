# original: organiza uma lista de três elementos informados pelo usuário em ordem crescente
# modificado para permitir que o usuário crie uma lista com quantos elementos quiser

lista = []
num = None

print(" --- Ordenador de Lista --- ")

while(num != -1):
  num = int(input("Insira números para compor a lista (-1 para encerrar): "))
  if num != -1: lista.append(num)

if(len(lista)):
  lista.sort()
  print("Lista ordenada: ", lista)
else: print("Erro: a lista está vazia")
