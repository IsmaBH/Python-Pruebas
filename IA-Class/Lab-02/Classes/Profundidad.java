/*
Clase que implementa la clase abstracta Algoritmo y en especifico se dedica
al metodo de busqueda por profundidad
*/
import java.awt.event.KeyEvent;
public class Profundidad extends Algoritmo{
	//Atributos
	private ArbolNario decisiones = new ArbolNario();
	//Constructor(Se invoca el constructor de la clase base)
	public Profundidad(){
		super("Profundidad");
	}
	//Metodos (De la clase y los abstractos de la clase base)
	public void insertaInicial(Coordenada inicial){
		Nodo raiz = decisiones.insertarRaiz(inicial)
	}
	public KeyEvent verificaReglas(Coordenada actual,String tipo){
		//Metodo que contiene las reglas con las que se puede mover el agente
		KeyEvent evento = new KeyEvent();
		//Case que verifica el tipo de casilla
		switch(tipo){
			case "desicion":
				//Si es una decision primero verificamos si su posicion ya esta agregada en el arbol
				if (decisiones.buscar(Nodo raiz,Coordenada buscar,boolean encontrado)) {
					
				}
				break;
			case "camino":
				//
				break;
			case "callejon":
				//
				break;
			default:
				System.out.println("Ha ocurrido un error inesperado!!!!!!");
				System.exit(0);
		}
	}
}