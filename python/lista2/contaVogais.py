# conta as vogais de uma string

frase = input("Insira uma frase: ")
contador = 0

for char in frase:
  if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
    contador = contador + 1
print("Vogais:", contador)
