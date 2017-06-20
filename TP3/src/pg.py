def compraVenta(a):
    if len(a) < 2:
        return []
    posMin = 0
    posMax = 1
    dif = a[posMax] - a[posMin]
    posMinActual = posMin
    for i in range(1, len(a)):
        if a[i] >= a[posMinActual]:
            if (a[i] - a[posMinActual]) > dif:
                dif = a[i] - a[posMinActual]
                posMin = posMinActual
                posMax = i
        else:
            posMinActual = i
    return [posMin, posMax]
