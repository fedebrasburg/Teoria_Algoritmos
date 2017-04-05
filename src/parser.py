CERO = 0
PRIMERO = 1
SEGUNDO = 2

class Parser(object):

    def __init__(self):

    def leer(self, nombre):
        """Lee un archivo con nombre"""
        grafo = Grafo()
        try:
            miArch = open(nombre)
            cant_nodos = int(miArch.readline())
            cant_aristas = int(miArch.readline())
            for i in range(0, cant_nodos):
                # linea = miArch.readline()
                # numeros = linea.split(" ")
                numeros[PRIMERO] = numeros[PRIMERO].rstrip('\n')
                self.agregar_vertice(numeros[PRIMERO],numeros[CERO])
            for i in range(0, cant_aristas):
                linea = miArch.readline()
                numeros = linea.split(" ")
                numeros[SEGUNDO] = numeros[SEGUNDO].rstrip('\n')
                self.agregar_arista(numeros[PRIMERO],numeros[SEGUNDO])
            miArch.close()
            return True
        except:
            print "Ocurrio un error leyendo el archivo"
            return False