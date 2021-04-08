import java.util.Vector;

class Nodo{
	String info;
	int nohijos;
	Nodo hijos[];
	Nodo hijosT[];
	public Nodo(String dato){
		info = dato;
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
	public String getDato(){
		return info;
	}
	public void setDato(String dato){
		this.info = dato;
	}
	public void verNodo(){
		System.out.println("{"+info+"}");
	}
}
