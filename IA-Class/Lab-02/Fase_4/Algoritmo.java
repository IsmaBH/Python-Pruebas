/*
**Clase abstracta que contiene
**las declaraciones para los diferentes algoritmos
*/
import java.util.ArrayList;

abstract class Algoritmo{
	private String nombre;
	//Declaracion de los metodos abstractos
	abstract public void insertarInicial(Coordenada inicial);
	abstract public void setPrioridad();
	abstract public int obtenerDireccion(int[][] lab,Personaje p);
	//Constructor
	public Algoritmo(String tipo){
		this.nombre = tipo;
	}
	//Metodo de la clase
	public String obtenerNombre(){
		return this.nombre;
	}
}