#lo hago no dirigido
#import pila
import heapq


CERO=0
PRIMERO=1
SEGUNDO=2

INFINITO = float("inf")#Truco magico de python none< any int <any string

class Nodo(object):
    def __init__(self,ID,distancia,padre=None):
        self.nombre=ID
        self.distancia=distancia
        self.padre=padre
    def  __cmp__(self,otro):
        if(self.distancia==otro.distancia):
            return 0
        if(self.distancia>otro.distancia):
            return 1
        return -1
    def inverse_cmp(self,otro):
        return -self.__cmp__(otro)
        
class Arista(object):
    def __init__(self,peso):
        self.peso=peso
    def peso(self):
        return self.peso

class Grafo(object):

    def __init__(self):
        """Crea un Grafo no dirigido con aristas sin peso"""
        self.aristas = {}
        self.nodos = {}
        self.nombres ={}

    def devolver_nodos(self):
        """Devuelve los nodos del grafo"""
        return self.nodos.keys()

    def existe_nodo(self,nombre):
        """Devuelve True si existe el nodo"""
        return (nombre in self.nodos.keys())

    def borrar_vertice(self,ID):
        """Borra un vertice que se identifica con ID (si tiene aristas asociadas levanta ValueError"""
        if(self.nombres.has_key(ID) and  len(self.aristas[ID]) == 0):
            self.nodos.pop(self.nombres[ID])
            self.nombres.pop(ID)
            self.aristas.pop(ID)
        raise ValueError

    def borrar_arista_no_dirigida(self,id1,id2):
        """Borra una arista entre id1 y id2 (si no existe devuelve error)"""
        if(aristas[id1].has_key(id2)):
            self.aristas[id1].remove(id2)
	elif (aristas[id2].has_key(id1)):
            self.aristas[id2].remove(id1)
        raise ValueError

    def borrar_arista_dirigida(self,id1,id2):
        """Borra una arista entre id1 y id2 (si no existe devuelve error)"""
        if(aristas[id1].has_key(id2)):
            self.aristas[id1].remove(id2)
        raise ValueError

    def agregar_vertice(self,nombre,ID):
        """Agrega un vertice que se identifica con un nombre y un ID"""
        self.nodos[nombre] = ID
        self.nombres[ID]=nombre
        self.aristas[ID] = {}

    def agregar_arista_no_dirigida(self,id1,id2,peso=0):
        """Agrego una arista sin peso entre los nodos con id1 y id2"""
        self.aristas[id1][id2] = Arista(peso)
        self.aristas[id2][id1] = Arista(peso)

    def agregar_arista_dirigida(self,id1,id2,peso=0):
        """Agrego una arista sin peso entre los nodos con id1 y id2"""
        self.aristas[id1][id2] = Arista(peso)

    def son_vecinos(self,id1,id2):
        """Devuelve si id1 y id2 son vecinos """
        return (id2 in self.aristas[id1].keys())#Azucar sintactico

    def peso_arista(self,id1,id2):
	if(self.son_vecinos(id1,id2)):
		return self.aristas[id1][id2].peso
	raise ValueError
    def leer(self,nombre):
        """Lee un archivo con nombre """
        try:            
            miArch = open(nombre)
            cant_nodos = int(miArch.readline())
            for i  in range(0,cant_nodos):
                linea = miArch.readline()
                numeros = linea.split(" ")
                numeros[PRIMERO] = numeros[PRIMERO].rstrip('\n')
                self.agregar_vertice(numeros[PRIMERO],numeros[CERO])
            cant_aristas = int(miArch.readline())
            for i  in range(0,cant_aristas):
                linea = miArch.readline()
                numeros = linea.split(" ")
                numeros[SEGUNDO] = numeros[SEGUNDO].rstrip('\n')
                self.agregar_arista(numeros[PRIMERO],numeros[SEGUNDO])
            miArch.close()
            return True
        except:
            print "Ocurrio un error leyendo el archivo"
            return False
            
    def _DFS_Visitar(self,actual,visitado,padre,lista):
        """Realiza un recorrido DFS"""
        visitado[actual] = True
        lista.append(actual)
        for ID_ady in self.aristas[self.nodos[actual]].keys():
            ady=self.nombres[ID_ady]
            if(visitado[ady] == False):
                padre[ady] = actual
                self._DFS_Visitar(ady,visitado,padre,lista)


    def DFS(self,nombre):
        """Hace un recorrido DFS desde un nombre """
        visitado,padre,distancia = self._inicializar_iterador()
        lista=[]
        self._DFS_Visitar(nombre,visitado,padre,lista)
        return lista

    def _inicializar_iterador(self):
        """Iniciliza variables del iterador"""
        visitado = {}
        distancia = {}
        padre = {}
        for actual in self.nodos.keys():
            visitado[actual] = False
            distancia[actual] = INFINITO
            padre[actual] = None
        return visitado,padre,distancia

    def BFS(self,nombre,limite=INFINITO):
        """Hace un recorrido BFS desde un nombre y devuelve una lista. 
        Si se le ingresa un limite devuelve todos los nodos a esa distancia."""
        l = []
        c = Cola();
        visitado,padre,distancia = self._inicializar_iterador()
        visitado[nombre] = True
        distancia[nombre] = CERO
        c.encolar(nombre)
        if(limite==INFINITO): l.append(nombre)
        while not c.esta_vacia():
            actual = c.desencolar()
            for ID_ady in self.aristas[self.nodos[actual]].keys():
                ady=self.nombres[ID_ady]
                if(visitado[ady] == False):
                    distancia[ady] = distancia[actual] + 1;
                    if(limite<distancia[ady]): return l
                    if(limite==distancia[ady] or limite==INFINITO): l.append(ady)
                    visitado[ady] = True
                    padre[ady] = actual
                    c.encolar(ady)
        return l

    def dijkstra(self,nombre):
        """Realiza el algoritmo de Djikstra, devuelve las distancias y los padres encontrados desde el nombre"""
        if not nombre in self.nodos: return
        ID=self.nodos[nombre]
        heap=[]
        visitado,padre,distancia = self._inicializar_iterador()
        distancia[nombre] = CERO
        nodo = Nodo(nombre,distancia[nombre],padre[nombre])
        heapq.heappush(heap,nodo)
        while(heap):
            nodo=heapq.heappop(heap)
            nombre=nodo.nombre
            if(not visitado[nombre]):
                visitado[nombre]=True
                padre[nombre]=nodo.padre
                distancia[nombre]=nodo.distancia
                for ID_ady in self.aristas[self.nodos[nombre]].keys():
                    ady= self.nombres[ID_ady]
                    nodo_nuevo=Nodo(ady,distancia[nombre]+1,nombre)    
                    heapq.heappush(heap,nodo_nuevo)
        return distancia,padre



class Cola(object):
    def __init__(self):
        self._datos = []

    def __str__(self):
        return str(self._datos)
    def encolar(self,dato):
        self._datos.append(dato)
        
    def desencolar(self):
        if(len(self._datos) > 0):
            return self._datos.pop(0)
    
    def esta_vacia(self):
        return len(self._datos) == 0

    def ver_tope(self):
        visitado = {}
        if(len(self._datos) > 0):
            return self._datos[0]
        else:
            return None
