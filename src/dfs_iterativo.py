from dfs import Tiempo
from dfs import ResultadoDFS

def asignarVisitado(g, v, tiempo_visitado, predecesor, visitado, tiempo):
	stack = [v]
	stackRecorrido = [v]
	while (stack):
		u = stack.pop()
		if (visitado[u]):
			continue
		visitado[u] = True
		tiempo.incrementar()
		tiempo_visitado[u] = tiempo.actual()
		for w in g.adyacentes(u):
			if (not visitado[w]):
				stack.append(w)
				stackRecorrido.append(w)
				predecesor[w] = u
	return stackRecorrido

def asignarBajo(g, v, tiempo_visitado, predecesor, bajo, puntos_artic, stack):
	while (stack):
		u = stack.pop()
		bajo[u] = tiempo_visitado[u]
		for w in g.adyacentes(u):
			if (tiempo_visitado[w] > tiempo_visitado[u]):
				if (bajo[w] >= tiempo_visitado[u]):
					puntos_artic.add(u)
				bajo[u] = min(bajo[u], bajo[w])
			elif (w != predecesor[u]):
				bajo[u] = min(bajo[u], tiempo_visitado[w])

def analizarRaices(g, predecesor, puntos_artic, raices):
	# Analizo las raices como puntos de articulacion
	for v in raices:
		hijos = 0
		for u in g.adyacentes(v):  # Basta con revisar si los adyacentes a v lo tienen como predecesor o no, no es necesario en todos los vertices
			if (predecesor[u] == v):
				hijos += 1
		if (hijos >= 2):
			puntos_artic.add(v)

def DFS_iterativo(g, lista_vertices = {}):
	if (lista_vertices == {}):
		lista_vertices = g.devolver_vertices()
	# Inicializo variables
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
		if (not visitado[v]):
			stack = asignarVisitado(g, v, tiempo_visitado, predecesor, visitado, tiempo)
			asignarBajo(g, v, tiempo_visitado, predecesor, bajo, puntos_artic, stack)
			raices.append(v)
			# Como v es raiz del arbol, lo saco para analizarlo por separado
			if (v in puntos_artic): # Aunque deberia estar incluida siempre
				puntos_artic.remove(v)
	print "# raices:", len(raices) # Si es conexo deberia ser 1 siempre
	analizarRaices(g, predecesor, puntos_artic, raices)
	return ResultadoDFS(tiempo_visitado, [], [], puntos_artic)