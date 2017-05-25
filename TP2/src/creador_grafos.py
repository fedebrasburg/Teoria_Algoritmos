import grafo
import random
 
def crearDigrafoCompleto(n,nombre):
	cantVertices = n * (n-1)
	file = open(nombre,"w")
	file.write(str(n) + "\n" )
	file.write(str(cantVertices) + "\n" )
	for i in range(n):
		for j in range(n):
			if i != j:
				file.write(str(i) + " " + str(j) + " " + str(random.random()*2) + " " + "\n")
	file.close() 

