# inverte uma string inserida pelo usuário

str = input("Insira uma frase: ")

strDividida = list(str)
strDividida.reverse()

print(f"Frase invertida: {''.join(strDividida)}")
