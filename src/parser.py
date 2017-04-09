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
            print "Ocurrio un error leyendo el archivo de Stable Matching " + nombre
            return False

    def _read_line(self,miArch):
        return miArch.readline().strip("\n")

    def _read_line_int_list(self,miArch):
        return [int(i) for i in self._read_line(miArch).split(" ")]

    def leerStableMatching(self, nombre):
        """Escribe un archivo del tipo Stable Matching"""
        try:
            miArch = open(nombre, 'r')
            n = int(self._read_line(miArch))
            E =[]
            for i in range(0, n):
                E.append(self._read_line_int_list(miArch))   
            m = int(self._read_line(miArch))
            H =[]
            for i in range(0, m):
                H.append(self._read_line_int_list(miArch))
            Q=self._read_line_int_list(miArch)
            miArch.close()
            return E,H,Q
        except:
            print "Ocurrio un error leyendo el archivo"
            return False

    def leerGrafoNoDirigido(self, nombre):
        """Lee un archivo de un grafo no dirigido sin peso"""
        try:
            grafo = Grafo()
            grafo.leerNoDirigido(nombre)
            return grafo
        except:
            print "Ocurrio un error leyendo el archivo de grafo no dirigido " + nombre
            return False

    def leerGrafoDirigido(self, nombre):
        """Lee un archivo de un grafo dirigido sin peso"""
        try:
            grafo = Grafo()
            grafo.leerDirigido(nombre)
            return grafo
        except:
            print "Ocurrio un error leyendo el archivo de grafo dirigido " + nombre
            return False
