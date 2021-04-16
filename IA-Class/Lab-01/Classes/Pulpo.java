import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Pulpo extends Personaje{
	//Atributos
	String raza;
	//Constructor
	public Pulpo(){
		super();
		this.raza = "Pulpo";
	}
	//Metodos
	@Override
	public void paint(Graphics grafico){
		grafico.setColor(Color.magenta);
		grafico.fillOval(x,y,ancho,alto);
		grafico.setColor(Color.black);
		grafico.drawOval(x,y,ancho,alto);
	}
}