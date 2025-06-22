# exibe a sequência de fibonacci até o n-ésimo termo

def fibonacci(n):
    match n:
      case 0: return []
      case 1: return [1]
      case _:
        lista_fib = [0, 1]
        while len(lista_fib) < n:
          prox_fib = lista_fib[len(lista_fib) - 1] + lista_fib[len(lista_fib) - 2]
          lista_fib.append(prox_fib)
        return lista_fib

n = int(input("Insira um número: "))

if(n < 0): print("Erro: número negativo")
else: print(f"Sequência de Fibonacci até o {n}o termo: {fibonacci(n)}")