total = 0
num1 = int(input("Insira o primeiro numero (inicio do intervalo): "))
num2 = int(input("Insira o segundo numero (fim do intervalo): "))

for i in range(num1, num2+1):
  if i % 3 == 0:
    total += i
  elif i % 5 == 0:
    total -= i
  elif i % 3 == 0 and i % 5 == 0:
    continue
print("Valor total:", total)
