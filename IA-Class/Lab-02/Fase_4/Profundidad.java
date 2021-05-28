/*
**Clase que implementa el algoritmo de 
**busqueda por profundidad desde la
**clase abstracta Algoritmo
*/
import java.util.ArrayList;

public class Profundidad extends Algoritmo{
	//Atributos
	private ArbolNario decisiones = new ArbolNario();
	private ArrayList<Integer> prioridad = new ArrayList<Integer>();
	//Constructor
	public Profundidad(String nombre){
		super(nombre);
	}
	//Implementacion de los metodos abstractos
	public void insertarInicial(Coordenada inicial){
		//Metodo auxiliar que permite colocar la raiz del arbol de decisiones
		Nodo raiz = decisiones.insertarRaiz(inicial);
	}
	public void setPrioridad(){
		//Este metodo podra ser cambiado para colocar la prioridad de movimiento deseada
		//Ejemplo: Arriba(38),Derecha(39),Izquierda(37),Abajo(40)
		prioridad.add(38);
		prioridad.add(39);
		prioridad.add(37);
		prioridad.add(40);
	}
	public int obtenerDireccion(int[][] lab,Personaje p){
		//Metodo que evaluara el laberinto y determinara el siguiente movimiento del agente
		int decision = 0;
		for (int i = 0; i < prioridad.size() ; i++) {
			switch(prioridad.get(i)){
				//Izquierda
				case 37:
					if (lab[p.getPosicionActual().getY()/40][(p.getPosicionActual().getX()/40)-1] != 0 && lab[p.getPosicionActual().getY()/40][(p.getPosicionActual().getX()/40)-1] != 1 && !p.esVisitado((p.getPosicionActual().getX()/40)-1,p.getPosicionActual().getY()/40)) {
						decision = 37;
					}
					break;
				//Arriba
				case 38:
					if (lab[(p.getPosicionActual().getY()/40)-1][p.getPosicionActual().getX()/40] != 0 && lab[(p.getPosicionActual().getY()/40)-1][p.getPosicionActual().getX()/40] != 1 && !p.esVisitado(p.getPosicionActual().getX()/40,(p.getPosicionActual().getY()/40)-1)) {
						decision = 38;
					}
					break;
				//Derecha
				case 39:
					if (lab[p.getPosicionActual().getY()/40][(p.getPosicionActual().getX()/40)+1] != 0 && lab[p.getPosicionActual().getY()/40][(p.getPosicionActual().getX()/40)+1] != 1 && !p.esVisitado((p.getPosicionActual().getX()/40)+1,p.getPosicionActual().getY()/40)) {
						decision = 39;
					}
					break;
				//Abajo
				case 40:
					if (lab[(p.getPosicionActual().getY()/40)+1][p.getPosicionActual().getX()/40] != 0 && lab[(p.getPosicionActual().getY()/40)+1][p.getPosicionActual().getX()/40] != 1 && !p.esVisitado(p.getPosicionActual().getX()/40,(p.getPosicionActual().getY()/40)+1)) {
						decision = 40;
					}
					break;
				default:
					decision = 0;
					break;
			}
		}
		return decision;
	}
}