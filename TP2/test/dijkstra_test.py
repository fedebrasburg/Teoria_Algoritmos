import sys
sys.path.append('../src')
from grafo import Grafo
from dijkstra import Dijkstra

g = Grafo()
g.agregar_vertice(0)
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_vertice(3)
g.agregar_vertice(4)
g.agregar_vertice(5)
g.agregar_arista_no_dirigida(0, 1, 7)
g.agregar_arista_no_dirigida(0, 2, 9)
g.agregar_arista_no_dirigida(0, 5, 14)
g.agregar_arista_no_dirigida(1, 2, 10)
g.agregar_arista_no_dirigida(1, 3, 15)
g.agregar_arista_no_dirigida(2, 3, 11)
g.agregar_arista_no_dirigida(2, 5, 2)
g.agregar_arista_no_dirigida(3, 4, 6)
g.agregar_arista_no_dirigida(4, 5, 9)
d = Dijkstra(g)
print "Nodo 0\n", d.dijkstra(0)
print "Nodo 1\n", d.dijkstra(1)
print "Nodo 2\n", d.dijkstra(2)
print "Nodo 3\n", d.dijkstra(3)
print "Nodo 4\n", d.dijkstra(4)
print "Nodo 5\n", d.dijkstra(5)
