/*
**Clase que implementa el algorimo de Busqueda por anchura
*/
import java.util.ArrayList;

public class Anchura extends Algoritmo(){
	//Atributos
	private ArbolNario decisiones = new ArbolNario();
	private ArrayList<Integer> prioridad = new ArrayList<Integer>();
	Nodo raiz;
	//Constructor
	public Anchura(String nombre){
		super(nombre);
	}
	//Metodos abstractos
	public void insertarInicial(Coordenada inicial){
		//Metodo auxiliar que permite colocar la raiz del arbol de decisiones
		raiz = decisiones.insertarRaiz(inicial);
	}
	public void setPrioridad(){
		//Este metodo podra ser cambiado para colocar la prioridad de movimiento deseada
		//Ejemplo: Arriba(38),Derecha(39),Izquierda(37),Abajo(40)
		prioridad.add(38);
		prioridad.add(39);
		prioridad.add(37);
		prioridad.add(40);
	}
	public void verDecisiones(){
		decisiones.recorrer(raiz);
	}
	public int obtenerDireccion(int[][] lab,Personaje p){
		int decision = 0;
		for (int i = 0; i < prioridad.size() ;i++ ) {
			//Izquierda
			if (prioridad.get(i) == 37 && p.esOcupable(lab[y/40][(x/40)-1])) {
				boolean compatible = decisiones.obtenerCompatibilidad(raiz,x);
				if (compatible == True) {
				 	decision = 37;
				 	break;
				 } 
			}
			//Derecha
			if (prioridad.get(i) == 39 && p.esOcupable(lab[y/40][(x/40)+1])) {
				boolean compatible = decisiones.obtenerCompatibilidad(raiz,x);
				if (compatible == True) {
				 	decision = 39;
				 	break;
				 } 
			}
			//Arriba
			if (prioridad.get(i) == 38 && p.esOcupable(lab[(y/40)-1][x/40])) {
				boolean compatible = decisiones.obtenerCompatibilidad(raiz,y);
				if (compatible == True) {
				 	decision = 38;
				 	break;
				} 
			}
			//Abajo
			if (prioridad.get(i) == 40 && p.esOcupable(lab[(y/40)+1][x/40])) {
				boolean compatible = decisiones.obtenerCompatibilidad(raiz,x);
				if (compatible == True) {
				 	decision = 40;
				 	break;
				 } 
			}
		}
		return decision;
	}
	public void insertarDesiciones(Coordenada actual,int caminos,Personaje p){}
	public Coordenada esCallejon(int x,int y){}
}