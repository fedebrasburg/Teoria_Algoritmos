from bellmanFord import BellmanFord
from grafo import Grafo
g=Grafo()
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_arista_dirigida(1,2)
d=BellmanFord(g)
print "nodo 1\n",d.bellmanFord(1)
print "nodo 2\n",d.bellmanFord(2)
