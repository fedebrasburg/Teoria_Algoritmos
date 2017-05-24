from tiempo import Tiempo
from resultado_DFS import ResultadoDFS


def DFS(g, lista_vertices={}):
	if lista_vertices == {}:
		lista_vertices = g.devolver_vertices()
	visitado = {}
	tiempo_visitado = {}
	tiempo = Tiempo()
	bosque = []
	f = {}
	for v in lista_vertices:
		visitado[v] = False
	for v in lista_vertices:
		if not visitado[v]:
			arbol = []
			DFS_Visitar(g, v, visitado, tiempo, tiempo_visitado, f, arbol)
			bosque.append(arbol)
	return ResultadoDFS(tiempo_visitado, f, bosque)

def DFS_Visitar(g, v, visitado, tiempo, tiempo_visitado, f, arbol):
	visitado[v] = True
	arbol.append(v)
	tiempo.incrementar()
	tiempo_visitado[v] = tiempo.actual()
	for u in g.adyacentes(v):
		if not visitado[u]:
			DFS_Visitar(g, u, visitado, tiempo, tiempo_visitado, f, arbol)
	tiempo.incrementar()
	f[v] = tiempo.actual()
