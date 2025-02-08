# organiza uma lista de três elementos informados pelo usuário em ordem crescente por meio do algoritmo de bubble sort

lista = []
i = 0

for i in range(3):
  num = int(input("Insira um numero: "))
  lista.append(num)
  i += 1

for j in range(3):
  for k in range(3-1-j):
    if lista[k] > lista[k+1]:
      aux = lista[k]
      lista[k] = lista[k+1]
      lista[k+1] = aux
      k += 1
  j += 1

print(lista)
