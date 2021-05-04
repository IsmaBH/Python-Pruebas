/*
** Clase que implenta la union de las
** Clases Laberinto y Personaje
*/

import java.awt.Graphics;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.Scanner;

public class Juego extends JPanel{
	//Atributos de la clase
	Laberinto laberinto = new Laberinto();
	Personaje personaje = new Personaje();
	//Constructor de la clase
	public Juego(){
		personaje.ejecutaAlgoritmo();
	}
	//Metodos de la clase
	@Override
	public void paint(Graphics grafico){
		//Empieza el metodo que nos permitira dibujar el laberinto
		laberinto.paint(grafico,personaje);
		personaje.paint(grafico);
	}
	public void setPersonaje(String opcion){
		personaje.setRaza(opcion);
	}
	public void sAlgoritmo(String opcion){
		personaje.setAlgoritmo(opcion);
	}
	public static void main(String[] args){
		//Variables para guardar las opciones de jugador
		String personajeSeleccionado;
		String algoritmoSeleccionado;
		//Modo de obtencion de los datos por consola
		System.out.println("Personajes disponibles: 1.- Humano, 2.- Mono, 3.- Pulpo");
		Scanner opcion = new Scanner(System.in);
		personajeSeleccionado = opcion.nextLine();
		System.out.println("Algoritmos disponibles: 1.- Anchura, 2.- Profundidad, 3.- A*");
		Scanner opAl = new Scanner(System.in);
		algoritmoSeleccionado = opAl.nextLine();
		//Creacion de la ventana de juego
		JFrame miventana = new JFrame("Mi laberinto");
		Juego game = new Juego();
		game.setPersonaje(personajeSeleccionado);
		game.sAlgoritmo(algoritmoSeleccionado);
		miventana.add(game);
		miventana.setSize(920,720);
		miventana.setLocation(300,200);
		miventana.setVisible(true);
		miventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		//Bucle de juego para actualizar la pantalla
		while(true){
			try{
				Thread.sleep(10);
				miventana.repaint();
			}catch(InterruptedException ex){
				System.out.println("Ocurrio un error");
			}
		}
	}
}
