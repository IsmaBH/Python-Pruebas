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
	public void verificaReglas(){}
	public KeyEvent Accion(){}
}