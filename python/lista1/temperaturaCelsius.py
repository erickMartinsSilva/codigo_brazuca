# exibe uma mensagem com base numa temperatura em celsius

celsius = int(input("Insira a temperatura atual, em Celsius: "))

if celsius > 30: print("Está quente! Não esqueça de se hidratar e passar protetor solar.")
elif celsius < 30 and celsius > 15: print("Está agradável. Aproveite seu dia!")
else: print("Está frio! Não esqueça de vestir um agasalho.")
