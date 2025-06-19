# mostra os equivalentes em fahrenheit e kelvin para uma temperatura em celsius

celsius = float(input("Insira uma temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("Fahrenheit: ", fahrenheit, "graus")
print("Kelvin: ", kelvin)
