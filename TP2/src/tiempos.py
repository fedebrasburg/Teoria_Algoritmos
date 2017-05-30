from creador_grafos import crearDigrafoCompleto
from bellman_ford import BellmanFord
from floyd_warshall import FloydWarshall
from dijkstra import Dijkstra
from grafo import Grafo
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
            crearDigrafoCompleto(tamanio_grafo,path)

def realizar_pruebas():
    parser = Parser()
    lista_iteraciones = []
    algoritmos = [FLOYDWARSHALL, DIJKSTRA, BELLMANFORD]

    grafos_dict = {}
    for tamanio_grafo in grafos_utilizados:
        print 'Leyendo grafo de tamanio ' + str(tamanio_grafo)
        grafo = parser.leer_grafo_dirigido("../in/grafoprueba" + str(tamanio_grafo) + ".txt")
        grafos_dict[tamanio_grafo] = grafo

    for numero_de_algoritmo in algoritmos:
        grafos = grafos_a_probar[numero_de_algoritmo]
        for tamanio_grafo in grafos:
            grafo = grafos_dict[tamanio_grafo]
            algoritmo = devolver_algoritmo(numero_de_algoritmo, grafo)
            print algoritmo.__class__.__name__, tamanio_grafo
            start = time.time()
            if numero_de_algoritmo == FLOYDWARSHALL:
                algoritmo.resolver_camino_minimo()
            else:
                for i in range(0, tamanio_grafo - 1):
                    algoritmo.resolver_camino_minimo(str(i))
            end = time.time()
            lista_iteraciones.append((algoritmo.__class__.__name__, str(tamanio_grafo), str(end - start)))

    for numero_de_algoritmo in [DIJKSTRA, BELLMANFORD]:
        grafos = grafos_a_probar[numero_de_algoritmo]
        for tamanio_grafo in grafos:
            grafo = grafos_dict[tamanio_grafo]
            algoritmo = devolver_algoritmo(numero_de_algoritmo, grafo)
            print algoritmo.__class__.__name__, tamanio_grafo
            start = time.time()
            algoritmo.resolver_camino_minimo(str(i))
            end = time.time()
            lista_iteraciones.append((algoritmo.__class__.__name__+"_unitario", str(tamanio_grafo), str(end - start)))

    f = open("../out/corrida_tiempo.csv", 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow(('Algoritmo', 'tamanio', 'tiempo'))
        for corrida in lista_iteraciones:
            writer.writerow((corrida))
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
