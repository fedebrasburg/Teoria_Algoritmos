from parser import Parser
from grafo import trasponer
from dfs import DFS
import time

"""Utilizar como python CFC.py"""

def CFC(g):
    """Recibe un grafo y devuelve las componentes fuertemente conexas"""
    r = DFS(g)
    g_traspuesta = trasponer(g)
    orden = sorted(r.get_tiempo_finalizado(), key=r.get_tiempo_finalizado().get, reverse = True)
    return DFS(g_traspuesta,orden).get_bosque_DFS()

for i in [0,1,2,3,4,5,6]:
	parser = Parser()
	g = parser.leer_grafo_dirigido("../in/ej3/d"+str(i)+".txt")
	start = time.time()
	CFC(g)
	end = time.time()
	print("Con " + str(g.devolver_cant_vertices()) + " vertices y " + str(len(g.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")
