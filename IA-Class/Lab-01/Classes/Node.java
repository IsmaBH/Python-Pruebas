public class Node {
    private Integer value;
    private Node nextElement;
    private Node previousElement;
 
    public Node(Integer value) {
        this.value = value;
    }
 
    public Integer getValue() {
        return value;
    }
 
    public void setValue(Integer value) {
        this.value = value;
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