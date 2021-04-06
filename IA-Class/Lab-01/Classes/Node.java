public class Node {
    private int coorX;
    private int coorY;
    private Node nextElement;
    private Node previousElement;
 
    public Node(int x,int y) {
        this.coorX = x;
        this.coorY = y;
    }
 
    public Integer getValueX() {
        return coorX;
    }

    public Integer getValueY() {
        return coorY;
    }

    public void setValueX(Integer value) {
        this.coorX = value;
    }

    public void setValueY(Integer value) {
        this.coorY = value;
    }
 
    public Node getNextElement() {
        return nextElement;
    }
 
    public void setNextElement(Node nextElement) {
        this.nextElement = nextElement;
    }
 
    public Node getPreviousElement() {
        return previousElement;
    }
 
    public void setPreviousElement(Node previousElement) {
        this.previousElement = previousElement;
    }
 
    @Override
    public String toString() {
        return "Node [value=" + value + ", nextElement=" + ((nextElement != null) ? nextElement.getValue()
                : null) + ", previousElement=" +( (previousElement != null) ? previousElement.getValue() : null) + "]";
    }
 
}