# original: imprime todos os números pares de 1 a 10
# modificado para imprimir todos os números pares num dado intervalo numérico

inicio = int(input("Insira o número inicial: "))
fim = int(input("Insira o número final: "))

print("Números pares de", inicio, "até", fim, ":")

for i in range(inicio, fim):
  if i % 2 == 0: print(i)
