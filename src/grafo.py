PRIMERO = 0
SEGUNDO = 1


class Arista(object):
    def __init__(self, id1, id2, peso):
        self.id1 = id1
        self.id2 = id2
        self.peso = peso

    def peso(self):
        return self.peso

    def __str__(self):
        return str(self.id1) + " a " + str(self.id2) + ", peso " + str(self.peso)


def trasponer(g):
        """Traspone el mismo grafo"""
        g_t = Grafo()
        for vertice in g.devolver_vertices():
            g_t.agregar_vertice(vertice)
        for arista in g.devolver_aristas():
            g_t.agregar_arista_dirigida(arista.id2, arista.id1, arista.peso)
        return g_t


class Grafo(object):
    def __init__(self):
        """Crea un Grafo dirigido (o no) con aristas pesadas (o no)"""
        self.aristas = {}
        self.vertices = []
        
    def devolver_aristas(self):
        """Devuelve las aristas del grafo"""
        lista_aristas = []
        for dic_aristas in self.aristas.values():
            for aristas in dic_aristas.values():
                lista_aristas += [aristas]
        return lista_aristas

    def devolver_vertices(self):
        return self.vertices

    def devolver_cant_vertices(self):
        """Devuelve los nodos del grafo"""
        return len(self.vertices)

    def agregar_vertice(self, id):
        """Agrega un vertice que se identifica con un nombre y un ID"""
        self.vertices.append(id)
        self.aristas[id] = {}

    def agregar_arista_no_dirigida(self, id1, id2, peso=0):
        """Agrego una arista no dirigida entre los nodos con id1 y id2"""
        self.agregar_arista_dirigida(id1, id2, peso)
        self.agregar_arista_dirigida(id2, id1, peso)

    def agregar_arista_dirigida(self, id1, id2, peso=0):
        """Agrego una arista dirigida entre los nodos con id1 y id2"""
        self.aristas[id1][id2] = Arista(id1, id2, peso)

    def son_vecinos(self, id1, id2):
        """Devuelve si id1 y id2 son vecinos"""
        return id2 in self.aristas[id1].keys()  # Azucar sintactico

    def peso_arista(self, id1, id2):
        """Devuelve el peso de la arista entre id1 e id2"""
        if self.son_vecinos(id1, id2):
            return self.aristas[id1][id2].peso
        raise ValueError

    def adyacentes(self, id):
        """Pide un id de un nodo existe y devuelve una lista de los id de sus adyacentes"""
        adyacentes = []
        for arista in self.aristas[id]:
            adyacentes.append(arista)
        return adyacentes

    def _leer(self, nombre, dirigido=False):
        """Lee un grafo (dirigido o no) de un archivo con nombre"""
        try:
            mi_arch = open(nombre)
            cant_nodos = int(mi_arch.readline())
            for i in range(0, cant_nodos):
                self.agregar_vertice(i)
            cant_aristas = int(mi_arch.readline())
            for i in range(0, cant_aristas):
                linea = mi_arch.readline()
                numeros = linea.split(" ")
                numeros[SEGUNDO] = numeros[SEGUNDO].rstrip('\n')
                if dirigido:
                    self.agregar_arista_dirigida(int(numeros[PRIMERO]), int(numeros[SEGUNDO]))
                else:
                    self.agregar_arista_no_dirigida(int(numeros[PRIMERO]), int(numeros[SEGUNDO]))
            mi_arch.close()
            return True
        except:
            return False

    def leer_dirigido(self, nombre):
        self._leer(nombre, True)

    def leer_no_dirigido(self, nombre):
        self._leer(nombre, False)
