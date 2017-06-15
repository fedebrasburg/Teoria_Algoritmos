import random


def crearDigrafoCompleto(n, nombre):
    cantAristas = n * (n - 1)
    arch = open(nombre, 'w')
    arch.write(str(n) + "\n")
    arch.write(str(cantAristas) + "\n")
    for i in range(n):
        for j in range(n):
            if i != j:
                arch.write(str(i) + " " + str(j) + " " + str(random.random() * 2) + " " + "\n")  # Crea una arista del vertice i al vertice j con un valor al azar entre 0 y 2
    arch.close()
