from dfs import Tiempo
from dfs import ResultadoDFS


def asignar_visitado(g, v, tiempo_visitado, predecesor, visitado, tiempo):
	stack = [v]
	stack_recorrido = [v]
	while stack:
		u = stack.pop()
		if visitado[u]:
			continue
		visitado[u] = True
		tiempo.incrementar()
		tiempo_visitado[u] = tiempo.actual()
		for w in g.adyacentes(u):
			if not visitado[w]:
				stack.append(w)
				stack_recorrido.append(w)
				predecesor[w] = u
	return stack_recorrido

def asignar_bajo(g, tiempo_visitado, predecesor, bajo, puntos_artic, stack):
	while stack:
		u = stack.pop()
		bajo[u] = tiempo_visitado[u]
		for w in g.adyacentes(u):
			if tiempo_visitado[w] > tiempo_visitado[u]:
				if bajo[w] >= tiempo_visitado[u]:
					puntos_artic.add(u)
				bajo[u] = min(bajo[u], bajo[w])
			elif w != predecesor[u]:
				bajo[u] = min(bajo[u], tiempo_visitado[w])

def analizar_raices(g, predecesor, puntos_artic, raices):
	# Analizo las raices como puntos de articulacion
	for v in raices:
		hijos = 0
		for u in g.adyacentes(v):  # Basta con revisar si los adyacentes a v lo tienen como predecesor o no, no es necesario en todos los vertices
			if predecesor[u] == v:
				hijos += 1
		if hijos >= 2:
			puntos_artic.add(v)

def DFS_iterativo(g):
	# Inicializo variables
	lista_vertices = g.devolver_vertices()
	visitado = {}
	tiempo_visitado = {}
	tiempo = Tiempo()
	predecesor = {}
	bajo = {}
	puntos_artic = set()
	raices = []
	for v in lista_vertices:
		visitado[v] = False
		predecesor[v] = None

	# Armo el arbol DFS
	for v in lista_vertices:
		if not visitado[v]:
			stack = asignar_visitado(g, v, tiempo_visitado, predecesor, visitado, tiempo)
			asignar_bajo(g, tiempo_visitado, predecesor, bajo, puntos_artic, stack)
			raices.append(v)
			# Como v es raiz del arbol, lo saco para analizarlo por separado
			if v in puntos_artic: # Aunque deberia estar incluida siempre
				puntos_artic.remove(v)
	analizar_raices(g, predecesor, puntos_artic, raices)
	return ResultadoDFS(tiempo_visitado, [], [], puntos_artic)
