#!/usr/bin/python
""" Usar como: python leer.py "../in/ej2/g1.txt"""
from grafo import Grafo
import sys
if(len(sys.argv)<2):
	print "Mandar el nombre del archivo a leer"
print "Archivo a leer" ,sys.argv[1]
g=Grafo()
g.leer(sys.argv[1])
ve= g.devolver_nodos()
print "vertices" ,ve
ar= g.devolver_aristas()
print "aristas",len(ar)
for a in ar:
	print a