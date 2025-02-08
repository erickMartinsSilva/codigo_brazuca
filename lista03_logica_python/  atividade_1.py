# calcula o fatorial de um número

num = int(input("Insira um numero inteiro: "))
aux = num
i = num - 1

for i in range(1, num):
  num = num * i
print("Fatorial de ", aux, " = ", num)
