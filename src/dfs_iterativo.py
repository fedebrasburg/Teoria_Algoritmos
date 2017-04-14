from grafo import Grafo
from dfs import Tiempo
from dfs import ResultadoDFS
import sys

def DFS_iterativo(g, lista_vertices = {}):
	if (lista_vertices == {}):
		lista_vertices = g.devolver_vertices()
	visitado = {}
	tiempo_visitado = {}
	tiempo = Tiempo()
	bosque = []
	tiempo_finalizado = {}
	predecesor = {}
	bajo = {}
	puntos_artic = set()
	raices = []
	stack = []
	for v in lista_vertices:
		visitado[v] = False
		predecesor[v] = None
	for v in lista_vertices:
		if (not visitado[v]):
			stack.append(lista_vertices[0])
			arbol = []
			while (not stack):
				u = stack.pop()
				visitado[u] = True
				arbol.append(u)
				tiempo.incrementar()
				tiempo_visitado[u] = tiempo.actual()
				bajo[u] = tiempo_visitado[u]
				for w in g.adyacentes(u):
					if (not visitado[w]):
						stack.append[w]
						predecesor[w] = u
						bajo[u] = min(bajo[u], bajo[w]) # El problema esta aca, donde necesito conocer el bajo[w], cuando todavia no lo procese
						if (bajo[w] >= tiempo_visitado[u]):
							puntos_artic.add(u)
					elif (w != predecesor[u]): # Arista de retroceso
						bajo[u] = min(bajo[u], tiempo_visitado[w])
				tiempo.incrementar()
				tiempo_finalizado[u] = tiempo.actual()
			# Como v es raiz del arbol, lo saco para analizarlo por separado
			if (v in puntos_artic): # Aunque deberia estar incluida siempre
				puntos_artic.remove(v)
			raices.append(v)
			bosque.append(arbol)
	print "# raices:", len(raices) # Si es conexo deberia ser 1 siempre
	for v in raices:
		hijos = 0
		for u in g.adyacentes(v): # Basta con revisar si los adyacentes a v lo tienen como predecesor o no, no es necesario en todos los vertices
			if (predecesor[u] == v):
				hijos += 1
		if (hijos >= 2):
			puntos_artic.add(v)
	return ResultadoDFS(tiempo_visitado, tiempo_finalizado, bosque, puntos_artic)

def DFS_Visitar(g, v, visitado, tiempo, tiempo_visitado, tiempo_finalizado, arbol, bajo, predecesor, puntos_artic):
	visitado[v] = True
	arbol.append(v)
	tiempo.incrementar()
	tiempo_visitado[v] = tiempo.actual()
	bajo[v] = tiempo_visitado[v]
	for u in g.adyacentes(v):
		if (not visitado[u]):
			predecesor[u] = v
			DFS_Visitar(g, u, visitado, tiempo, tiempo_visitado, tiempo_finalizado, arbol, bajo, predecesor, puntos_artic)
			bajo[v] = min(bajo[v], bajo[u])
			if (bajo[u] >= tiempo_visitado[v]):
				puntos_artic.add(v)
		elif (u != predecesor[v]): # Arista de retroceso
			bajo[v] = min(bajo[v], tiempo_visitado[u])
	tiempo.incrementar()
	tiempo_finalizado[v] = tiempo.actual()