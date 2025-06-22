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

num = int(input("Insira um numero: "))

if(num < 0): raise ValueError("Número abaixo de zero")

print(f"Sequência de Fibonacci até o {num}o termo: {fibonacci(num)}")