package DataStructure.MyLinkedList;

/**
 * Created by phoebegl on 2017/4/27.
 */
public class MyList {

    private Node head;

    public MyList() {
        this.head = null;
    }

    public MyList(Node head) {
        this.head = head;
    }

    public void insert(int value) {
        Node n = new Node(value,null);
        insert(n);
    }

    public void insert(Node newNode) {
        if(head == null)
            head = newNode;
        else {
            Node temp = head;
            while(temp.getNext() != null) {
                temp = temp.getNext();
            }
            temp.setNext(newNode);
        }
    }

    public void remove(int value) {
        if(head == null)
            return;
        Node temp = head;
        if(temp.getValue() == value) {
            this.head = head.getNext();
            return;
        }

        while(temp.getNext() != null) {
            if(temp.getNext().getValue() == value) {
                temp.setNext(temp.getNext().getNext());
                return;
            }
            temp = temp.getNext();
        }
    }

    public void showAll() {
        Node temp = getHead();
        while(temp != null) {
            System.out.println(temp.getValue());
            temp = temp.getNext();
        }
    }

    public int getSize() {
        int result = 0;
        Node temp = getHead();
        while(temp != null) {
            result++;
            temp = temp.getNext();
        }
        return result;
    }

    public boolean isEmpty() {
        return getSize() == 0 ? true : false;
    }

    public int find(int x) {
        Node temp = getHead();
        int index = 0;
        while(temp != null) {
            if(temp.getValue() == x) {
                return index;
            }
            index++;
            temp = temp.getNext();
        }
        return -1;
    }

    public Node findNode(int x) {
        Node temp = getHead();
        while(temp != null) {
            if(temp.getValue() == x) {
                return temp;
            }
            temp = temp.getNext();
        }
        return null;
    }

    public Node getHead() {
        return head;
    }

    public void setHead(Node head) {
        this.head = head;
    }
}
