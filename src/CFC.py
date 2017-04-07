from grafo import Grafo
from parser import Parser
import time

tiempo = 0
def DFS(g,f = {}, lista_vertices = {}):
	if(lista_vertices == {}):
		lista_vertices = g.devolver_vertices()
	global tiempo
	estado = {}
	tiempo_visitado = {}
	tiempo = 0
	bosque = []
	for v in lista_vertices:
		estado[v] = False
	for v in lista_vertices:
		if estado[v] == False:
			arbol = []
			DFS_Visitar(g,v,estado,tiempo_visitado,f,arbol)
			bosque.append(arbol)
	return bosque

def DFS_Visitar(g,v,estado,tiempo_visitado,f,arbol):
	global tiempo
	estado[v] = True
	arbol.append(v)
	tiempo += 1
	tiempo_visitado[v] = tiempo
	for u in g.adyacentes(v):
		if estado[u] == False:
			DFS_Visitar(g,u,estado,tiempo_visitado,f,arbol)
	tiempo += 1
	f[v] = tiempo

def CFC(g):
	"""Recibe un grafo y devuelve las componentes fuertemente conexas"""
	f = {}
	DFS(g,f)
	g.trasponer()
	return DFS(g,{},sorted(f, key=f.get, reverse = True))

for i in [1,2,3,4,5,6]:
	start = time.time()
	parser = Parser()
	g = parser.leerGrafoDirigido("../in/ej3/d"+str(i)+".txt")
	CFC(g)
	end = time.time()
	print("Con " + str(g.devolver_cant_vertices()) + " vertices y " + str(len(g.devolver_aristas())) + " aristas, tardo: " + str(end - start) + " segundos")