/*
** Clase que implenta la union de las
** Clases Laberinto y Personaje
*/

import java.awt.Graphics;
import java.awt.event.KeyListener;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Juego extends JPanel{
	//Atributos de la clase
	Laberinto laberinto = new Laberinto();
	Personaje personaje = new Personaje();
	//Constructor de la clase
	public Juego(){
		addKeyListener(new KeyListener(){
			@Override
			public void keyTyped(KeyEvent e){}
			@Override
			public void keyPressed(KeyEvent e){
				personaje.teclaPresionada(e);
			}
			@Override
			public void keyReleased(KeyEvent e){}
		});
		setFocusable(true);
	}
	//Metodos de la clase
	@Override
	public void paint(Graphics grafico){
		//Empieza el metodo que nos permitira dibujar el laberinto
		laberinto.paint(grafico);
		personaje.paint(grafico);
	}
	public static void main(String[] args){
		JFrame miventana = new JFrame("Mi laberinto");
		Juego game = new Juego();
		miventana.add(game);
		miventana.setSize(920,540);
		miventana.setLocation(300,200);
		miventana.setVisible(true);
		miventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		while(true){
			try{
				Thread.sleep(10);
			}catch(InterruptedException ex){
				System.out.println("Ocurrio un error");
			}
			game.repaint();
		}
	}
}
