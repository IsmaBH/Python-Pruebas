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
			}
		}
		//Tecla derecha
		if(evento.getKeyCode() == 39){
			if(laberinto[y/40][(x/40)+1] != 0){
				x = x + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
			}
		}
		//Tecla abajo
		if(evento.getKeyCode() == 40){
			if(laberinto[(y/40)+1][x/40] != 0){
				y = y + movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
			}
		}
		//Tecla arriba
		if(evento.getKeyCode() == 38){
			if(laberinto[(y/40)-1][x/40] != 0){
				y = y - movimiento;
				posicionActual(laberinto[y/40][x/40],x,y);
			}
		}
	}
	public void posicionActual(int valor,int x,int y){
		if (valor == 1) {
			System.out.println("Piso: ");
			System.out.println(x+","+y);
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
