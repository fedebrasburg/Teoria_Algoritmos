CERO=0
PRIMERO=1
SEGUNDO=2

INFINITO = float("inf") # Truco magico de python none <any int, <any string

class Nodo(object):
    def __init__(self,ID,distancia,padre=None):
        self.nombre=ID
        self.distancia=distancia
        self.padre=padre # TODO: Esto no es medio turbio? jajaj
    def __cmp__(self,otro):
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
        """Crea un Grafo dirigido (o no) con aristas pesadas (o no)"""
        self.aristas = {}
        self.nodos = {}
        self.nombres ={}

    def devolver_nodos(self):
        """Devuelve los nodos del grafo"""
        return self.nodos.keys()

    def existe_nodo(self,nombre):
        """Devuelve True si existe el nodo"""
        return (nombre in self.nodos.keys())

    # TODO: En estos 3 métodos de borrar, el raise no iría en un else, ya que así lanza la execpción siempre? Pregunto, no sé cómo lo maneja Python jajaj
    def borrar_vertice(self,ID):
        """Borra un vertice que se identifica con ID (si tiene aristas asociadas levanta ValueError)"""
        # TODO: Sino hacer que elimine todas las aristas y después el nodo?
        if (self.nombres.has_key(ID) and len(self.aristas[ID]) == 0):
            self.nodos.pop(self.nombres[ID])
            self.nombres.pop(ID)
            self.aristas.pop(ID)
        raise ValueError

    def borrar_arista_no_dirigida(self,id1,id2):
        """Borra una arista entre id1 y id2 (si no existe devuelve error)"""
        if (aristas[id1].has_key(id2)):
            self.aristas[id1].remove(id2)
        elif (aristas[id2].has_key(id1)): # TODO: No debería ser un if directamente, en vez de elif? Porque eliminaría una sola de las 2 así
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
        """Agrego una arista no dirigida entre los nodos con id1 y id2"""
        self.aristas[id1][id2] = Arista(peso)
        self.aristas[id2][id1] = Arista(peso)

    def agregar_arista_dirigida(self,id1,id2,peso=0):
        """Agrego una arista dirigida entre los nodos con id1 y id2"""
        self.aristas[id1][id2] = Arista(peso)

    def son_vecinos(self,id1,id2):
        """Devuelve si id1 y id2 son vecinos"""
        return (id2 in self.aristas[id1].keys())#Azucar sintactico

    def peso_arista(self,id1,id2):
        if(self.son_vecinos(id1,id2)):
            return self.aristas[id1][id2].peso
        raise ValueError

    def leer(self,nombre):
        """Lee un archivo con nombre""" # TODO: Puede que haya que modificar esto para leer el archivo
        try:
            miArch = open(nombre)
            cant_nodos = int(miArch.readline())
            for i in range(0,cant_nodos):
                linea = miArch.readline()
                numeros = linea.split(" ")
                numeros[PRIMERO] = numeros[PRIMERO].rstrip('\n')
                self.agregar_vertice(numeros[PRIMERO],numeros[CERO])
            cant_aristas = int(miArch.readline())
            for i in range(0,cant_aristas):
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
