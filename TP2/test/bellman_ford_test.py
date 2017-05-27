from TP2.src.bellman_ford import BellmanFord
from TP2.src.grafo import Grafo

g = Grafo()
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_arista_dirigida(1, 2)
d = BellmanFord(g)
print "Nodo 1\n", d.bellmanFord(1)
print "Nodo 2\n", d.bellmanFord(2)
