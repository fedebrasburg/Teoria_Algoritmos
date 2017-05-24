from grafo import Grafo

CERO = 0
UNO = 1


class Parser(object):

    def escribir_stable_matching(self, nombre, E, H, Q):
        """Escribe un archivo del tipo Stable Matching"""
        try:
            mi_arch = open(nombre, 'w')
            n = len(E)
            mi_arch.write(str(n) + '\n')
            for i in range(0, n):
                numeros = " ".join(str(x) for x in E[i]) + '\n'  # Deberia haber m numeros
                mi_arch.write(numeros)
            m = len(H)
            mi_arch.write(str(m) + '\n')
            for i in range(0, m):
                numeros = " ".join(str(x) for x in H[i]) + '\n'  # Deberia haber n numeros
                mi_arch.write(numeros)
            numeros = " ".join(str(x) for x in Q) + '\n'  # Deberia haber m numeros
            mi_arch.write(numeros)
            mi_arch.close()
            return True
        except:
            print "Ocurrio un error leyendo el archivo de Stable Matching " + nombre
            return False

    def _read_line(self, mi_arch):
        return mi_arch.readline().strip("\n")

    def _read_line_int_list(self, mi_arch):
        return [int(i) for i in self._read_line(mi_arch).split(" ")]

    def leer_stable_matching(self, nombre):
        """Escribe un archivo del tipo Stable Matching"""
        try:
            mi_arch = open(nombre, 'r')
            n = int(self._read_line(mi_arch))
            E = []
            for i in range(0, n):
                E.append(self._read_line_int_list(mi_arch))
            m = int(self._read_line(mi_arch))
            H = []
            for i in range(0, m):
                H.append(self._read_line_int_list(mi_arch))
            Q = self._read_line_int_list(mi_arch)
            mi_arch.close()
            return E, H, Q
        except:
            print "Ocurrio un error leyendo el archivo"
            return False

    def leer_grafo_no_dirigido(self, nombre):
        """Lee un archivo de un grafo no dirigido sin peso"""
        try:
            grafo = Grafo()
            grafo.leer_no_dirigido(nombre)
            return grafo
        except:
            print "Ocurrio un error leyendo el archivo de grafo no dirigido " + nombre
            return False

    def leer_grafo_dirigido(self, nombre):
        """Lee un archivo de un grafo dirigido sin peso"""
        try:
            grafo = Grafo()
            grafo.leer_dirigido(nombre)
            return grafo
        except:
            print "Ocurrio un error leyendo el archivo de grafo dirigido " + nombre
            return False
