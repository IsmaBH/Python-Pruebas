/*
** CLase donde se implementa al jugador
** con sus caracteristicas
*/
import java.util.ArrayList;
import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.event.KeyEvent;
import javax.swing.JPanel;

public class Personaje extends JPanel{
	//Atributos de la clase
	ArrayList<Coordenada> visitados = new ArrayList<Coordenada>();
	ArrayList<Coordenada> vision = new ArrayList<Coordenada>();
	Laberinto lab = new Laberinto();
	Algoritmo algoritmo;
	private String raza;
	private int x = 80;
	private int y = 80;
	private final int ancho = 40;
	private final int alto = 40;
	private final int movimiento = 40;
	Coordenada inicial = new Coordenada(x/40,y/40);
	//Metodo paint para mostrar en pantalla
	@Override
	public void paint(Graphics grafico){
		if (raza == "Humano") {
			grafico.setColor(Color.red);	
		}else if (raza == "Mono") {
			grafico.setColor(Color.cyan);
		}else if (raza == "Pulpo") {
			grafico.setColor(Color.magenta);
		}
		grafico.fillOval(x,y,ancho,alto);
		grafico.setColor(Color.black);
		grafico.drawOval(x,y,ancho,alto);
		if (!esVisitado(x/40,y/40)) {
			visitados.add(inicial);
			algoritmo.setPrioridad();
			algoritmo.insertaInicial(inicial);
		}
	}
	//Metodos de la clase
	public void ejecutaAlgoritmo(){
		//El primer paso es obtener la direccion a la que se movera el agente
		int evento = algoritmo.obtenerDireccion(0);
		//El segundo paso sera intentar mover a la direccion deseada
		boolean mover = teclaPresionada(evento);
		//Si no se puede mover a la direccion deseada:
		if (mover == false) {
			//Buscar otra direccion
			for (int i = 1; i <= 3 ; i++ ) {
				evento = algoritmo.obtenerDireccion(i);
				mover = teclaPresionada(evento);
				if (mover == true) {
					break;
				}
			}
		}
		//Repetir
	}
	public boolean teclaPresionada(int evento){
		int laberinto[][] = lab.obtieneLaberinto();
		boolean mover = false;
		//Tecla izquierda
		if(evento == 37){
			if(laberinto[y/40][(x/40)-1] != 0 && laberinto[y/40][(x/40)-1] != 1){
				x = x - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				mover = true;
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
			}
		}
		//Tecla derecha
		if(evento == 39){
			if(laberinto[y/40][(x/40)+1] != 0 && laberinto[y/40][(x/40)+1] != 1){
				x = x + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				mover = true;
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
			}
		}
		//Tecla abajo
		if(evento == 40){
			if(laberinto[(y/40)+1][x/40] != 0 && laberinto[(y/40)+1][x/40] != 1){
				y = y + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				mover = true;
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
			}
		}
		//Tecla arriba
		if(evento == 38){
			if(laberinto[(y/40)-1][x/40] != 0 && laberinto[(y/40)-1][x/40] != 1){
				y = y - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				mover = true;
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
			}
		}
		return mover;
	}
	//Metodo Auxiliar para la verificacion de las casillas(sensores)
	public void sensores(int x,int y){
		int laberinto[][] = lab.obtieneLaberinto();
		int caminos = 0;
		vision.clear();
		//Izquierda
		vision.add(new Coordenada((x/40)-1,y/40));
		if (esOcupable(laberinto[y/40][(x/40)-1]) && !esVisitado((x/40)-1,y/40)) {
			caminos++;
		}else{
			visitados.add(new Coordenada((x/40)-1,y/40));
		}
		//Derecha
		vision.add(new Coordenada((x/40)+1,y/40));
		if (esOcupable(laberinto[y/40][(x/40)+1]) && !esVisitado((x/40)+1,y/40)) {
			caminos++;
		}else{
			visitados.add(new Coordenada((x/40)+1,y/40));
		}
		//Abajo
		vision.add(new Coordenada(x/40,(y/40)+1));
		if (esOcupable(laberinto[(y/40)+1][x/40]) && !esVisitado(x/40,(y/40)+1)) {
			caminos++;
		}else{
			visitados.add(new Coordenada(x/40,(y/40)+1));
		}
		//Arriba
		vision.add(new Coordenada(x/40,(y/40)-1));
		if (esOcupable(laberinto[(y/40)-1][x/40]) && !esVisitado(x/40,(y/40)-1)) {
			caminos++;
		}else{
			visitados.add(new Coordenada(x/40,(y/40)-1));
		}
		if (laberinto[(y/40)-1][x/40] != 0 && !esVisitado(x/40,(y/40)-1)) {
			caminos++;
		}
		//Resultados
		if (caminos > 1) {
			System.out.println("Soy una decisión con "+caminos+" caminos");
		}else if(caminos == 1){
			System.out.println("Soy un camino: "+x+","+y+" Con "+caminos+" caminos");
		}else if (caminos == 0) {
			System.out.println("Soy un callejon tengo "+caminos+" disponibles");
		}
	}
	public void posicionActual(int valor,int x,int y){
		int laberinto[][] = lab.obtieneLaberinto();
		if (valor == 2) {
			sensores(x,y);
		}
		if (valor == 3) {
			sensores(x,y);
			System.out.print("Agua: ");
			System.out.println(x+","+y);
		}
		if (valor == 4) {
			sensores(x,y);
			System.out.print("Arena: ");
			System.out.println(x+","+y);
		}
		if (valor == 5) {
			sensores(x,y);
			System.out.println("Bosque");
			System.out.println(x+","+y);
		}
		if (valor == 8) {
			System.out.println("LLegaste a la meta!!");
			System.exit(0);
		}
	}
	//Metodo para buscar en el array un objeto
	public boolean esVisitado(int x,int y){
		boolean existe = false;
		for (int i = 0; i < visitados.size() ; i++ ) {
			if (visitados.get(i).getX() == x && visitados.get(i).getY() == y) {
				existe = true;
				break;
			}
		}
		return existe;
	}
	//Metodo para saber si esta en el campo de vision una posicion
	public boolean esVisible(int x,int y){
		boolean visible = false;
		for (int i = 0; i < vision.size() ; i++ ) {
			if (vision.get(i).getX() == x && vision.get(i).getY() == y) {
				visible = true;
				break;
			}
		}
		return visible;
	}
	public void setRaza(String opcion){
		switch(opcion){
			case "1":
				this.raza = "Humano";
				break;
			case "2":
				this.raza = "Mono";
				break;
			case "3":
				this.raza = "Pulpo";
				break;
			default:
				System.out.println("No haz escogido ningun tipo,intenta nuevamente");
				System.exit(0);
		}
	}
	public void setAlgoritmo(String opcion){
		switch(opcion){
			case "1":
				//this.algoritmo = new Anchura("Anchura");
				break;
			case "2":
				this.algoritmo = new Profundidad();
				break;
			case "3":
				//this.algoritmo = new Aestrella("Aestrella");
				break;
			default:
				System.out.println("No haz escogido ningun tipo,intenta nuevamente");
				System.exit(0);
		}
	}
	public boolean esOcupable(int valor){
		boolean ocupar = false;
		switch(valor){
			//Valor = 1 para la pared/montaña
			case 1:
				if (this.raza == "Sasquatch") {
					ocupar = true;
				}
				break;
			//Valor = 2 para la tierra/camino
			case 2:
				ocupar = true;
				break;
			//Valor = 3 para el agua
			case 3:
				if (this.raza != "Sasquatch") {
					ocupar = true;
				}
				break;
			//Valor = 4 para la arena
			case 4:
				if (this.raza != "Sasquatch" && this.raza != "Pulpo") {
					ocupar = true;
				}
				break;
			//Valor = 5 para el bosque
			case 5:
				ocupar = true;
			//Valor = 6 para el pantano
			case 6:
				ocupar = true;
			//Valor = 7 para la nieve
			case 7:
				if (this.raza != "Mono" && this.raza != "Pulpo") {
					ocupar = true;
				}
			//Valor = 8 para objetivo
			case 8:
				if (this.raza != "Sasquatch") {
					ocupar = true;
				}
			//Default se esta usando para los limites del mapa
			default:
				ocupar = false;
		}
		return ocupar;
	}
}
