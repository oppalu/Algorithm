package DataStructure.BinaryTree;

import java.util.Stack;

/**
 * Created by phoebegl on 2017/4/30.
 */
public class BinaryTree {

    private BinaryNode root;

    public BinaryTree() {
        this.root = null;
    }

    public BinaryTree(BinaryNode root) {
        this.root = root;
    }

    public boolean isEmpty() {
        return root == null ? true : false;
    }

    public BinaryNode createTreeByPreAndIn(String pre,String in) {
        if(pre.length() != in.length())
            return null;
        return createTree(pre,0,pre.length()-1,in,0,in.length()-1);
    }

    public BinaryNode createTree(String pre,int prestart,int preend,String in,int instart,int inend) {
        if(instart > inend)
            return null;
        BinaryNode r = new BinaryNode(pre.charAt(prestart));
        int position = findPosition(in,instart,inend,pre.charAt(prestart));
        r.setLeftChild(createTree(pre,prestart+1,prestart+position-instart,in,instart,position-1));
        r.setRightChild(createTree(pre,position-inend+preend+1,preend,in,position+1,inend));
        return r;
    }

    private int findPosition(String in,int start,int end,char key) {
        int i;
        for(i = start;i<=end;i++) {
            if(in.charAt(i) == key)
                return i;
        }
        return -1;
    }

    public void preOrderNoRecur(BinaryNode node) {
        Stack<BinaryNode> stack = new Stack<>();
        BinaryNode b = node;
        while(true) {
            while(b != null) {
                System.out.print(b.getElement()+" ");
                stack.push(b);
                b = b.getLeftChild();
            }
            if(!stack.isEmpty()) {
                b = stack.pop();
                b = b.getRightChild();
            } else
                return;
        }
    }

    public void inOrderNoRecur(BinaryNode node) {
        Stack<BinaryNode> stack = new Stack<>();
        BinaryNode b = node;
        while(true) {
            while(b != null) {
                stack.push(b);
                b = b.getLeftChild();
            }
            if(!stack.isEmpty()) {
                b = stack.pop();
                System.out.print(b.getElement()+" ");
                b = b.getRightChild();
            } else
                return;
        }
    }

    public void postOrderNoRecur(BinaryNode node) {
        Stack<BinaryNode> stack = new Stack<>();
        BinaryNode b = node;
        while(node != null) {

            for(;node.getLeftChild()!=null;node=node.getLeftChild()){
                stack.push(node);
            }

            while(node!=null && (node.getRightChild()==null || node.getRightChild()==b)) {
                System.out.print(node.getElement()+" ");
                b = node;
                if(stack.empty())
                    return;
                node = stack.pop();
            }
            stack.push(node);
            node = node.getRightChild();
        }
    }

    public void preOrder(BinaryNode node) {
        if(node == null)
            return;
        System.out.print(node.getElement()+" ");
        preOrder(node.getLeftChild());
        preOrder(node.getRightChild());
    }

    public void inOrder(BinaryNode node) {
        if(node == null)
            return;
        inOrder(node.getLeftChild());
        System.out.print(node.getElement()+" ");
        inOrder(node.getRightChild());
    }

    public void postOrder(BinaryNode node) {
        if(node == null)
            return;
        System.out.print(node.getElement()+" ");
        postOrder(node.getLeftChild());
        postOrder(node.getRightChild());
    }

    public BinaryNode getRoot() {
        return root;
    }

    public void setRoot(BinaryNode root) {
        this.root = root;
    }
}
