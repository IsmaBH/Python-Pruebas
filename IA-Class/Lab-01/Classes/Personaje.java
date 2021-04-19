/*
** CLase donde se implementa al jugador
** con sus caracteristicas
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
	//Atributos de la clase
	ArrayList<Coordenada> visitados = new ArrayList<Coordenada>();
	ArrayList<Coordenada> visibilidad = new ArrayList<Coordenada>();
	Laberinto lab = new Laberinto();
	private String raza;
	private int x = 40;
	private int y = 40;
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
		}else if (raza == "pulpo") {
			grafico.setColor(Color.magenta);
		}
		grafico.fillOval(x,y,ancho,alto);
		grafico.setColor(Color.black);
		grafico.drawOval(x,y,ancho,alto);
		if (!esVisitado(x/40,y/40)) {
			visitados.add(inicial);
		}
	}
	//Metodos de la clase
	public void teclaPresionada(KeyEvent evento){
		int laberinto[][] = lab.obtieneLaberinto();
		//Tecla izquierda
		if(evento.getKeyCode() == 37){
			if(laberinto[y/40][(x/40)-1] != 0){
				x = x - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
			}
		}
		//Tecla derecha
		if(evento.getKeyCode() == 39){
			if(laberinto[y/40][(x/40)+1] != 0){
				x = x + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
			}
		}
		//Tecla abajo
		if(evento.getKeyCode() == 40){
			if(laberinto[(y/40)+1][x/40] != 0){
				y = y + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
			}
		}
		//Tecla arriba
		if(evento.getKeyCode() == 38){
			if(laberinto[(y/40)-1][x/40] != 0){
				y = y - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!esVisitado(x/40,y/40)) {
					visitados.add(new Coordenada(x/40,y/40));
				}
			}
		}
	}
	//Metodo Auxiliar para la verificacion de las casillas(sensores)
	public void sensores(int x,int y){
		int laberinto[][] = lab.obtieneLaberinto();
		int caminos = 0;
		if (laberinto[y/40][(x/40)-1] != 0 && !esVisitado((x/40)-1,y/40)) {
			caminos++;
		}
		if (laberinto[y/40][(x/40)+1] != 0 && !esVisitado((x/40)+1,y/40)) {
			caminos++;
		}
		if (laberinto[(y/40)+1][x/40] != 0 && !esVisitado(x/40,(y/40)+1)) {
			caminos++;
		}
		if (laberinto[(y/40)-1][x/40] != 0 && !esVisitado(x/40,(y/40)-1)) {
			caminos++;
		}
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
		if (valor == 1) {
			sensores(x,y);
		}
		if (valor == 2) {
			System.out.print("Agua: ");
			System.out.println(x+","+y);
		}
		if (valor == 3) {
			System.out.print("Arena: ");
			System.out.println(x+","+y);
		}
		if (valor == 4) {
			System.out.println("LLegaste a la meta!!");
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
}
