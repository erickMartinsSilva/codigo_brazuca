# original: calcula a média ponderada de notas com pesos fixos
# modificado para permitir pesos escolhidos pelo usuário

nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))
nota3 = float(input("Insira a terceira nota do aluno: "))
peso1 = int(input("Insira o peso da primeira nota: "))
peso2 = int(input("Insira o peso da segunda nota: "))
peso3 = int(input("Insira o peso da terceira nota: "))

media = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso3)

print("Média do aluno:", format(media, ".2f"))
