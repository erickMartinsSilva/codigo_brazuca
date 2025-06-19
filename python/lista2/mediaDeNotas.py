# calcula a média de várias notas

soma_nota = 0
contador = 0
nota = None

while(nota != -1):
  nota = float(input("Insira notas (-1 para encerrar): "))
  soma_nota += nota
  contador += 1

media = soma_nota / contador

print("Media: ", format(media, ".2f"))
