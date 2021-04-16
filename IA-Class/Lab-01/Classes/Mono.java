/*
**Clase que implementa al personaje mono
*/
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Mono extends Personaje{
	//Atributos
	String raza;
	//Constructor
	public Mono(){
		super();
		this.raza = "Mono";
	}
	//Metodos
	@Override
	public void paint(Graphics grafico){
		grafico.setColor(Color.cyan);
		grafico.fillOval(x,y,ancho,alto);
		grafico.setColor(Color.black);
		grafico.drawOval(x,y,ancho,alto);
	}
}