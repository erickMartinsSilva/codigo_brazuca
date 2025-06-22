# verifica se um número é perfeito (soma de seus divisores exceto o número for igual ao número)

num = int(input("Insira um numero: "))
lista_divisores = [1]
soma = 0

for i in range(2, num):
  if num % i == 0: lista_divisores.append(i)

for numero in lista_divisores: soma += numero

if soma == num: print("O numero e perfeito")
else: print("O numero nao e perfeito")
