# verifica se uma palavra é um palíndromo (igual de trás pra frente)

palavra = input("Insira uma palavra: ")
palavraDividida = list(palavra)

palavraDividida.reverse()

if(''.join(palavraDividida) == palavra): print("É um palíndromo")
else: print("Não é um palíndromo")