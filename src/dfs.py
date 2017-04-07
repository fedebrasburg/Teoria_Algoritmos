from grafo import Grafo
import time

class Tiempo:
	def __init__(self):
		self.t = 0
	def incrementar(self):
		self.t += 1
	def actual(self):
		return self.t

class ResultadoDFS:
	def __init__(self,tiempo_visitado,f,bosque):
		self.bosque = bosque
		self.f = f
		self.tiempo_visitado = tiempo_visitado
	def tiempo_visitado(self):
		return self.tiempo_visitado
	def tiempo_finalizado(self):
		return self.f
	def bosque_DFS(self):
		return self.bosque

tiempo = 0
def DFS(g,lista_vertices = {}):
	if(lista_vertices == {}):
		lista_vertices = g.devolver_vertices()
	estado = {}
	tiempo_visitado = {}
	tiempo = Tiempo()
	bosque = []
	f = {}
	for v in lista_vertices:
		estado[v] = False
	for v in lista_vertices:
		if estado[v] == False:
			arbol = []
			DFS_Visitar(g,v,estado,tiempo,tiempo_visitado,f,arbol)
			bosque.append(arbol)
	return ResultadoDFS(tiempo_visitado,f,bosque)

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