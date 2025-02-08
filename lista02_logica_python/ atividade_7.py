lista = []
contador = 1

print("--- LISTA DE COMPRAS ---")

while contador == 1:
  print("1. Adicionar item")
  print("2. Imprimir lista")
  print("3. Sair")

  escolha = int(input())
  
  if escolha == 1:
    item = input("Escreva o nome do item para ser adicionado: ")
    lista.append(item)
  elif escolha == 2:
    for str in lista:
      print(str)
  elif escolha == 3:
    contador = 0
  else:
    print("ERRO: Escolha invalida, tente novamente.")