# mostra os equivalentes em fahrenheit e kelvin para uma temperatura em celsius inserida pelo usuário

celsius = float(input("Insira uma temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Temperatura em Fahrenheit: {fahrenheit} graus F")
print(f"Temperatura em Kelvin: {kelvin} K")
