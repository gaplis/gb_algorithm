package Lections.Lection_3;

public class task_2 {
    Node head;
    Node tail;

    public void push(int value){
        Node node = new Node();
        node.value = value;
        node.next = head;
        head.previous = node;
        head = node;
    }

    public Integer peek(){
        Integer result = null;
        if (tail != null) {
            result = tail.value;
            tail.previous.next = null;
            tail = tail.previous;
        }

        return result;
    }

    public Integer pop(){
        Integer result = null;
        if (head != null) {
            result = head.value;
            head = head.next;
        }

        return result;
        
    }

    public void revert(){
        if (head != null && head.next != null){
            Node temp = head;
            revert(head.next, head);
            temp.next = null;
        }
    }

    private void revert(Node currentNode, Node previouNode){
        if (currentNode.next == null) {
            head = currentNode;
        } else {
            revert(currentNode.next, currentNode);
        }
        currentNode.next = previouNode;
    }

    public class Node{
        int value;
        Node next;

        Node previous;
    }
}
