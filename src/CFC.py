from grafo import Grafo
from parser import Parser
from grafo import trasponer
from dfs import DFS
import time


def CFC(g):
	"""Recibe un grafo y devuelve las componentes fuertemente conexas"""
	r = DFS(g)
	return DFS(trasponer(g),sorted(r.tiempo_finalizado(), key=r.tiempo_finalizado().get, reverse = True)).bosque_DFS()

for i in [0]:
	start = time.time()
	parser = Parser()
	g = parser.leerGrafoDirigido("../in/ej3/d"+str(i)+".txt")
	print CFC(g)
	end = time.time()
	print("Con " + str(g.devolver_cant_vertices()) + " vertices y " + str(len(g.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")


