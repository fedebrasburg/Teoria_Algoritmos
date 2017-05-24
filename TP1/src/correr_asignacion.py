import sys
import os
import time
from asignacion_de_residencias import *

if len(sys.argv) != 5:
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print "\nPara correr el programa se necesitan 4 parametros:\n" \
              "\t-1.El nombre del archivo a crearse en la entrada\n" \
              "\t-2.El numero m de hospitales\n" \
              "\t-3.El numero n de pacientes\n" \
              "\t-4.El nombre del archivo de salida\n" \
              "Un ejemplo que corre correctamente es (desde la carpeta src):\n" \
              "\tpython correr_asignacion.py 'in.txt' 100 100 'out.txt'\n " \
              "Recuerde revisar en las carpetas in/ y out/ para ver los archivos correspondientes"
    else:
        print "Revise que esten bien las entradas. Para mas ayuda ingrese -h o --help"
    exit()
cwd = os.getcwd().split('/')
if cwd[len(cwd) - 1] != "src":
    print "El programa debe ser corrido desde la carpeta 'src' del proyecto"
    exit()

nombre_archivo_problema = "../in/" + sys.argv[1]
nombre_archivo_salida = "../out/" + sys.argv[4]
m = sys.argv[2]
n = sys.argv[3]
crear_archivo_problema(nombre_archivo_problema, m, n)
start = time.time()
resolver_archivo_problema_con_archivo_salida(nombre_archivo_problema, nombre_archivo_salida)
end = time.time()
print("El problema de asignacion " + sys.argv[1] + " tardo " + str(end - start))
