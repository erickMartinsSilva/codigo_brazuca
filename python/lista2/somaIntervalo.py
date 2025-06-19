# soma todos os números de 1 até num

num = int(input("Insira um numero: "))
soma = 0
i = 1

for i in range(num+1):
  soma += i

print(soma)
