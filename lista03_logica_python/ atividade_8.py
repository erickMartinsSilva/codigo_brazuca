# exibe a sequência de fibonacci até o n-ésimo termo

def fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    lista_fib = [0, 1]
    while (len(lista_fib) < n):
      next_fib = lista_fib[-1] + lista_fib[-2]
      lista_fib.append(next_fib)
    return lista_fib

num = int(input("Insira um numero: "))
print("Sequencia de Fibonacci ate o", num, "termo:", fibonacci(num))
