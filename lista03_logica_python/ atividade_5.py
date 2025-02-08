# exibe a tabuada de um número inserido

num = int(input("Insira um numero para exibir sua tabuada: "))

for i in range(1, 11):
  print(num, "*", i, "=", num * i)
