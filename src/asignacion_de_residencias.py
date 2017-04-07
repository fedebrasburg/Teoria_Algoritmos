from random import shuffle
from parser import Parser
from collections import deque

def crear_archivo_problema(nombre,m,n): 
	parser=Parser()
	E,H,Q=crear_problema(m,n)
	parser.escribirStableMatching(nombre,E,H,Q)

def crear_problema(m,n):
	E=crear_lista_de_listas_al_azar(m,n)
	H=crear_lista_de_listas_al_azar(n,m)
	Q=[n for i in range(m) ]
	return E,H,Q

def crear_lista_de_listas_al_azar(cantidad_de_elementos,cantidad_de_listas):
	lista=[[i for i in range(cantidad_de_elementos)] for l in range(cantidad_de_listas)]
	[shuffle(l) for l in lista]
	return lista
	
def resolver_archivo_problema(archivo):
	parser=Parser()
	E,H,Q=parser.leerStableMatching(archivo)
	return resolver_problema(E,H,Q)

def resolver_problema(E,H,Q):
	n=len(E)
	m=len(H)

	sig_deseado=[0]*n
	P=[None]*m
	pendientes=deque(range(n))
	while (len(pendientes)!=0):
		e=pendientes.pop()
		h_deseado=E[e][sig_deseado[e]]
		sig_deseado[e]+=1

		e_rival=P[h_deseado]
		if e_rival is None:
			P[h_deseado]=e
		elif (H[h_deseado][e]>H[h_deseado][e_rival]):
			P[h_deseado]=e
			pendientes.append(e_rival)
		else:
			pendientes.append(e)
	return P
