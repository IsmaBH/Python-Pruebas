/*
**Clase abstracta que contiene
**las declaraciones para los diferentes algoritmos
*/
abstract class Algoritmo{
	private String nombre;
	//Declaracion de los metodos abstractos
	//Constructor
	public Algoritmo(String tipo){
		this.nombre = tipo;
	}
	//Metodo de la clase
	public String obtenerNombre(){
		return this.nombre;
	}
}