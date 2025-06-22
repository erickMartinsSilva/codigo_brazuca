# verifica se um número é par ou ímpar

def paridade(num):
  if num % 2 != 0:
    return "Ímpar"
  else: return "Par"

num = int(input("Insira um numero: "))
print(paridade(num))

