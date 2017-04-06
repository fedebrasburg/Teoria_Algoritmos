INFINITO = float("inf") # Truco magico de python none <any int, <any string

# Yo a la clase Arista tal vez haria que tenga src y dst, y despues en el grafo la manejo como una lista de aristas en vez de como un hash
class Arista(object):
    def __init__(self, peso):
        self.peso = peso
    def peso(self):
        return self.peso

class Grafo(object):
    def __init__(self, cantVertices):
        """Crea un Grafo dirigido (o no) con aristas pesadas (o no)"""
        self.aristas = {}
        self.cantVertices = cantVertices
        for i in range(0, cantVertices):
            self.aristas[i] = {}
            a = self.aristas[i]

    def devolver_cant_nodos(self):
        """Devuelve los nodos del grafo"""
        return self.cantVertices

    def existe_nodo(self, ID):
        """Devuelve True si existe el nodo"""
        return (0 <= ID and ID < self.cantVertices)

    def agregar_arista_no_dirigida(self, id1, id2, peso = 0):
        """Agrego una arista no dirigida entre los nodos con id1 y id2"""
        self.aristas[id1][id2] = Arista(peso)
        self.aristas[id2][id1] = Arista(peso)

    def agregar_arista_dirigida(self, id1, id2, peso = 0):
        """Agrego una arista dirigida entre los nodos con id1 y id2"""
        self.aristas[id1][id2] = Arista(peso)

    def son_vecinos(self, id1, id2):
        """Devuelve si id1 y id2 son vecinos"""
        return (id2 in self.aristas[id1].keys())#Azucar sintactico

    def peso_arista(self, id1, id2):
        """Devuelve el peso de la arista entre id1 e id2"""
        if(self.son_vecinos(id1,id2)):
            return self.aristas[id1][id2].peso
        raise ValueError

    def _DFS_Visitar(self, actual, visitado, padre, lista):
        """Realiza un recorrido DFS"""
        visitado[actual] = True
        lista.append(actual)
        for ID_ady in self.aristas[actual].keys():
            if(visitado[ID_ady] == False):
                padre[ID_ady] = actual
                self._DFS_Visitar(ID_ady, visitado, padre, lista)

    def DFS(self, ID):
        """Hace un recorrido DFS desde un ID"""
        visitado,padre,distancia = self._inicializar_iterador()
        lista = []
        self._DFS_Visitar(ID, visitado, padre, lista)
        return lista

    def _inicializar_iterador(self):
        """Iniciliza variables del iterador"""
        visitado = {}
        distancia = {}
        padre = {}
        for actual in range(0, cantVertices):
            visitado[actual] = False
            distancia[actual] = INFINITO
            padre[actual] = None
        return visitado, padre, distancia