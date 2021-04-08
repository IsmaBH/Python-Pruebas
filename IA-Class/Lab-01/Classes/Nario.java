/*
 *Clase que prueba el funcionamiento
 *del arbol n-ario
 */
public class Nario{
	public static void main(String[] args){
		arbol a1 = new arbol();
		Nodo nodo = a1.insertarRaiz("0");
		a1.raiz.verNodo();
		a1.InsertarRecursivo(nodo,"1","0");
		a1.InsertarRecursivo(nodo,"2","0");
		a1.InsertarRecursivo(nodo,"3","0");

		a1.InsertarRecursivo(nodo,"1.1","1");
		a1.InsertarRecursivo(nodo,"1.2","1");

		a1.InsertarRecursivo(nodo,"3.1","3");
		a1.InsertarRecursivo(nodo,"3.2","3");
		a1.InsertarRecursivo(nodo,"3.3","3");
		a1.InsertarRecursivo(nodo,"3.4","3");

		a1.verHijosRecursivo(nodo);
	}
}
