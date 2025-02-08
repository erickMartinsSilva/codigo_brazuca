# calcula a média ponderada de notas com pesos fixos

nota1 = float(input("Insira a primeira nota (peso 2): "))
nota2 = float(input("Insira a segunda nota (peso 3): "))
nota3 = float(input("Insira a terceira nota (peso 5): "))

media = ((nota1*2)+(nota2*3)+(nota3*5))/10
print("Media das notas:", format(media, ".2f"))
