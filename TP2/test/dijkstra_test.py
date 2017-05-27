from TP2.src.dijkstra import Dijkstra
from TP2.src.grafo import Grafo

g = Grafo()
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_arista_dirigida(1, 2)
d = Dijkstra(g)
print "Nodo 1\n", d.dijkstra(1)
print "Nodo 2\n", d.dijkstra(2)
