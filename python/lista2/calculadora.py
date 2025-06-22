# simples calculadora que permite o usuário realizar operações de adição, subtração, multiplicação e divisão com dois números

num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))
op = input("Insira a operacao desejada (+, -, *, /, **): ")

match op:
    case '+': resultado = num1 + num2;
    case '-': resultado = num1 - num2;
    case '*': resultado = num1 * num2;
    case '/': resultado = num1 / num2;
    case '**': resultado = num1 ** num2;

print(f"Resultado: {resultado:.2f}")
