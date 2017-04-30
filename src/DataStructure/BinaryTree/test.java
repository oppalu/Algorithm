package DataStructure.BinaryTree;

/**
 * Created by phoebegl on 2017/4/30.
 */
public class test {

    public static void main(String[] args) {
        BinaryNode n1 = new BinaryNode("D");
        BinaryNode n2 = new BinaryNode("E");
        BinaryNode n3 = new BinaryNode("F");
        BinaryNode n4 = new BinaryNode("B",n1,n2);
        BinaryNode n5 = new BinaryNode("C",null,n3);
        BinaryNode n6 = new BinaryNode("A",n4,n5);

        BinaryTree tree = new BinaryTree(n6);
        tree.setRoot(tree.createTreeByPreAndIn("ABDCEGFHI","DBAEGCHFI"));
        tree.inOrder(tree.getRoot());
    }
}
