/*
**Clase para el personaje tipo humano
*/
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Humano extends Personaje{
	//Atributos
	String raza;
	//Constructor
	public Humano(){
		super();
		this.raza = "Humano";
	}
	//Metodos
	@Override
	public void paint(Graphics grafico){
		grafico.setColor(Color.red);
		grafico.fillOval(x,y,ancho,alto);
		grafico.setColor(Color.black);
		grafico.drawOval(x,y,ancho,alto);
	}
}