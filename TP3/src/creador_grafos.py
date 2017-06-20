from random import randint
from grafo import Grafo


# Crea un grafo de n vertices y 2*n aristas, junto con el archivo correspondiente
# Importante: No correr el algoritmo para n <= 4, ya que para esos n, 2*n > n*(n-1)/2
# (Aristas en grafo completo), por lo que no existe grafo posible con n vertices y 2*n aristas
def crearGrafoConexo(n, nombre):
    if 2 * n > n * (n - 1) / 2:
        print 'No es posible correr el algoritmo ya que 2*n > n*(n-1)/2 para n =', n
        return
    cantAristas = 2 * n

    arch = open(nombre, 'w')
    arch.write(str(n) + "\n")
    arch.write(str(cantAristas) + "\n")
    # Escribo la primer arista, que siempre se va a corresponder con la 0 <-> 1
    arch.write(str(0) + " " + str(1) + "\n")
    # Creo el grafo inicial, junto con la primera arista
    g = Grafo()
    g.agregar_vertice(0)
    g.agregar_vertice(1)
    g.agregar_arista_no_dirigida(0, 1)

    # Primero creo un grafo conexo de n vertices y n-1 aristas, agregando de a 1 por vez
    # y creando una arista entre el y cualquiera de los anteriores
    for i in range(2, n):
        verticeRandom = randint(0, i - 1)
        arch.write(str(i) + " " + str(verticeRandom) + "\n")
        g.agregar_vertice(i)
        g.agregar_arista_no_dirigida(i, verticeRandom)
    # Despues genero las n+1 aristas restantes de manera aleatoria, teniendo en cuenta
    # que no se creen aristas repetidas
    i = 0
    while i <= n:
        verticeRandom1 = randint(0, n - 1)
        verticeRandom2 = randint(0, n - 1)
        if verticeRandom1 != verticeRandom2 and not g.son_vecinos(verticeRandom1, verticeRandom2):
            arch.write(str(verticeRandom1) + " " + str(verticeRandom2) + "\n")
            g.agregar_arista_no_dirigida(verticeRandom1, verticeRandom2)
            i += 1
    arch.close()
    return g

# Crea un grafo completo con n vertices, junto con el archivo correspondiente
def crearGrafoCompleto(n, nombre):
    g = Grafo()
    for i in range(n):
        g.agregar_vertice(i)
    cantAristas = n * (n - 1) / 2
    arch = open(nombre, 'w')
    arch.write(str(n) + "\n")
    arch.write(str(cantAristas) + "\n")
    for i in range(n):
        for j in range(i + 1, n):
            g.agregar_arista_no_dirigida(i, j)
            arch.write(str(i) + " " + str(j)+ "\n")  # Crea una arista del vertice i al vertice j
    arch.close()
    return g
