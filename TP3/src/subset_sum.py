import random
import pickle


class SubsetSum(object):
    def levantar_problema(self, nombre_archivo):
        listaNumeros = []
        with open(nombre_archivo, 'rb') as f:
            listaNumeros = pickle.load(f)
        return listaNumeros

    def generar_problema_aleatorio(self, nombre_archivo, n, numMin, numMax):
        listaNumeros = []
        if (numMin < 0) or (numMax < 0) or (numMax < numMin):
            print "Error en los enteros minimos y maximos"
            return
        for x in range(0, n):
            listaNumeros.append(random.randint(numMin, numMax))
        with open(nombre_archivo, 'wb') as f:
            pickle.dump(listaNumeros, f)

    def recortar_lista(self, listaNumeros, d):
        if not listaNumeros:
            return
        listaNumeros = sorted(listaNumeros)
        n = len(listaNumeros)
        last = listaNumeros[0]
        nuevaListaNumeros = [listaNumeros[0]]
        for i in range(1, n):
            if listaNumeros[i] > (last * (1 + d)):
                nuevaListaNumeros.append(listaNumeros[i])
                last = listaNumeros[i]
        return nuevaListaNumeros

    def resolver_problema(self, nombre_archivo, t, e):
        listaNumeros = self.levantar_problema(nombre_archivo)
        if not listaNumeros:
            return
        n = len(listaNumeros)
        L = range(0, n + 1)
        L[0] = [0]
        for i in range(1, n):
            nuevaLista = map(lambda x: x + listaNumeros[i - 1], L[i - 1])
            L[i] = list(set(L[i - 1] + nuevaLista))
            L[i] = self.recortar_lista(L[i], e / (2 * n))
            L[i] = [j for j in L[i] if j <= t]
        L[n] = sorted(L[n - 1])
        z = L[-1][-1]
        return z
