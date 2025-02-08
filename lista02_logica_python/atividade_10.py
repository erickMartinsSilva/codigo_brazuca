def primo(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True

n1 = int(input("Insira o primeiro numero do intervalo: "))
n2 = int(input("Insira o segundo numero do intervalo (deve ser maior que o primeiro): "))

print("Numeros primos: ")

for j in range(n1,n2+1):
  if (primo(j)):
    print(j)