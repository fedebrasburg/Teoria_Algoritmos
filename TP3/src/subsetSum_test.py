import time
from subsetSum import subsetSum
s=subsetSum()
print s
for i in range(0,3):
	for j in range(1,6):
		n=10**i*j
		s.generar_problema_aleatorio("../files/subsetSum"+str(n)+".txt",n,-100,100)
		start = time.time()
		print s.resolverProblema("../files/subsetSum"+str(n)+".txt",n*50,0.5),n*50
		end = time.time()
		print "tamanio",n,"tiempo",end-start
n=1000
s.generar_problema_aleatorio("../files/subsetSum"+str(n)+".txt",n,-100,100)
start = time.time()
print s.resolverProblema("../files/subsetSum"+str(n)+".txt",n*50,0.5),n*50
end = time.time()
print "tamanio",n,"tiempo",end-start