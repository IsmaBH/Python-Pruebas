/*
Clase que implementa la clase abstracta Algoritmo y en especifico se dedica
al metodo de busqueda por profundidad
*/
import java.util.ArrayList;

public class Profundidad extends Algoritmo{
	//Atributos
	private ArrayList<Integer> prioridad = new ArrayList<Integer>();
	private ArbolNario decisiones = new ArbolNario();
	private Nodo raiz;
	//Constructor(Se invoca el constructor de la clase base)
	public Profundidad(){
		super("Profundidad");
	}
	//Metodos 
	public void setPrioridad(){
		//Arriba = 38, abajo = 40, izquierda = 37, derecha = 39
		prioridad.add(38);
		prioridad.add(39);
		prioridad.add(40);
		prioridad.add(37);
	}
	public void insertaInicial(Coordenada inicial){
		Nodo raiz = decisiones.insertarRaiz(inicial);
	}
	public int obtenerDireccion(int indice){
		int direccion = 0;
		switch(indice){
			case 0:
				direccion = prioridad.get(0);
				break;
			case 1:
				direccion = prioridad.get(1);
				break;
			case 2:
				direccion = prioridad.get(2);
				break;
			case 3:
				direccion = prioridad.get(3);
				break;
			default:
				System.out.println("No haz escogido ningun tipo,intenta nuevamente");
				System.exit(0);
		}
		return direccion;
	}
	public void reglas(){
		//Code
	}
}