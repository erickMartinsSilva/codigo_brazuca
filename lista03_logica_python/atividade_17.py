num = int(input("Insira um numero: "))
lista_divisores = []
soma = 0

for i in range(1, num):
  if num % i == 0:
    lista_divisores.append(i)

for i in range(len(lista_divisores)):
  soma += lista_divisores[i]

if soma == num:
  print("O numero e perfeito")
else:
  print("O numero nao e perfeito")
