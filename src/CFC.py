from grafo import Grafo
from parser import Parser

parser = Parser()
g = parser.leerGrafoDirigido("../in/ej3/d1.txt")

def DFS(g):
	estado = {}
	tiempo_visitado = {}
	for v in g.devolver_vertices():
		estado[v] = False
	tiempo = 0
	for v in g.devolver_vertices():
		if estado[v] == False:
			DFS_Visitar(g,v,estado,tiempo,tiempo_visitado)

def DFS_Visitar(g,v,estado,tiempo,tiempo_visitado):
	estado[v] = True
	tiempo += 1
	print("Visite id:" + str(v) + " en tiempo " + str(tiempo))
	tiempo_visitado[v] = tiempo
	for u in g.adyacentes(v):
		if estado[u] == False:
			DFS_Visitar(g,u,estado,tiempo,tiempo_visitado)
	tiempo += 1

DFS(g)