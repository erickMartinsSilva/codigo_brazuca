# conta quantas palavras há numa frase

frase = input("Insira uma frase: ")

if len(frase) == 0: raise SyntaxError("Frase vazia")

fraseDividida = frase.split(" ")

match len(fraseDividida):
    case 1: print("A frase contém uma palavra")
    case _: print(f"A frase contém {len(fraseDividida)} palavras")
