# conta quantas palavras há numa frase

frase = input("Insira uma frase: ")
contador = 1

for char in frase:
  if char == ' ':
    contador += 1

print("A frase contem", contador, "palavras")
