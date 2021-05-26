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
	//private Algoritmo algoritmo;
	String tipo;
	private int x;
	private int y;
	private final int ancho = 40;
	private final int alto = 40;
	private final int movimiento = 40;
	//Constructor de la clase
	public Personaje(int pos_x,int pos_y,String nombre){
		this.x = pos_x;
		this.y = pos_y;
		this.tipo = nombre;
		this.inicial = new Coordenada(pos_x/40,pos_y/40);
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
		/*if (!esVisitado(x/40,y/40)) {
			visitados.add(inicial);
		}*/
	}
	//Metodos de la clase (Acciones del agente)
	//Fase 1 mover al personaje 3 casillas a la derecha
	public void ejecutaAlgoritmo(){
		int laberinto[][] = lab.obtieneLaberinto();
		if (laberinto[y/40][(x/40)+1] != 0 && laberinto[y/40][(x/40)+1] != 1) {
			x = x + movimiento;
		}
	}
}