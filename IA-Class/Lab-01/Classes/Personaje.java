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
	listaDoble visitados = new listaDoble();
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
		visitados.addLast(x,y);
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
		int laberinto[][] = lab.obtieneLaberinto();
		int caminos = 0;
		int counter = 0;
		if (valor == 1) {
			for (int i = -1;i<=1;i=i+2) {
				if (laberinto[(x/40)+i][y/40] != 0 & (!visitados.find((x/40)+i,y/40))) {
					caminos++;
				}else{}
				for (int j = -1;j<=1;j=j+2) {
					counter = counter + 2;
					if(laberinto[x/40][(y/40)+(j+counter)] != 0 & (!visitados.find(x/40,(y/40)+(j+counter)))) {
						caminos++;
					}else{}
					break;
				}
			}
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
