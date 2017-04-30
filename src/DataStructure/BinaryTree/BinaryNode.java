package DataStructure.BinaryTree;

/**
 * Created by phoebegl on 2017/4/30.
 */
public class BinaryNode {

    private BinaryNode leftChild;
    private BinaryNode rightChild;
    private Object element;

    public BinaryNode() {
        this.leftChild = null;
        this.rightChild = null;
    }

    public BinaryNode(Object ele) {
        this.element = ele;
    }

    public BinaryNode(Object ele,BinaryNode l,BinaryNode r) {
        this.element = ele;
        this.leftChild = l;
        this.rightChild = r;
    }

    public BinaryNode getLeftChild() {
        return leftChild;
    }

    public void setLeftChild(BinaryNode leftChild) {
        this.leftChild = leftChild;
    }

    public BinaryNode getRightChild() {
        return rightChild;
    }

    public void setRightChild(BinaryNode rightChild) {
        this.rightChild = rightChild;
    }

    public Object getElement() {
        return element;
    }

    public void setElement(Object element) {
        this.element = element;
    }
}
