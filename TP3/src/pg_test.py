import random
from pg import compraVenta

def minMax(a):
	if len(a) == 2:
		return a
	min = a[0]
	max = a[1]
	for i in range(2,len(a)):
		if max < a[i]:
			max = a[i]
	before = minMax(a[1:])
	if (before[1] - before[0]) > (max - min):
		return before
	return [min,max]

def generadorArray(n):
	a = []
	for _ in range(n):
		a.append(random.randint(1,1000))
	return a

bien = 0
n = 1000
inicial = 2
for i in range(inicial,n):
	a = generadorArray(i)
	rta = compraVenta(a)
	rtaCuadrada = minMax(a)
	if (a[rta[1]] - a[rta[0]]) == (rtaCuadrada[1] - rtaCuadrada[0]):
		bien += 1
	else:
		print a 
		print rtaCuadrada
		print rta
print bien == (n - inicial)
