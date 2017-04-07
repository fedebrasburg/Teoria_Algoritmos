

PRIMERO = 0
SEGUNDO = 1
# Yo a la clase Arista tal vez haria que tenga src y dst, y despues en el grafo la manejo como una lista de aristas en vez de como un hash

class Arista(object):

    def __init__(self,id1,id2, peso):
        self.id1=id1
        self.id2=id2
        self.peso = peso
    def peso(self):
        return self.peso
    def __str__(self):
        return  str(self.id1) +" a " + str(self.id2) + ",peso "+ str(self.peso)

class Grafo(object):
    def __init__(self):
        """Crea un Grafo dirigido (o no) con aristas pesadas (o no)"""
        self.aristas = {}
        self.vertices = []
        
    def devolver_aristas(self):
        """Devuelve las aristas del grafo"""
        lista_aristas=[]
        for dic_aristas in self.aristas.values():
            for aristas in dic_aristas.values():
                lista_aristas+=[aristas]
        return lista_aristas

    def devolver_vertices(self):
	   return self.vertices

    def devolver_cant_vertices(self):
        """Devuelve los nodos del grafo"""
        return len(self.vertices)

    def existe_nodo(self, ID):
        """Devuelve True si existe el nodo"""
        return (ID in self.vertices)

    def borrar_vertice(self, ID):
        """Borra un vertice que se identifica con ID (si tiene aristas asociadas levanta ValueError)"""
        if (self.existe_nodo(ID) and len(self.aristas[ID]) == 0):
            self.vertices.remove(ID)
            self.aristas.pop(ID)
        else:
            raise ValueError

    def borrar_arista_no_dirigida(self, id1, id2):
        """Borra una arista entre id1 y id2 (si no existe devuelve error)"""
        self.borrar_arista_dirigida(id1,id2)
        self.borrar_arista_dirigida(id2,id1)

    def borrar_arista_dirigida(self, id1, id2):
        """Borra una arista entre id1 y id2 (si no existe devuelve error)"""
        if(self.aristas[id1].has_key(id2)):
            self.aristas[id1].pop(id2)
        else:
            raise ValueError

    def agregar_vertice(self, ID):
        """Agrega un vertice que se identifica con un nombre y un ID"""
        self.vertices.append(ID)
        self.aristas[ID] = {}

    def agregar_arista_no_dirigida(self, id1, id2, peso = 0):
        """Agrego una arista no dirigida entre los nodos con id1 y id2"""
        self.agregar_arista_dirigida(id1, id2, peso)
        self.agregar_arista_dirigida(id2, id1, peso)

    def agregar_arista_dirigida(self, id1, id2, peso = 0):
        """Agrego una arista dirigida entre los nodos con id1 y id2"""
        self.aristas[id1][id2] = Arista(id1, id2, peso)

    def son_vecinos(self, id1, id2):
        """Devuelve si id1 y id2 son vecinos"""
        return (id2 in self.aristas[id1].keys())  # Azucar sintactico

    def peso_arista(self, id1, id2):
        """Devuelve el peso de la arista entre id1 e id2"""
        if(self.son_vecinos(id1,id2)):
            return self.aristas[id1][id2].peso
        raise ValueError

    def adyacentes(self, id):
        """Pide un id de un nodo existe y devuelve una lista de los id de sus adyacentes"""
        adyacentes = []
        for arista in self.aristas[id]:
            adyacentes.append(arista)
        return adyacentes

    def trasponer(self):
        """Traspone el mismo grafo"""
        lista_aristas = self.devolver_aristas()
        for arista in lista_aristas:
            self.borrar_arista_dirigida(arista.id1,arista.id2)
        for arista in lista_aristas:
            self.agregar_arista_dirigida(arista.id2,arista.id1, arista.peso)


    def leer(self, nombre):
        """Lee un archivo con nombre"""  # TODO: Puede que haya que modificar esto para leer el archivo DONE
        try:
		miArch = open(nombre)
	        cant_nodos = int(miArch.readline())
	        for i in range(0, cant_nodos):
		        self.agregar_vertice( i)
	        cant_aristas = int(miArch.readline())
	        for i in range(0, cant_aristas):
		        linea = miArch.readline()
	                numeros = linea.split(" ")
	                numeros[SEGUNDO] = numeros[SEGUNDO].rstrip('\n')
	                self.agregar_arista_dirigida(int(numeros[PRIMERO]),int (numeros[SEGUNDO]))
	        miArch.close()
	        return True
	except:
            print "Ocurrio un error leyendo el archivo"
            return False

    def _DFS_Visitar(self, actual, visitado, padre, lista):
        """Realiza un recorrido DFS"""
        visitado[actual] = True
        lista.append(actual)
        for ID_ady in self.aristas[actual].keys():
            if(visitado[ID_ady] == False):
                padre[ID_ady] = actual
                self._DFS_Visitar(ID_ady, visitado, padre, lista)

    def DFS(self, nombre):
        """Hace un recorrido DFS desde un nombre """
        visitado, padre, distancia = self._inicializar_iterador()
        lista = []
        self._DFS_Visitar(nombre, visitado, padre, lista)
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

