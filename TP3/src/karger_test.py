from grafo import Grafo

def contraer(grafo, id1, id2):
    for destino, arista in grafo.devolver_aristas()[id2].items():
        # Si la arista a agregar no es una arista entre id1 e id2
        if destino != id1:
            grafo.agregar_arista_no_dirigida(id1, destino)
        # Borro la arista original del grafo
        grafo.borrar_arista_no_dirigida(id2, destino)
    # Borro la arista que va de id1 a id2, ya que antes solo borre la de id2 a id1
    grafo.borrar_arista_no_dirigida(id1, id2)
    # Borro el vertice que contraje, que se fusiono con id1
    grafo.borrar_vertice(id2)

g = Grafo()
g.agregar_vertice(0)
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_vertice(3)
g.agregar_arista_no_dirigida(0, 1)
g.agregar_arista_no_dirigida(1, 2)
g.agregar_arista_no_dirigida(2, 3)
g.agregar_arista_no_dirigida(3, 0)
g.agregar_arista_no_dirigida(0, 2)

print 'Aristas:', g.devolver_aristas()
print 'Aristas_list:', g.devolver_aristas_list()
contraer(g, 0, 1)
print 'Aristas:', g.devolver_aristas()
print 'Aristas_list:', g.devolver_aristas_list()
