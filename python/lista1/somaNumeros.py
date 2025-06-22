# soma números até o usuário parar

num = -1
soma = 0

while num != 0:
  num = int(input("Insira números para serem somados (0 para parar): "))
  soma += num
  
print("Soma dos números inseridos: ", soma)
