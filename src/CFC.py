from grafo import Grafo
from parser import Parser
from grafo import trasponer
import time

class Tiempo:
	def __init__(self):
		self.t = 0
	def incrementar(self):
		self.t += 1
	def actual(self):
		return self.t

tiempo = 0
def DFS(g,f = {}, lista_vertices = {}):
	if(lista_vertices == {}):
		lista_vertices = g.devolver_vertices()
	estado = {}
	tiempo_visitado = {}
	tiempo = Tiempo()
	bosque = []
	for v in lista_vertices:
		estado[v] = False
	for v in lista_vertices:
		if estado[v] == False:
			arbol = []
			DFS_Visitar(g,v,estado,tiempo,tiempo_visitado,f,arbol)
			bosque.append(arbol)
	return bosque

def DFS_Visitar(g,v,estado,tiempo,tiempo_visitado,f,arbol):
	estado[v] = True
	arbol.append(v)
	tiempo.incrementar()
	tiempo_visitado[v] = tiempo.actual()
	for u in g.adyacentes(v):
		if estado[u] == False:
			DFS_Visitar(g,u,estado,tiempo,tiempo_visitado,f,arbol)
	tiempo.incrementar()
	f[v] = tiempo.actual()

def CFC(g):
	"""Recibe un grafo y devuelve las componentes fuertemente conexas"""
	f = {}
	DFS(g,f)
	return DFS(trasponer(g),{},sorted(f, key=f.get, reverse = True))

for i in [0]:
	start = time.time()
	parser = Parser()
	g = parser.leerGrafoDirigido("../in/ej3/d"+str(i)+".txt")
	print CFC(g)
	end = time.time()
	print("Con " + str(g.devolver_cant_vertices()) + " vertices y " + str(len(g.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")