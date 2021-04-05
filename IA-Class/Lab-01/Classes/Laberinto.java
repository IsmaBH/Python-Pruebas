/*
** Clase que implementa las caracteristicas del laberinto
** Esta clase se expandira en un futuro para agregar diferentes
** Caracteristicas y tipos de areas segun un codigo dado
*/

import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Laberinto extends JPanel{
	//Atributos de la clase
	private int fila = 0;
	private int columna = 0;
	private final int numeroFilas = 13;
	private final int numeroColumnas = 23;
	private final int anchoBloque = 40;
	private final int altoBloque = 40;
	//Metodos de la clase
	@Override
	public void paint(Graphics grafico){
		int [][]laberinto = obtieneLaberinto();
		for(fila = 0;fila<numeroFilas;fila++){
			for(columna = 0;columna<numeroColumnas;columna++){
				if(laberinto[fila][columna] == 1){
					grafico.setColor(Color.blue);
					grafico.fillRect(columna*40,fila*40,anchoBloque,altoBloque);
					grafico.setColor(Color.black);
					grafico.drawRect(columna*40,fila*40,anchoBloque,altoBloque);
				}
			}
		}
	}
	public int[][] obtieneLaberinto(){
		int laberinto[][] = 
			{{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
			 {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1},
			 {1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
			 {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
			};
		return laberinto;
	}
}
