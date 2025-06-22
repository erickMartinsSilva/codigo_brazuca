import random

def menu(n):
  print("1. Visualizar regras")
  print("2. Gerar cartela")
  print("3. Visualizar cartela")
  print("4. Novo sorteio")
  print("5. Sair")
  print(f"Sorteios restantes: {n}")

print("--- BINGO ---")

op = 0
sorteios = 50
cartela = set()
temCartela = False
numeros = []

for i in range (1, 75):
  numeros.append(i)

while op != 5 and sorteios > 0:
  menu(sorteios)

  op = int(input("Escolha a opção desejada: "))

  match op:
    case 1: 
      print("Neste jogo, você vai receber uma cartela com cinco números aleatórios diferentes de 1 a 75.")
      print("Você terá 50 sorteios para tentar completar sua cartela. Se conseguir, você vence!")
    case 2:
      if len(cartela): print("Vocẽ já tem uma cartela!")
      else:
        while(len(cartela) < 5):
          sorteado = random.choice(numeros)
          cartela.add(sorteado)

        print(f"Cartela gerada com sucesso! Sua cartela: {cartela}")
        temCartela = True
    case 3:
      if temCartela: print(cartela)
      else: print("Você não tem uma cartela para visualizar!")
    case 4:
      if temCartela:
        sorteado = random.choice(numeros)
        numeros.remove(sorteado)
        print(f"O número sorteado nessa rodada foi... {sorteado}!")

        if sorteado in cartela:
          cartela.remove(sorteado)
          print("O número estava na sua cartela!")
          if len(cartela) != 0: print(f"Cartela atual: {cartela}")
        else: print("O número não estava na sua cartela...")

        sorteios -= 1

        if len(cartela) == 0: break
      else: print("Você precisa de uma cartela para jogar!")
    case 5: 
      print("Tchau!")
      break
    case _: print("Erro: opção inválida!")

if op != 5:
  if sorteios > 0 and len(cartela) == 0:
    print(f"Parabéns! Você ganhou o jogo em {50 - sorteios} rodadas!")
  else: print(f"Você não conseguiu completar sua cartela... Obrigado por jogar!")