PRIMERO = 0
SEGUNDO = 1
TERCERO = 2


class Arista(object):
    def __init__(self, id1, id2, peso):
        self.id1 = id1
        self.id2 = id2
        self.peso = peso

    def peso(self):
        return self.peso

    def __str__(self):
        return str(self.id1) + " a " + str(self.id2) + ", peso " + str(self.peso)


class Grafo(object):
    def __init__(self):
        """Crea un Grafo dirigido (o no) con aristas pesadas (o no)"""
        self.aristas = {}
        self.vertices = []

    def devolver_aristas(self):
        """Devuelve las aristas del grafo"""
        return self.aristas

    def devolver_aristas_list(self):
        lista = []
        for i in self.aristas:
            for j in self.aristas[i].values():
                lista += j
        return lista

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
        arista = Arista(id1, id2, peso)
        if id2 in self.aristas[id1]:
            self.aristas[id1][id2].append(arista)
        else:
            self.aristas[id1][id2] = [arista]

    def son_vecinos(self, id1, id2):
        """Devuelve si id1 y id2 son vecinos"""
        try:
            if self.aristas[id1][id2]:
                return True
            return False
        except:
            return False

    def peso_arista(self, id1, id2):
        """Devuelve el peso de la arista entre id1 e id2"""
        if self.son_vecinos(id1, id2):
            return self.aristas[id1][id2].peso
        raise ValueError

    def borrar_vertice(self, id):
        self.vertices.remove(id)
        del self.aristas[id]

    def borrar_arista_no_dirigida(self, id1, id2):
        self.borrar_arista_dirigida(id1, id2)
        self.borrar_arista_dirigida(id2, id1)

    def borrar_arista_dirigida(self, id1, id2):
        if self.son_vecinos(id1, id2):
            del self.aristas[id1][id2]

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
                peso = 0
                if len(numeros) > 2:
                    peso = numeros[TERCERO].rstrip('\n')
                else:
                    numeros[SEGUNDO] = numeros[SEGUNDO].rstrip('\n')
                if dirigido:
                    self.agregar_arista_dirigida(int(numeros[PRIMERO]), int(numeros[SEGUNDO]), peso)
                else:
                    self.agregar_arista_no_dirigida(int(numeros[PRIMERO]), int(numeros[SEGUNDO]), peso)
            mi_arch.close()
            return True
        except:
            return False

    def leer_dirigido(self, nombre):
        self._leer(nombre, True)

    def leer_no_dirigido(self, nombre):
        self._leer(nombre, False)
