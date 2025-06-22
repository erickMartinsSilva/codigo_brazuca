# simples lista de compras que permite com que o usuário adicione e remova itens dela, além de visualizar seus itens

class Item:
  def __init__(self, nome, qtd=1):
    self.nome = nome
    self.qtd = qtd

def menu():
  print("1. Adicionar item")
  print("2. Remover item")
  print("3. Listar itens")
  print("4. Sair")

# imprime cada objeto da lista, exibindo seu nome e quantidade
def printList(list):
  for i in list:
    print(i.qtd, "x", i.nome)

# encontra um objeto na lista com base em seu nome e retorna seu índice. caso o objeto não exista na lista, retorna -1
def findByName(list, item):
  for i in list:
    if(i.nome == item.nome): return list.index(i)
  
  return -1

print("--- LISTA DE COMPRAS ---")

lista = []
escolha = 0

while escolha != 4:
  menu()

  escolha = int(input("Insira a ação desejada: "))
  
  match escolha:
    case 1: 
      nome = input("Escreva o nome do item a ser adicionado à lista: ")
      qtd = int(input("Insira a quantidade do item: "))

      item = Item(nome, qtd)
      
      if(findByName(lista, item) != -1):
        lista[findByName(lista, item)].qtd += item.qtd
      else: lista.append(item)

      print("Item adicionado com sucesso!")
    case 2:
      nome = input("Insira o nome do item a ser removido da lista: ")

      item = Item(nome)
      
      if(findByName(lista, item) != -1):
        lista.remove(lista[findByName(lista, item)])
        print("Item removido com sucesso!")
      else: print("Erro: este item não está presente na lista")
    case 3:
      if(len(lista)): printList(lista)
      else: print("A lista está vazia!")
    case 4: break
    case _:
      print("Erro: opção inválida")