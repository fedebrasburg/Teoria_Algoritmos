import time
from subset_sum import SubsetSum

s = SubsetSum()
print s
for i in range(0, 3):
    for j in range(1, 6):
        n = 10 ** i * j
        s.generar_problema_aleatorio("../in/subsetSum" + str(n) + ".txt", n, 0, 100)
        start = time.time()
        print s.resolver_problema("../in/subsetSum" + str(n) + ".txt", n * 50, 0.5), n * 100
        end = time.time()
        print "tamanio", n, "tiempo", end - start
n = 1000
s.generar_problema_aleatorio("../in/subsetSum" + str(n) + ".txt", n, 0, 100)
start = time.time()
print s.resolver_problema("../in/subsetSum" + str(n) + ".txt", n * 50, 0.5), n * 100
end = time.time()
print "tamanio", n, "tiempo", end - start
