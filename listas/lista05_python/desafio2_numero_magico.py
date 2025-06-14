def primo(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  return True

def soma_digitos(num):
  soma = 0
  for digit in num:
    soma += digit
  return soma

num1 = int(input("Insira o primeiro numero (inicio do intervalo): "))
num2 = int(input("Insira o segundo numero (fim do intervalo): "))
contador = 0

for i in range (num1, num2+1):
  if i % 4 == 0 and primo(i) and soma_digitos(i) % 2 != 0:
    contador += 1
if contador > 0:
  print("Há", contador, "números mágicos no intervalo.")
else:
  print("Não há números mágicos no intervalo.")
