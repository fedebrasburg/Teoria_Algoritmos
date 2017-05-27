from TP2.src.floyd_warshall import FloydWarshall
from TP2.src.grafo import Grafo

g = Grafo()
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_arista_dirigida(1, 2, 3)
d = FloydWarshall(g)
print "Matriz\n", d.floydWarhsall()
