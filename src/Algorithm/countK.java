package Algorithm;

import DataStructure.MyLinkedList.MyList;
import DataStructure.MyLinkedList.Node;

/**
 * Created by phoebegl on 2017/4/21.
 * 查找链表中倒数第k个位置上的结点.
 * 若查找成功,输出该结点的data域的值, 并返回1; 否则返回0.
 */
public class countK {

    public static void main(String[] args) {
        MyList list = new MyList();
        list.insert(new Node(1));
        list.insert(new Node(2));
        list.insert(new Node(4));
        list.insert(new Node(3));
        list.insert(new Node(8));
        list.insert(new Node(10));
        list.insert(new Node(7));
        find(list,6);
    }

    public static void find(MyList list, int k) {
        if(k > list.getSize()) {
            System.out.println("k大于列表长度!");
            return;
        }

        Node temp = list.getHead();
        Node result = temp;
        for(int i=0;i<k;i++) {
            temp = temp.getNext();
        }
        while(temp != null) {
            temp = temp.getNext();
            result = result.getNext();
        }
        System.out.println("倒数第"+k+"个节点值为:"+result.getValue());
    }
}

