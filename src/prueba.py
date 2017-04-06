from grafo import Grafo
g=Grafo()
g.agregar_vertice(0,0)
g.agregar_vertice(1,1)
g.agregar_arista_dirigida(0,1)
g.borrar_arista_dirigida(0,1)
g.agregar_arista_no_dirigida(0,1)
g.borrar_arista_no_dirigida(0,1)
g.borrar_vertice(0)
