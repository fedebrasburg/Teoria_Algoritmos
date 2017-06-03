from creador_grafos import crearDigrafoCompleto
from bellman_ford import BellmanFord
from floyd_warshall import FloydWarshall
from dijkstra import Dijkstra
from parser import Parser
import time
import csv
from os.path import isfile

FLOYDWARSHALL = 0
DIJKSTRA = 1
BELLMANFORD = 2

grafos_a_probar = {}
grafos_a_probar[FLOYDWARSHALL] = [10, 20, 50, 100, 250]
grafos_a_probar[DIJKSTRA] = [10, 20, 50, 100, 250, 500, 1000, 1500, 2000, 2500]
grafos_a_probar[BELLMANFORD] = [10, 20, 50, 100]
grafos_utilizados = [10, 20, 50, 100, 250, 500, 1000, 1500, 2000, 2500]

def devolver_algoritmo(n, grafo):
    if n == FLOYDWARSHALL:
        return FloydWarshall(grafo)
    if n == DIJKSTRA:
        return Dijkstra(grafo)
    if n == BELLMANFORD:
        return BellmanFord(grafo)

def crear_grafos_de_prueba():
    for tamanio_grafo in grafos_utilizados:
        path = "../in/grafoprueba" + str(tamanio_grafo) + ".txt"
        if not isfile(path):
            crearDigrafoCompleto(tamanio_grafo, path)

def realizar_pruebas():
    parser = Parser()
    lista_iteraciones = []

    for tamanio_grafo in grafos_utilizados:
        print 'Leyendo grafo de tamanio ' + str(tamanio_grafo)
        grafo = parser.leer_grafo_dirigido("../in/grafoprueba" + str(tamanio_grafo) + ".txt")

        #  Analizo los algoritmos para todos los caminos minimos del grafo
        for numero_de_algoritmo in [FLOYDWARSHALL, DIJKSTRA, BELLMANFORD]:
            if tamanio_grafo in grafos_a_probar[numero_de_algoritmo]:
                algoritmo = devolver_algoritmo(numero_de_algoritmo, grafo)
                print "\t" + algoritmo.__class__.__name__
                start = time.time()
                if numero_de_algoritmo == FLOYDWARSHALL:
                    algoritmo.resolver_camino_minimo()
                else:
                    for i in range(0, tamanio_grafo - 1):
                        algoritmo.resolver_camino_minimo(str(i))
                end = time.time()
                lista_iteraciones.append((algoritmo.__class__.__name__, str(tamanio_grafo), str(end - start)))

        #  Analizo Dijkstra y Bellman-Ford en forma "unitaria" (Es decir, para un unico origen)
        for numero_de_algoritmo in [DIJKSTRA, BELLMANFORD]:
            if tamanio_grafo in grafos_a_probar[numero_de_algoritmo]:
                algoritmo = devolver_algoritmo(numero_de_algoritmo, grafo)
                print "\t" + algoritmo.__class__.__name__ + "_unitario"
                start = time.time()
                algoritmo.resolver_camino_minimo(str(0))
                end = time.time()
                lista_iteraciones.append((algoritmo.__class__.__name__+"_unitario", str(tamanio_grafo), str(end - start)))

    #  Creo archivo .csv para crear los graficos facilmente
    f = open("../out/corrida_tiempo.csv", 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow(('Algoritmo', 'Tamanio', 'Tiempo'))
        for corrida in lista_iteraciones:
            writer.writerow(corrida)
    finally:
        f.close()

    texto = ""
    for corrida in lista_iteraciones:
        texto += "El algoritmo " + corrida[0] + " para la instancia " + corrida[1] + " tardo " + corrida[2] + "\n"
    f = open("../out/corrida_tiempo.txt", 'w')
    f.write(str(texto))
    f.close()

crear_grafos_de_prueba()
realizar_pruebas()
