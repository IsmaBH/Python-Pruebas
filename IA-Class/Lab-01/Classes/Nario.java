/*
 *Clase que prueba el funcionamiento
 *del arbol n-ario
 */
public class Nario{
	public static void main(String[] args){
		arbol a1 = new arbol();
		Nodo nodo = a1.insertarRaiz("0",1,1);
		a1.raiz.verNodo();
		a1.Insertar(nodo,"1",1,2,"0");
		a1.Insertar(nodo,"2",1,3,"0");
		a1.Insertar(nodo,"3",1,4,"0");

		a1.Insertar(nodo,"1.1",2,1,"1");
		a1.Insertar(nodo,"1.2",2,2,"1");

		a1.Insertar(nodo,"3.1",3,1,"3");
		a1.Insertar(nodo,"3.2",3,2,"3");
		a1.Insertar(nodo,"3.3",3,3,"3");
		a1.Insertar(nodo,"3.4",3,4,"3");

		a1.verHijos(nodo);
	}
}
