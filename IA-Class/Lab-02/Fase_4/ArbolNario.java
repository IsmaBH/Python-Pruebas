import java.util.ArrayList;

public class ArbolNario{
	Nodo raiz;
	public ArbolNario(){
		this.raiz = null;
	}
	public Nodo obtenerRaiz(){
		return this.raiz;
	}
	public Nodo insertarRaiz(Coordenada posicionInicial){
		raiz = new Nodo(posicionInicial);
		return raiz;
	}
	public void insertarNodo(Nodo nodo,Coordenada pos,Coordenada padre){
		Nodo nuevo = new Nodo(pos);
		//Verificamos si el nodo padre es la raiz
		if (nodo.getCoord().getX() == padre.getX() && nodo.getCoord().getY() == padre.getY()) {
			nodo.aumentarHijo(nuevo);
		}else{
			//Si no buscamos al padre entre los hijos
			for (int i = 0; i < nodo.getNoHijos() ; i++) {
				if (nodo.hijos.get(i).getCoord().getX() == padre.getX() && nodo.hijos.get(i).getCoord().getY() == padre.getY()) {
					nodo.hijos.get(i).aumentarHijo(nuevo);
				}else{
					insertarNodo(nodo.hijos.get(i),pos,padre);
				}
			}
		}
	}
	public void recorrer(Nodo raiz){
		raiz.verInfo();
		for (int i = 0; i < raiz.getNoHijos() ; i++ ) {
			recorrer(raiz.hijos.get(i));
		}
	}
	public void recorrerHijosRaiz(Nodo raiz){
		for (int i = 0; i<raiz.getNoHijos() ; i++ ) {
			recorrerHijosRaiz(raiz.hijos.get(i));
		}
		raiz.verInfo();
	}
	public boolean buscar(Nodo raiz,Coordenada buscar,boolean encontrado){
		if (raiz.getCoord().getX() == buscar.getX() && raiz.getCoord().getY() == buscar.getY()) {
			encontrado = true;
		}
		for (int i = 0; i<raiz.getNoHijos() ; i++) {
			encontrado = buscar(raiz.hijos.get(i),buscar,encontrado);
		}
		return encontrado;
	}
	public int cantidadNodos(Nodo raiz){
		int mayor = 0;
		if (raiz == null) {
			return 0;
		}else{
			for (int i = 0; i<raiz.getNoHijos() ; i++) {
				mayor += cantidadNodos(raiz.hijos.get(i));
			}
			return mayor+1;
		}
	}
	public int altura(Nodo raiz){
		int mayor = 0;
		int tempo = 0;
		if (raiz == null) {
			return 0;
		}else{
			for (int i = 0; i<raiz.getNoHijos() ; i++) {
				tempo = altura(raiz.hijos.get(i));
				if (tempo > mayor) {
					mayor = tempo;
				}
			}
			return mayor+1;
		}
	}
	public int altura2(Nodo raiz){
		int nivel = 0;
		if (raiz == null) {
			return 0;
		}else{
			for (int i = 0; i < raiz.getNoHijos() ; i++) {
				nivel += altura2(raiz.hijos.get(i));
				if (i == 0) {
					nivel ++;
				}
			}
			return nivel;
		}
	}
	public int altura3(Nodo raiz,int nivel){
		if (raiz == null) {
			return 0;
		}else{
			for (int i = 0; i<raiz.getNoHijos() ; i++) {
				nivel = altura3(raiz.hijos.get(i),nivel);
				if (i == 0) {
					nivel++;
				}
			}
			return nivel;
		}
	}
	public int numeroHojas(Nodo raiz){
		int asum = 0;
		if (raiz.getNoHijos() == 0) {
			return 1;
		}else{
			for (int i = 0; i<raiz.getNoHijos() ; i++) {
				asum += numeroHojas(raiz.hijos.get(i));
			}
			return asum;
		}
	}
	public int nivelElemento(Nodo raiz,Coordenada elemento,int nivel){
		int tempo = 0;
		if (raiz == null) {
			return -1;
		}else if (raiz.getCoord().getX() == elemento.getX() && raiz.getCoord().getY() == elemento.getY()) {
			return nivel;
		}else{
			//Se busca en los hijos
			for (int i = 0; i<raiz.getNoHijos() ; i++ ) {
				tempo = nivelElemento(raiz.hijos.get(i),elemento,nivel+1);
				if (tempo != -1) {
					return tempo;
				}
			}
			return -1;
		}
	}
	public void borrarNodo(Nodo raiz,Coordenada borrar, boolean rama){
		//Para poder borrar primero buscamos que exista el nodo que se pretende borrar
		for (int i = 0; i<raiz.getNoHijos() ; i++ ) {
			//En caso de que se quiera borrar con todo y la rama
			if ((raiz.hijos.get(i).getCoord().getX() == borrar.getX() && raiz.hijos.get(i).getCoord().getY() == borrar.getY()) && raiz.hijos.get(i).getNoHijos() != 0 && rama) {
				raiz.hijos.remove(i);
				raiz.actualizarNoHijos();
				break;
			//En caso contrario se verifica que el nodo no tenga hijos
			}else if ((raiz.hijos.get(i).getCoord().getX() == borrar.getX() && raiz.hijos.get(i).getCoord().getY() == borrar.getY())&& raiz.hijos.get(i).getNoHijos() == 0) {
				raiz.hijos.remove(i);
				raiz.actualizarNoHijos();
				break;
			}
			borrarNodo(raiz.hijos.get(i),borrar,rama);
		}
	}
}
class Nodo{
		//Atributos
		Coordenada posicion;
		int cantidadHijos;
		int hijosVisitados;
		String otro;
		ArrayList <Nodo> hijos;
		//Constructores
		public Nodo(Coordenada pos){
			hijos = new ArrayList<Nodo>();
			this.posicion = pos;
			this.cantidadHijos = 0;
		}
		//Metodos
		public void aumentarHijo(Nodo hijo){
			hijos.add(hijo);
			cantidadHijos = hijos.size();
		}
		public void actualizarNoHijos(){
			cantidadHijos = hijos.size();
		}
		public void verInfo(){
			System.out.println("("+posicion.getX()+","+posicion.getY()+")");
		}
		public void verHijos(){
			System.out.println(cantidadHijos);
		}
		public void aumentaVisitados(){
			hijosVisitados = hijosVisitados + 1;
		}
		public void setOtro(String others){
			this.otro = others;
		}
		public String getOtro(){
			return this.otro;
		}
		public void setCoords(Coordenada pos){
			this.posicion = pos;
		}
		public Coordenada getCoord(){
			return this.posicion;
		}
		public int getNoHijos(){
			return cantidadHijos;
		}
		public void restarHijos(){
			this.cantidadHijos--;
		}
		public Nodo retornarNodo(){
			return this;
		}
}