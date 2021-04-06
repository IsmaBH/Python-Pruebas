/*
** Clase que implementa las caracteristicas del laberinto
** Esta clase se expandira en un futuro para agregar diferentes
** Caracteristicas y tipos de areas segun un codigo dado
*/

import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Laberinto extends JPanel{
	//Atributos de la clase
	private int fila = 0;
	private int columna = 0;
	private final int numeroFilas = 10;
	private final int numeroColumnas = 10;
	private final int anchoBloque = 40;
	private final int altoBloque = 40;
	//Metodos de la clase
	@Override
	public void paint(Graphics grafico){
		int [][]laberinto = obtieneLaberinto();
		for(fila = 0;fila<numeroFilas;fila++){
			for(columna = 0;columna<numeroColumnas;columna++){
				//Codigo 0 es una pared/montaña
				if(laberinto[fila][columna] == 0){
					grafico.setColor(Color.gray);
					grafico.fillRect(columna*40,fila*40,anchoBloque,altoBloque);
					grafico.setColor(Color.black);
					grafico.drawRect(columna*40,fila*40,anchoBloque,altoBloque);
				}
				//Codigo 1 es camino
				if (laberinto[fila][columna] == 1) {
					grafico.setColor(Color.white);
					grafico.fillRect(columna*40,fila*40,anchoBloque,altoBloque);
					grafico.setColor(Color.black);
					grafico.drawRect(columna*40,fila*40,anchoBloque,altoBloque);
				}
				//Codigo 2 es agua
				if (laberinto[fila][columna] == 2) {
					grafico.setColor(Color.blue);
					grafico.fillRect(columna*40,fila*40,anchoBloque,altoBloque);
					grafico.setColor(Color.black);
					grafico.drawRect(columna*40,fila*40,anchoBloque,altoBloque);
				}
				//Codigo 3 es arena
				if (laberinto[fila][columna] == 3) {
					grafico.setColor(Color.yellow);
					grafico.fillRect(columna*40,fila*40,anchoBloque,altoBloque);
					grafico.setColor(Color.black);
					grafico.drawRect(columna*40,fila*40,anchoBloque,altoBloque);
				}
				//Codigo 4 es la meta/bosque
				if (laberinto[fila][columna] == 4) {
					grafico.setColor(Color.green);
					grafico.fillRect(columna*40,fila*40,anchoBloque,altoBloque);
					grafico.setColor(Color.black);
					grafico.drawRect(columna*40,fila*40,anchoBloque,altoBloque);
				}
			}
		}
	}
	//Metodo que obtiene el laberinto
	public int[][] obtieneLaberinto(){
		int[][] laberinto = new int[10][10];
		try{
			String ruta = "Mapas/mapa_10_x_10.txt";
			BufferedReader br = new BufferedReader(new FileReader(ruta));
			String linea = br.readLine();
			int contador = 0;
			while(linea != null){
				String[] valores = linea.split(",");
				for (int i = 0;i<valores.length;i++) {
					laberinto[contador][i] = Integer.parseInt(valores[i]);
				}
				contador++;
				linea = br.readLine();
			}
			br.close();
		}catch(FileNotFoundException e){
			System.out.println("No se encuentra el archivo");
			e.printStackTrace();
		}catch(NumberFormatException e){
			System.out.println("No se pudo convertir a entero");
			e.printStackTrace();
		}catch(IOException e){
			System.out.println("Error accediendo al archivo");
			e.printStackTrace();
		}
		return laberinto;
	}
}
