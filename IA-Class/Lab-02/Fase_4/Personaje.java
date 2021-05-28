/*
**Segunda version de la clase personaje para la implementacion
**de los algoritmos de busqueda variados
*/
import java.util.ArrayList;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.event.KeyEvent;
import javax.swing.JPanel;

public class Personaje extends JPanel{
	//Atributos
	private ArrayList<Coordenada> visitados = new ArrayList<Coordenada>();
	private ArrayList<Coordenada> vision = new ArrayList<Coordenada>();
	private Laberinto lab = new Laberinto();
	private Coordenada inicial;
	private Algoritmo algoritmo;
	String tipo;
	private int x;
	private int y;
	private final int ancho = 40;
	private final int alto = 40;
	private final int movimiento = 40;
	//Constructor de la clase
	public Personaje(int pos_x,int pos_y,String nombre,String al_op){
		this.x = pos_x;
		this.y = pos_y;
		this.tipo = nombre;
		this.inicial = new Coordenada(pos_x/40,pos_y/40);
		setAlgoritmo(al_op);
	}
	//Metodos de la clase (Getters)
	public Coordenada getPosicionActual(){
		Coordenada actual = new Coordenada(this.x,this.y);
		return actual;
	}
	public String getTipo(){
		return this.tipo;
	}
	public ArrayList<Coordenada> getVisitados(){
		return this.visitados;
	}
	public ArrayList<Coordenada> getVision(){
		return this.vision;
	}
	public Coordenada getPosicionInicial(){
		return this.inicial;
	}
	//Metodo set del algoritmo
	public void setAlgoritmo(String opcion){
		switch (opcion){
			case "1":
				algoritmo = new Profundidad("Profundidad");
				algoritmo.setPrioridad();
				break;
			case "2":
				break;
			case "3":
				break;
			default: 
				System.out.println("No haz escogido ningun tipo,intenta nuevamente");
				System.exit(0);
		}
	}
	//Metodo paint de la clase
	@Override
	public void paint(Graphics grafico){
		if (tipo == "Humano") {
			grafico.setColor(Color.red);	
		}else if (tipo == "Mono") {
			grafico.setColor(Color.cyan);
		}else if (tipo == "Pulpo") {
			grafico.setColor(Color.magenta);
		}
		grafico.fillOval(x,y,ancho,alto);
		grafico.setColor(Color.black);
		grafico.drawOval(x,y,ancho,alto);
		if (!esVisitado(x/40,y/40)) {
			visitados.add(inicial);
		}
	}
	//Metodos de la clase (Acciones del agente)
	public void ejecutaAlgoritmo(){
		int laberinto[][] = lab.obtieneLaberinto();
		int direccion = algoritmo.obtenerDireccion(laberinto,retornarPersonaje());
		switch(direccion){
			case 37:
				x = x - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
				break;
			case 38:
				y = y - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
				break;
			case 39:
				x = x + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
				break;
			case 40:
				y = y + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
				break;
			default:
				System.out.println("No se encontro la salida");
				System.exit(0);
		}
	}
	//Metodos auxiliares
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
	//Metodo que determina si la casilla es ocupable por el tipo de actor
	public boolean esOcupable(int valor){
		boolean ocupar = false;
		switch(valor){
			//Valor = 1 para la pared/montaña
			case 1:
				if (this.tipo == "Sasquatch") {
					ocupar = true;
				}
				break;
			//Valor = 2 para la tierra/camino
			case 2:
				ocupar = true;
				break;
			//Valor = 3 para el agua
			case 3:
				if (this.tipo != "Sasquatch") {
					ocupar = true;
				}
				break;
			//Valor = 4 para la arena
			case 4:
				if (this.tipo != "Sasquatch" && this.tipo != "Pulpo") {
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
				if (this.tipo != "Mono" && this.tipo != "Pulpo") {
					ocupar = true;
				}
			//Valor = 8 para objetivo
			case 8:
				if (this.tipo != "Sasquatch") {
					ocupar = true;
				}
			//Default se esta usando para los limites del mapa
			default:
				ocupar = false;
		}
		return ocupar;
	}
	//Metodo que comfirma el tipo de casilla en la que esta el actor
	public void posicionActual(int valor,int x,int y){
		int laberinto[][] = lab.obtieneLaberinto();
		if (valor == 2) {
			//Suelo
			sensores(x,y);
		}
		if (valor == 3) {
			//Agua
			sensores(x,y);
		}
		if (valor == 4) {
			//Arena
			sensores(x,y);
		}
		if (valor == 5) {
			//Bosque
			sensores(x,y);
		}
		if (valor == 8) {
			System.out.println("LLegaste a la meta!!");
		}
	}
	//Metodo que determina lo que puede percibir el actor
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
			System.out.println("Soy un camino!");
		}else if (caminos == 0) {
			System.out.println("Soy un callejon tengo "+caminos+" caminos disponibles");
		}
	}
	//Metodo que retorna la informacion del personaje actual
	public Personaje retornarPersonaje(){
		return this;
	}
}