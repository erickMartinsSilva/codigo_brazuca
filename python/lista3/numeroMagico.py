def primo(num):
  if num <= 1: return False

  for i in range(2, int(num**0.5)+1):
    if num % i == 0: return False

  return True

def soma_digitos(num):
  digits = str(num)
  soma = 0

  for digit in digits:
    soma += int(digit)
  return soma


num1 = int(input("Insira o número de início do intervalo: "))
num2 = int(input("Insira o número de fim do intervalo: "))

if(num1 > num2):
  print("Erro: valor de início maior que valor de fim")
else:
  contador = 0

  for i in range (num1, num2+1):
    if i % 4 == 0 and primo(i) and soma_digitos(i) % 2 == 0: 
      contador += 1

  match contador:
    case 0: print("Não há números mágicos no intervalo.")
    case 1: print("Há 1 número mágico no intervalo.")
    case _: print(f"Há {contador} números mágicos no intervalo.")