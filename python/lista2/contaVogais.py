# conta as vogais de uma string

frase = input("Insira uma frase: ").lower()
vogais = ['a', 'e', 'i', 'o', 'u']
contador = 1

for char in frase:
    try:
      if(vogais.index(char)): contador += 1
    except ValueError: continue

match contador:
   case 0: print("A frase não possui vogais")
   case 1: print("A frase possui 1 vogal")
   case _: print(f"A frase possui {contador} vogais")
