#Implementacion del arbol de busqueda con un ejemplo de los Simpson
from arbol import *
#Inicio del programa principal
abuela = "Jacqueline Gurney"
marge = "Marge Bouvier"
patty = "Patty Bouvier"
selma = "Selma Bouvier"
bart = "Bart Simpson"
lisa = "Lisa Simpson"
maggie = "Maggie Simpson"
ling = "Ling Bouvier"

arbol = Arbol(abuela)
arbol.agregarElemento(arbol,patty,abuela)
arbol.agregarElemento(arbol,selma,abuela)
arbol.agregarElemento(arbol,ling,selma)
arbol.agregarElemento(arbol,marge,abuela)
arbol.agregarElemento(arbol,bart,marge)
arbol.agregarElemento(arbol,lisa,marge)
arbol.agregarElemento(arbol,maggie,marge)
print("Busqueda por profundidad")
arbol.ejecutarProfundidadPrimero(arbol,arbol.printElement)
print("-------------------------------------------------")
print("Busqueda por anchura")
arbol.ejecutarAnchoPrimero(arbol,arbol.printElement)