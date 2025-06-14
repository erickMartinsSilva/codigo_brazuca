# simples lista de compras que permite que o usuário adicione e veja ela

lista = []
ativo = True

print("--- LISTA DE COMPRAS ---")

while ativo:
  print("1. Adicionar item")
  print("2. Remover item")
  print("3. Listar itens")
  print("4. Sair")

  escolha = int(input())
  
  if escolha == 1:
    item = input("Escreva o nome do item para ser adicionado: ")
    lista.append(item)
  elif escolha == 2:
    item = input("Escreva o nome do item para ser removido: ")
    lista.remove(item)
  elif escolha == 3:
    for str in lista:
      print(str)
  elif escolha == 4:
    ativo = False
  else:
    print("ERRO: Escolha invalida, tente novamente.")