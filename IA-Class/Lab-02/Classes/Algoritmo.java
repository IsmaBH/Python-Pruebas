/*
Clase que representa el algoritmo, es de tipo abstracta por que
el algoritmo a usar puede variar.
*/
import java.util.ArrayList;

abstract class Algoritmo{
	//Atributos de la clase
	private String nombre;
	//Metodos abstractos de la clase
	abstract public void setPrioridad();
	abstract public void insertaInicial(Coordenada inicial);
	abstract public int obtenerDireccion(int indice);
	abstract public void reglas();
	//Constructor
	public Algoritmo(String nom){
		this.nombre = nom;
	}
	//Metodo toString de la clase
	public String toString(){
		return (nombre);
	}
}