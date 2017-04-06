from grafo import Grafo

CERO = 0
UNO = 1

class Parser(object):

    def escribirStableMatching(self, nombre, E, H, Q):
        """Escribe un archivo del tipo Stable Matching"""
        try:
            miArch = open(nombre, 'w')
            n = len(E)
            miArch.write(str(n) + '\n')
            for i in range(0, n):
                numeros = " ".join(str(x) for x in E[i]) + '\n' # Deberia haber m numeros
                miArch.write(numeros)
            m = len(H)
            miArch.write(str(m) + '\n')
            for i in range(0, m):
                numeros = " ".join(str(x) for x in H[i]) + '\n' # Deberia haber n numeros
                miArch.write(numeros)
            numeros = " ".join(str(x) for x in Q) + '\n' # Deberia haber m numeros
            miArch.write(numeros)
            miArch.close()
            return True
        except:
            print "Ocurrio un error leyendo el archivo"
            return False

    def leerGrafoNoDirigido(self, nombre):
        """Lee un archivo de un grafo dirigido"""
        # idem dirigido, cambiando el metodo a llamar del grafo

    def leerGrafoDirigido(self, nombre):
        """Lee un archivo de un grafo dirigido sin peso"""
        try:
            miArch = open(nombre)
            cant_nodos = int(miArch.readline())
            print(cant_nodos)
            grafo = Grafo(cant_nodos)
            cant_aristas = int(miArch.readline())
            print(cant_aristas)
            for i in range(0, cant_aristas):
                linea = miArch.readline()
                linea = linea.rstrip('\n')
                numeros = map(int, linea.split(" "))
                print(str(numeros[CERO]) + " " + str(numeros[UNO]))
                grafo.agregar_arista_dirigida(numeros[CERO], numeros[UNO])
            miArch.close()
            return grafo
        except:
            print "Ocurrio un error leyendo el archivo"
            return False