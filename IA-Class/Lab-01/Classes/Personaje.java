/*
** CLase donde se implementa al jugador
** con sus caracteristicas
*/

import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Personaje extends JPanel{
	//Atributos de la clase
	Laberinto lab = new Laberinto();
	private int x = 40;
	private int y = 40;
	private final int ancho = 40;
	private final int alto = 40;
	private final int movimiento = 40;
	Node e = new Node(1,1);
	listaDoble visitados = new listaDoble(e);
	ArbolNario ObjArbol = new ArbolNario();
	Nodo raiz = ObjArbol.insertarRaiz("0",x/40,y/40);
	//Metodos de la clase
	@Override
	public void paint(Graphics grafico){
		grafico.setColor(Color.red);
		grafico.fillOval(x,y,ancho,alto);
		grafico.setColor(Color.black);
		grafico.drawOval(x,y,ancho,alto);
	}
	public void teclaPresionada(KeyEvent evento){
		int laberinto[][] = lab.obtieneLaberinto();
		//Tecla izquierda
		if(evento.getKeyCode() == 37){
			if(laberinto[y/40][(x/40)-1] != 0){
				x = x - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!visitados.find(x/40,y/40)) {
					visitados.addLast((x/40),(y/40));
				}
			}
		}
		//Tecla derecha
		if(evento.getKeyCode() == 39){
			if(laberinto[y/40][(x/40)+1] != 0){
				x = x + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!visitados.find(x/40,y/40)) {
					visitados.addLast((x/40),(y/40));
				}
			}
		}
		//Tecla abajo
		if(evento.getKeyCode() == 40){
			if(laberinto[(y/40)+1][x/40] != 0){
				y = y + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!visitados.find(x/40,y/40)) {
					visitados.addLast((x/40),(y/40));
				}
			}
		}
		//Tecla arriba
		if(evento.getKeyCode() == 38){
			if(laberinto[(y/40)-1][x/40] != 0){
				y = y - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
				if (!visitados.find(x/40,y/40)) {
					visitados.addLast((x/40),(y/40));
				}
			}
		}
	}
	//Metodo Auxiliar para la verificacion de las casillas(sensores)
	public void sensores(int x,int y){
		int laberinto[][] = lab.obtieneLaberinto();
		int caminos = 0;
		if (laberinto[y/40][(x/40)-1] != 0 && !visitados.find((x/40)-1,y/40)) {
			caminos++;
		}
		if (laberinto[y/40][(x/40)+1] != 0 && !visitados.find((x/40)+1,y/40)) {
			caminos++;
		}
		if (laberinto[(y/40)+1][x/40] != 0 && !visitados.find(x/40,(y/40)+1)) {
			caminos++;
		}
		if (laberinto[(y/40)-1][x/40] != 0 && !visitados.find(x/40,(y/40)-1)) {
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
}
