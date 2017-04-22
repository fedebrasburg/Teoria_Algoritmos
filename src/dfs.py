import sys

class Tiempo:
	def __init__(self):
		self.t = 0
	def incrementar(self):
		self.t += 1
	def actual(self):
		return self.t

class ResultadoDFS:
	def __init__(self, tiempo_visitado, tiempo_finalizado, bosque, puntos_artic):
		self.bosque = bosque
		self.tiempo_finalizado = tiempo_finalizado
		self.tiempo_visitado = tiempo_visitado
		self.puntos_artic = puntos_artic
	def get_tiempo_visitado(self):
		return self.tiempo_visitado
	def get_tiempo_finalizado(self):
		return self.tiempo_finalizado
	def get_bosque_DFS(self):
		return self.bosque
	def get_puntos_artic(self):
		return self.puntos_artic

def DFS(g, lista_vertices = {}):
	sys.setrecursionlimit(6054) # Con 6054 se banca el g5, con 22784 tira exceeded recursion depth, con 22785 segfault (Para el g6)
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
	for v in lista_vertices:
		visitado[v] = False
		predecesor[v] = None
	for v in lista_vertices:
		if (not visitado[v]):
			arbol = []
			DFS_Visitar(g, v, visitado, tiempo, tiempo_visitado, tiempo_finalizado, arbol, bajo, predecesor, puntos_artic)
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