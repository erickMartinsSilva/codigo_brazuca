def par(num):
  if num % 2 != 0:
    return False
  else: return True

num = int(input("Insira um numero: "))

if par(num):
  print("O numero é par")
else:
  print("O numero é ímpar")
