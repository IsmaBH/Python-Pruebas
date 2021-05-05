/*
Clase que representa el algoritmo, es de tipo abstracta por que
el algoritmo a usar puede variar.
*/
abstract class Algoritmo{
	//Atributos de la clase
	private String nombre;
	//Metodos abstractos de la clase
	abstract public void verificaReglas(Coordenada actual,String tipo);
	//Constructor
	public Algoritmo(String nom){
		this.nombre = nom;
	}
	//Metodo toString de la clase
	public String toString(){
		return (nombre);
	}
}