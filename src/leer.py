#!/usr/bin/python
""" Usar como: python leer.py "../in/ej2/g1.txt"""
from grafo import Grafo
from parser import Parser
import sys

if(len(sys.argv) < 2):
	print "Mandar el nombre del archivo a leer"
print "Archivo a leer:", sys.argv[1]
p = Parser()
g = p.leerGrafoDirigido(sys.argv[1])
ve = g.devolver_vertices()
print "vertices", ve
ar = g.devolver_aristas()
print "aristas", len(ar)
for a in ar:
	print a
