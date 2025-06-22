num1 = int(input("Insira o número de início do intervalo: "))
num2 = int(input("Insira o número de fim do intervalo: "))
total = 0

for i in range(num1, num2+1):
  if i % 3 == 0: total += i
  elif i % 5 == 0: total -= i
  
print("Valor total:", total)
