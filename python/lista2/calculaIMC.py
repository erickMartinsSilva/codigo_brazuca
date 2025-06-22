# calcula o imc com base no peso e altura fornecidos pelo usuário

peso = float(input("Insira seu peso, em kg: "))
altura = float(input("Insira sua altura, em metros: "))

print(f"IMC: {peso/(altura * altura):.2f}")
