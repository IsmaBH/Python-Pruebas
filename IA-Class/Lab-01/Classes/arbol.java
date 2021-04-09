//Clase para implementar el arbol
import java.util.Vector;

public class arbol{
	Nodo raiz;
	public Nodo insertarRaiz(String dato,int x,int y){
		raiz = new Nodo(dato,x,y);
		return raiz;
	}
	public void verHijos(Nodo nodo){
		//Se inicia con los padres
		for(int i = 0;i<nodo.nohijos;i++){
			nodo.hijos[i].verNodo();
			//Se hace lo mismo con los hijos
			verHijos(nodo.hijos[i]);
		}
	}
	public void Insertar(Nodo nodo,String dato,int x,int y,String padre){
		Nodo nuevo = new Nodo(dato,x,y);
		//Si el padre es la raiz
		if(nodo.getId().equals(padre)){
			nodo.aumentarHijos(nuevo);
		}else{
			//Si el padre es uno de los hijos
			for(int i = 0;i<nodo.nohijos;i++){
				if(nodo.hijos[i].getId().equals(padre)){
					//Se coloca el hijo en el nodo
					nodo.hijos[i].aumentarHijos(nuevo);
				}else{
					//Busca el padre en los hijos del nodo
					Insertar(nodo.hijos[i],dato,x,y,padre);
				}
			}
		}
	}
	public boolean buscarAnchura(Nodo nodo,int x,int y){
		char resultado = new char[2];
		for (int i = 0;i<nodo.nohijos;i++) {
			if (nodo.hijos[i].getX() == x && nodo.hijos[i].getY() == y) {
				resultado[0] = "1";
				resultado[1] = nodo.getId();
			}else{
				buscarAnchura(nodo.hijos[i],x,y);
			}
		}
		return resultado;
	}
}

class Nodo{
	String id;
	int coordX = 0;
	int coordY = 0;
	int nohijos;
	Nodo hijos[];
	Nodo hijosT[];

	public Nodo(String id,int x,int y){
		this.id = id;
		this.coordX = x;
		this.coordY = y;
		this.nohijos = 0;
	}
	public void copiarHijos(){
		//Aumenta en 1 los hijos con un arreglo temporal
		this.hijosT = new Nodo[nohijos+1];
		for(int i = 0;i<this.nohijos;i++){
			hijosT[i] = hijos[i];
		}
	}
	public void aumentarHijos(Nodo nodo){
		copiarHijos();
		this.hijosT[this.nohijos] = nodo;
		this.hijos = hijosT;
		this.nohijos++;
	}
	public String getId(){
		return this.id;
	}
	public void setId(String dato){
		this.id = dato;
	}
	public int getX(){
		return this.coordX;
	}
	public void setX(int dato){
		this.coordX = dato;
	}
	public int getY(){
		return this.coordY;
	}
	public void setY(int dato){
		this.coordY = dato;
	}
	public void verNodo(){
		System.out.println("{"+id+"}");
	}
}