from dfs import Tiempo
from dfs import ResultadoDFS

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
			stack.append(v)
			arbol = []
			while (stack):
				u = stack.pop()
				visitado[u] = True
				arbol.append(u)
				tiempo.incrementar()
				tiempo_visitado[u] = tiempo.actual()
				bajo[u] = tiempo_visitado[u]
				for w in g.adyacentes(u):
					if (not visitado[w]):
						stack.append(w)
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
	analizarRaices(g, predecesor, puntos_artic, raices)

	return ResultadoDFS(tiempo_visitado, tiempo_finalizado, bosque, puntos_artic)

def assignNum(g, v, tiempo_visitado, predecesor, visitado, tiempo, arbol):
	stack = []
	stack2 = []
	stack.append(v)
	stack2.append(v)
	while (stack):
		u = stack.pop()
		if (visitado[u]):
			continue
		visitado[u] = True
		tiempo.incrementar()
		tiempo_visitado[u] = tiempo.actual()
		# arbol.append(u)
		for w in g.adyacentes(u):
			if (not visitado[w]):
				stack.append(w)
				stack2.append(w)
				predecesor[w] = u
	return stack2

def assignLow(g, v, tiempo_visitado, predecesor, bajo, puntos_artic, stack2):
	for u in g.devolver_vertices():
		bajo[u] = tiempo_visitado[u]

	stack = []
	stack.append(v)
	while (stack2):
		u = stack2.pop()
		# bajo[u] = tiempo_visitado[u]
		for w in g.adyacentes(u):
			if (tiempo_visitado[w] > tiempo_visitado[u]):
				# stack.append(w)
				# assignLow(g, w, tiempo_visitado, predecesor, bajo, puntos_artic)
				if (bajo[w] >= tiempo_visitado[u]):
					puntos_artic.add(u)
				bajo[u] = min(bajo[u], bajo[w])
			elif (w != predecesor[u]):
				bajo[u] = min(bajo[u], tiempo_visitado[w])

def analizarRaices(g, predecesor, puntos_artic, raices):
	# Analizo las raices como puntos de articulacion
	for v in raices:
		hijos = 0
		for u in g.adyacentes(
				v):  # Basta con revisar si los adyacentes a v lo tienen como predecesor o no, no es necesario en todos los vertices
			if (predecesor[u] == v):
				hijos += 1
		if (hijos >= 2):
			puntos_artic.add(v)

def DFS_iterativo2(g, lista_vertices = {}):
	if (lista_vertices == {}):
		lista_vertices = g.devolver_vertices()
	# Inicializo variables
	visitado = {}
	tiempo_visitado = {}
	tiempo = Tiempo()
	bosque = []
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
			arbol = []
			stack2 = assignNum(g, v, tiempo_visitado, predecesor, visitado, tiempo, arbol)
			assignLow(g, v, tiempo_visitado, predecesor, bajo, puntos_artic, stack2)
			raices.append(v)
			# Como v es raiz del arbol, lo saco para analizarlo por separado
			if (v in puntos_artic): # Aunque deberia estar incluida siempre
				puntos_artic.remove(v)
			bosque.append(arbol)
	print "# raices:", len(raices) # Si es conexo deberia ser 1 siempre
	analizarRaices(g, predecesor, puntos_artic, raices)
	return ResultadoDFS(tiempo_visitado, [], bosque, puntos_artic)