import sys
import time
from asignacion_de_residencias import *

if len(sys.argv) < 2:
    exit()
i = sys.argv[1]
start = time.time()
resolver_archivo_problema("../in/ej1/asignacion" + str(i) + ".txt")
end = time.time()
print("El problema de asignacion " + str(i) + " tardo " + str(end - start))
