from collections import deque
class Arbol:
	#Init method for the class
	def __init__(self, elemento):
		self.hijos = []
		self.elemento = elemento
	#Methods
	#agregarElemento: this method add a element to the tree by a father given
	def agregarElemento(self, arbol, elemento, elementoPadre):
		subarbol = arbol.buscarSubarbol(arbol,elementoPadre)
		subarbol.hijos.append(Arbol(elemento))
	#buscarSubarbol: this methos search for the correct father to add a child
	def buscarSubarbol(self,arbol,elemento):
		if arbol.elemento == elemento:
			return arbol
		for subarbol in arbol.hijos:
			arbolBuscado = arbol.buscarSubarbol(subarbol, elemento)
			if (arbolBuscado != None):
				return arbolBuscado
		return None
	#profundidad: this method count the levels of the tree
	def profundidad(self,arbol):
		if len(arbol.hijos) == 0:
			return 1
		return 1 + max(map(profundidad,arbol.hijos))
	#grado: this method tells the grade of the tree (n-arian)
	def grado(self,arbol):
		return max(map(grado, arbol.hijos) + [len(arbol.hijos)])
	#ejecutarProfundidadPrimero: this method makes a search in depth first
	def ejecutarProfundidadPrimero(self,arbol,funcion):
		funcion(arbol.elemento)
		for hijo in arbol.hijos:
			arbol.ejecutarProfundidadPrimero(hijo, funcion)
	#ejecutarProfundidadPrimero: this method makes a search in width first
	def ejecutarAnchoPrimero(self, arbol, funcion, cola = deque()):
		funcion(arbol.elemento)
		if len(arbol.hijos) > 0:
			cola.extend(arbol.hijos)
		if len(cola) != 0:
			arbol.ejecutarAnchoPrimero(cola.popleft(),funcion,cola)
	#printElement: this is a utilitarian method to print an element of the tree
	def printElement(self,elemento):
		print(elemento)