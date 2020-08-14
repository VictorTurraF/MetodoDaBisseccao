# Equação
eq = lambda x : (x ** 3) + (3 * x) - 1 

# Erro
lim = 10 ** -2

# Procura os intervalos onde estão as raizes
def procurar_intervalos( pontos ):
  intervalos = []
  for x in range(0, len(pontos) - 1):
    if pontos[x][1] * pontos[x+1][1] < 0:
      intervalos.append( [ pontos[x], pontos[x+1] ] )
  return intervalos

# Faz uma varredura no eixo X para deterninar os pontos
def encontar_pontos(f):
  pontos = []
  for x in range(-5, 5):
    pontos.append( [ x, f(x) ] )
  return pontos

pontos = encontar_pontos( eq )

intervalos = procurar_intervalos(pontos)

print("Intervalos encontrados :")
print( intervalos )

f = eq

# para cada intervalo encontrado
for p in intervalos:
  print("\nIntervalo: ")
  print(p)
  
  a = p[0][0]
  b = p[1][0]
  error = b - a
  it = 1

  # Realiza uma iteração enquanto a erro for maior que o limite
  while error > lim:
    Xk = (a + b)/2
    Fa = f(a)
    Fxk = f(Xk)
    error = b - a
    
    print("\nIteração: " + str(it))
    print("a: " + str(a))
    print("b: " + str(b))
    print("Xk: " + str(Xk))
    print("f(a): " + str(Fa))
    print("f(Xk): " + str(Fxk))
    print("Diferença: " + str(error) )

    if (Fa * Fxk) >= 0:
      a = Xk
    else:
      b = Xk

    it += 1
  
  print("\nA raiz procurada é: " + str(Xk))

  print('\n')