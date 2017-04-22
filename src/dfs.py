from tiempo import Tiempo
from resultado_DFS import ResultadoDFS


class DFS:

    def __init__(self, g, lista_vertices={}):
        self.g = g
        self.lista_vertices = g.devolver_vertices() if (lista_vertices == {}) else lista_vertices
        self.visitado = {}
        self.tiempo_visitado = {}
        self.tiempo = Tiempo()
        self.bosque = []
        self.tiempo_finalizado = {}
        self.predecesor = {}
        self.bajo = {}
        self.puntos_artic = set()
        self.raices = []
        for v in self.lista_vertices:
            self.visitado[v] = False
            self.predecesor[v] = None

    def hacer_DFS(self):
        for v in self.lista_vertices:
            if not self.visitado[v]:
                arbol = []
                self._DFS_Visitar(v, arbol)
                # Como v es raiz del arbol, lo saco para analizarlo por separado
                if v in self.puntos_artic:  # Aunque deberia estar incluida siempre
                    self.puntos_artic.remove(v)
                self.raices.append(v)
                self.bosque.append(arbol)
        print "# raices:", len(self.raices)  # Si es conexo deberia ser 1 siempre
        for v in self.raices:
            hijos = 0
            for u in self.g.adyacentes(v):  # Basta con revisar si los adyacentes a v lo tienen como predecesor o no, no es necesario en todos los vertices
                if self.predecesor[u] == v:
                    hijos += 1
            if hijos >= 2:
                self.puntos_artic.add(v)
        return ResultadoDFS(self.tiempo_visitado, self.tiempo_finalizado, self.bosque, self.puntos_artic)

    def _DFS_Visitar(self, v, arbol):
        self.visitado[v] = True
        arbol.append(v)
        self.tiempo.incrementar()
        self.tiempo_visitado[v] = self.tiempo.actual()
        self.bajo[v] = self.tiempo_visitado[v]
        for u in self.g.adyacentes(v):
            if not self.visitado[u]:
                self.predecesor[u] = v
                self._DFS_Visitar(u, arbol)
                self.bajo[v] = min(self.bajo[v], self.bajo[u])
                if self.bajo[u] >= self.tiempo_visitado[v]:
                    self.puntos_artic.add(v)
            elif u != self.predecesor[v]:  # Arista de retroceso
                self.bajo[v] = min(self.bajo[v], self.tiempo_visitado[u])
        self.tiempo.incrementar()
        self.tiempo_finalizado[v] = self.tiempo.actual()
