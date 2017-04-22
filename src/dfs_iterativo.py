from tiempo import Tiempo


class DFSIterativo(object):

	def __init__(self, g, v, visitado):
		self.g = g
		self.v = v
		self.visitado = visitado
		self.tiempo_visitado = {}
		self.tiempo = Tiempo()
		self.predecesor = {}
		self.bajo = {}
		self.puntos_articulacion = set()
		for u in g.devolver_vertices():
			self.predecesor[u] = None

	def _asignar_visitado(self):
		stack = [self.v]
		stack_recorrido = [self.v]
		while stack:
			u = stack.pop()
			if self.visitado[u]:
				continue
			self.visitado[u] = True
			self.tiempo.incrementar()
			self.tiempo_visitado[u] = self.tiempo.actual()
			for w in self.g.adyacentes(u):
				if not self.visitado[w]:
					stack.append(w)
					stack_recorrido.append(w)
					self.predecesor[w] = u
		return stack_recorrido

	def _asignar_bajo(self, stack):
		while stack:
			u = stack.pop()
			self.bajo[u] = self.tiempo_visitado[u]
			for w in self.g.adyacentes(u):
				if self.tiempo_visitado[w] > self.tiempo_visitado[u]:
					if self.bajo[w] >= self.tiempo_visitado[u]:
						self.puntos_articulacion.add(u)
					self.bajo[u] = min(self.bajo[u], self.bajo[w])
				elif w != self.predecesor[u]:
					self.bajo[u] = min(self.bajo[u], self.tiempo_visitado[w])

	def get_predecesor(self):
		return self.predecesor

	def get_puntos_articulacion(self):
		return self.puntos_articulacion

	def hacer_dfs(self):
		stack_recorrido = self._asignar_visitado()
		self._asignar_bajo(stack_recorrido)
