public class listaDoble{
    private Node tail;
    private Node head;
 
    public void addLast(Integer value) {
        Node node = new Node(value);
        if (tail == null && head == null) {
            tail = node;
            head = node;
        } else {
            tail.setNextElement(node);
            node.setPreviousElement(tail);
            tail = node;
        }
    }
 
    public void addFirst(Integer value) {
        Node node = new Node(value);
        if (tail == null && head == null) {
            tail = node;
            head = node;
        } else {
            node.setNextElement(head);
            head.setPreviousElement(node);
            head = node;
        }
    }
 
    public boolean find(int value) {
        boolean c = false;
        for (Node i = head; i != null; i = i.getNextElement()) {
            if (i.getValue() == value) {
                c = true;
                break;
            }else{
                c = false;
            }
        }
        return c;
    }
}