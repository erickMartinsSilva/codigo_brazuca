# soma todos os números pares de um a 100

i = 1
soma = 0

for i in range(101):
  if i % 2 == 0:
    soma += i
  i += 1

print(soma)
