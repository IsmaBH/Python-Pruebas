//Clase para implementar el arbol
class arbol{
	Nodo raiz;
	public Nodo insertarRaiz(String dato){
		raiz = new Nodo(dato);
		return raiz;
	}
	public void verHijosRecursivo(Nodo nodo){
		//Se inicia con los padres
		for(int i = 0;i<nodo.nohijos;i++){
			nodo.hijos[i].verNodo();
			//Se hace lo mismo con los hijos
			verHijosRecursivo(nodo.hijos[i]);
		}
	}
	public void InsertarRecursivo(Nodo nodo,String dato,String padre){
		Nodo nuevo = new Nodo(dato);
		//Si el padre es la raiz
		if(nodo.getDato().equals(padre)){
			nodo.aumentarHijo(nuevo);
		}else{
			//Si el padre es uno de los hijos
			for(int i = 0;i<nodo.nohijos;i++){
				if(nodo.hijos[i].getDato().equals(padre)){
					//Se coloca el hijo en el nodo
					nodo.hijos[i].aumentarHijo(nuevo);
				}else{
					//Busca el padre en los hijos del nodo
					InsertarRecursivo(nodo.hijos[i],dato,padre);
				}
			}
		}
	}
}
