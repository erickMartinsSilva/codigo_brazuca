# conta quantas ocorrências de uma letra existem numa frase

frase = input("Escreva uma frase: ")
letra = input("Agora, selecione uma letra presente na frase: ")

if frase.count(letra) == 0: print("Não há ocorrências desta letra na frase.")
else: print("A letra aparece", frase.count(letra), "vezes na frase.")
