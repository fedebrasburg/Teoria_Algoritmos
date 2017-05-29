from TP2.src.bellman_ford import BellmanFord
from TP2.src.grafo import Grafo

g = Grafo()
g.agregar_vertice(0)
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_vertice(3)
g.agregar_vertice(4)
g.agregar_arista_dirigida(0, 1, 6)
g.agregar_arista_dirigida(0, 3, 7)
g.agregar_arista_dirigida(1, 2, 5)
g.agregar_arista_dirigida(1, 3, 8)
g.agregar_arista_dirigida(1, 4, -4)
g.agregar_arista_dirigida(2, 1, -2)
g.agregar_arista_dirigida(3, 2, -3)
g.agregar_arista_dirigida(3, 4, 9)
g.agregar_arista_dirigida(4, 0, 2)
g.agregar_arista_dirigida(4, 2, 7)
bf = BellmanFord(g)
print "Nodo 0\n", bf.bellmanFord(0)
print "Nodo 1\n", bf.bellmanFord(1)
print "Nodo 2\n", bf.bellmanFord(2)
print "Nodo 3\n", bf.bellmanFord(3)
print "Nodo 4\n", bf.bellmanFord(4)
