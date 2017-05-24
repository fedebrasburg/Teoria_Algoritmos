from random import shuffle
from random import sample
from parser import Parser
from collections import deque


def crear_archivo_problema(nombre, m, n):
    parser = Parser()
    E, H, Q = crear_problema(int(m), int(n))
    parser.escribir_stable_matching(nombre, E, H, Q)

def crear_problema(m, n):
    if m > n:
        print "El numero de hospitales debe ser menor o igual al de pacientes"
        exit()
    E = crear_lista_de_listas_al_azar(m, n)
    H = crear_lista_de_listas_al_azar(n, m)
    Q = constrained_sum_sample_pos(m, n)
    return E, H, Q

def crear_lista_de_listas_al_azar(cantidad_de_elementos, cantidad_de_listas):
    lista = [[i for i in range(cantidad_de_elementos)] for l in range(cantidad_de_listas)]
    [shuffle(l) for l in lista]
    return lista

def resolver_archivo_problema(archivo):
    parser = Parser()
    E, H, Q = parser.leer_stable_matching(archivo)
    return resolver_problema(E, H, Q)

def resolver_archivo_problema_con_archivo_salida(archivo_problema, archivo_salida):
    parser = Parser()
    E, H, Q = parser.leer_stable_matching(archivo_problema)
    P = resolver_problema(E, H, Q)
    f = open(archivo_salida, 'w')
    f.write(str(P))
    f.close()
    return True

def constrained_sum_sample_pos(n, total):
    # http://stackoverflow.com/questions/3589214/generate-multiple-random-numbers-to-equal-a-value-in-python
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    dividers = sorted(sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def reducir_problema(E, H, Q):
    viejo_E = E
    nuevo_E = []
    nuevo_H = H
    for i in range(0, len(Q)):
        nuevo_E = []
        tam_H = len(nuevo_H)
        nuevo_H = nuevo_H + [nuevo_H[i]] * (Q[i] - 1)
        nuevo_tam_H = len(nuevo_H)
        for l in viejo_E:
            nuevo_E += [l[:l.index(i) + 1] + range(tam_H, nuevo_tam_H) + l[l.index(i) + 1:]]
        viejo_E = nuevo_E
    return nuevo_E, nuevo_H

def resolver_problema(E, H, Q):
    n = len(E)
    m = len(H)
    if m > n:
        print "El numero de hospitales debe ser menor o igual al de pacientes"
        exit()
    if n != m:
        E, H = reducir_problema(E, H, Q)

    sig_deseado = [0] * n
    P = [None] * n
    pendientes = deque(range(n))
    while len(pendientes) != 0:
        e = pendientes.pop()
        h_deseado = E[e][sig_deseado[e]]
        sig_deseado[e] += 1

        e_rival = P[h_deseado]
        if e_rival is None:
            P[h_deseado] = e
        elif H[h_deseado][e] > H[h_deseado][e_rival]:
            P[h_deseado] = e
            pendientes.append(e_rival)
        else:
            pendientes.append(e)
    return P
