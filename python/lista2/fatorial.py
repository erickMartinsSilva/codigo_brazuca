# calcula o fatorial de um número inserido pelo usuário

num = int(input("Insira um número inteiro positivo: "))
aux = num
i = num - 1

for i in range(1, num):
  num = num * i

print(f"{aux}! = {num}")
