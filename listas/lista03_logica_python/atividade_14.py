# simples calculadora que permite o usuário realizar operações de adição, subtração, multiplicação e divisão com dois números

num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))
op = input("Insira a operacao desejada (+, -, *, /): ")

if op == '+':
  resultado = num1 + num2
elif op == '-':
  resultado = num1 - num2
elif op == '*':
  resultado = num1 * num2
elif op == '/':
  resultado = num1 / num2

print(resultado)
