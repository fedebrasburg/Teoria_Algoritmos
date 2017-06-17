import random
import pickle
class subsetSum(object):

	def levantar_problema(self,nombre_archivo):
		listaNumeros=[]
		with open(nombre_archivo, 'rb') as f:
			listaNumeros = pickle.load(f)
		return listaNumeros

	def generar_problema_aleatorio(self,nombre_archivo,n,numMin,numMax):
		listaNumeros=[]
		for x in range (0, n):
			listaNumeros.append(random.randint(numMin, numMax))
		with open(nombre_archivo, 'wb') as f:
			pickle.dump(listaNumeros, f)

	def recortar_lista(self,listaNumeros,d):
		if(not listaNumeros):
			return
		#print "\nrecortar lista con d",d
		listaNumeros=sorted(listaNumeros)
		n = len(listaNumeros)
		last = listaNumeros[0]
		nuevaListaNumeros=[listaNumeros[0]]
		#print "ultimo",last
		for i in range(1,n):
			#print "comparacion",listaNumeros[i],last*(1+d)
			if(listaNumeros[i]>(last*(1+d))):
				nuevaListaNumeros.append(listaNumeros[i])
				last=listaNumeros[i]
		#print "\n"
		return nuevaListaNumeros

	def resolverProblema(self,nombre_archivo,t,e):
		listaNumeros=self.levantar_problema(nombre_archivo)
		if(not listaNumeros):
			return
		n = len(listaNumeros)
		L = range(0,n+1)
		L[0] = [0]
		for i in range(1,n):
			#print "paso",i
			#print listaNumeros[i-1]
			nuevalista=map(lambda x: x+listaNumeros[i-1], L[i-1])
			L[i]=list(set(L[i-1] +nuevalista)) 
			#print "lista",L[i]
			L[i]=self.recortar_lista(L[i],e/(2*n))
			#print "lista recortada",L[i]
			L[i]=[j for j in L[i] if j<=t]
			#print "lista filtrada",L[i]
		L[n]=sorted(L[n-1])
		z=L[-1][-1]
		return z

