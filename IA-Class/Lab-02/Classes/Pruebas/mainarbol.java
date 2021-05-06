public class mainarbol{
	public static void main(String[] args) {
	ArbolNario ObjArbol = new ArbolNario();
	Coordenada inicial = new Coordenada(1,1);
	Nodo raiz = ObjArbol.insertarRaiz(inicial);

	ObjArbol.insertarNodo(raiz,new Coordenada(1,2),inicial);
	ObjArbol.insertarNodo(raiz,new Coordenada(2,2),inicial);
	ObjArbol.insertarNodo(raiz,new Coordenada(3,2),inicial);
	ObjArbol.insertarNodo(raiz,new Coordenada(4,2),inicial);
	ObjArbol.insertarNodo(raiz,new Coordenada(1,3),new Coordenada(1,2));
	ObjArbol.insertarNodo(raiz,new Coordenada(2,1),new Coordenada(2,2));
	ObjArbol.insertarNodo(raiz,new Coordenada(3,4),new Coordenada(3,2));
	ObjArbol.insertarNodo(raiz,new Coordenada(3,8),new Coordenada(3,2));
	ObjArbol.insertarNodo(raiz,new Coordenada(4,8),new Coordenada(3,8));
	ObjArbol.insertarNodo(raiz,new Coordenada(1,5),new Coordenada(1,2));
	ObjArbol.insertarNodo(raiz,new Coordenada(2,5),new Coordenada(1,5));
	//ObjArbol.recorrer(raiz);
	ObjArbol.recorrerHijosRaiz(raiz);
	/*System.out.println("Buscar "+ObjArbol.buscar(raiz,"2",false));
	System.out.println("Cantidad: "+ObjArbol.cantidadNodos(raiz));
	System.out.println("Altura: "+ObjArbol.altura(raiz));
	System.out.println("Altura2: "+ObjArbol.altura2(raiz));
	System.out.println("Altura3: "+ObjArbol.altura3(raiz,0));
	System.out.println("Hojas: "+ObjArbol.numeroHojas(raiz));
	System.out.println("Nivel Elemento: "+ObjArbol.nivelElemento(raiz,"1.",0));
	System.out.println("---------------------------------------------------------");
	ObjArbol.borrarNodo(raiz,"4",true);
	ObjArbol.recorrer(raiz);
	System.out.println("------------------------------------------------------");
	ObjArbol.recorrerHijosRaiz(raiz);*/
	}
}