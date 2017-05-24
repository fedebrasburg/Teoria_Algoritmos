from dijkstra import Dijkstra
from grafo import Grafo
g=Grafo()
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_arista_dirigida(1,2)
d=Dijkstra(g)
print "nodo 1\n",d.dijkstra(1)
print "nodo 2\n",d.dijkstra(2)
