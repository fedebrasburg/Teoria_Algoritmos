
from creador_grafos import crearDigrafoCompleto
from bellman_ford import BellmanFord
from floyd_warshall import FloydWarshall
from dijkstra import Dijkstra
from grafo import Grafo
from parser import Parser
import time
import csv
from os.path import isfile
FLOYDWARSHALL=0
DIJKSTRA=1
BELLMANFORD=2
cantidad_de_algoritmos=3

grafos_a_probar=range(0,cantidad_de_algoritmos)
grafos_a_probar[FLOYDWARSHALL] =[10,20,50,100,250]
grafos_a_probar[DIJKSTRA]=[10,20,50,100,250,500,1000,1500,2000,2500]
grafos_a_probar[BELLMANFORD]=[10,20,50,100]
grafos_utilizados= [10,20,50,100,250,500,1000,1500,2000,2500]

def devolver_algoritmo(n,g):
	if(n==FLOYDWARSHALL):
		return 	FloydWarshall(g)
	if(n==DIJKSTRA):
		return Dijkstra(g)
	if(n==BELLMANFORD):
		return BellmanFord(g)

def crear_grafos_de_prueba():
	for tamanio_grafo in grafos_utilizados:
		path=  "../out/grafoprueba"+str(tamanio_grafo)+".txt"
		if not isfile(path):
			crearDigrafoCompleto(tamanio_grafo,path)

def realizar_pruebas():
	parser=Parser()
	l=[]
	algoritmos=range(0,cantidad_de_algoritmos)
	for numero_de_algoritmo in algoritmos: 
		grafos=grafos_a_probar[numero_de_algoritmo]
		for tamanio_grafo in grafos:
			g=parser.leer_grafo_dirigido("../out/grafoprueba"+str(tamanio_grafo)+".txt")
			algoritmo=devolver_algoritmo(numero_de_algoritmo,g)
			print algoritmo.__class__.__name__,tamanio_grafo
			start = time.time()
			if(numero_de_algoritmo==FLOYDWARSHALL):
				algoritmo.resolver_camino_minimo()
			else:
				for j in range(0,tamanio_grafo-1):
					algoritmo.resolver_camino_minimo(str(j))	
			end = time.time()
			l.append((algoritmo.__class__.__name__,str(tamanio_grafo),str(end - start)))
		
	f = open("../out/corrida_tiempo.csv", 'wt')
	try:
	    writer = csv.writer(f)
	    writer.writerow( ('Algoritmo', 'tamanio', 'tiempo'))
	    for corrida in l:
	    	writer.writerow((corrida))
	finally:
		f.close()
	

	texto=""
	for corrida in l:
		texto +="El algoritmo " + corrida[0] + " para la instancia " + corrida[1] +" tardo "+corrida[2]+"\n"
	f = open("../out/corrida_tiempo.txt", 'w')
	f.write(str(texto))
	f.close()
	

crear_grafos_de_prueba()
realizar_pruebas()