public class listaDoble{
    private Node tail;
    private Node head;
 
    public void addLast(Integer x,Integer y) {
        Node node = new Node(x,y);
        if (tail == null && head == null) {
            tail = node;
            head = node;
        } else {
            tail.setNextElement(node);
            node.setPreviousElement(tail);
            tail = node;
        }
    }
 
    public void addFirst(Integer x,Integer y) {
        Node node = new Node(x,y);
        if (tail == null && head == null) {
            tail = node;
            head = node;
        } else {
            node.setNextElement(head);
            head.setPreviousElement(node);
            head = node;
        }
    }
    public boolean find(int x,int y) {
        boolean c = false;
        for (Node i = head; i != null; i = i.getNextElement()) {
            if (i.getValueX() == x && i.getValueY() == y) {
                c = true;
                break;
            }else{
                c = false;
            }
        }
        return c;
    }
    public void print() {
        for (Node i = head; i != null; i = i.getNextElement()) {
            System.out.printf("\t %s ", i.toString());
        }
        System.out.println();
    }
}