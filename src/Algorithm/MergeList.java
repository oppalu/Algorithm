package Algorithm;

import DataStructure.BinaryTree.BinaryNode;
import DataStructure.BinaryTree.BinaryTree;
import DataStructure.MyLinkedList.MyList;
import DataStructure.MyLinkedList.Node;

/**
 * Created by phoebegl on 2017/5/3.
 * 合并两个排序的链表
 */
public class MergeList {

    public static Node merge(MyList list1,MyList list2) {
        if(list1.isEmpty()) {
            return list2.getHead();
        }
        else if(list2.isEmpty()) {
            return list1.getHead();
        }
        Node result = null;
        if(list1.getHead().getValue() <= list2.getHead().getValue()) {
            result = list1.getHead();
            list1.remove(list1.getHead().getValue());
            result.setNext(merge(list1,list2));
        } else {
            result = list2.getHead();
            list2.remove(list2.getHead().getValue());
            result.setNext(merge(list1,list2));
        }
        return result;
    }

    public static void main(String[] args) {
        MyList l1 = new MyList();
        MyList l2 = new MyList();
        l1.insert(1);
        l1.insert(3);
        l1.insert(5);
        l2.insert(2);
        l2.insert(6);

        MyList list = new MyList();
        list.setHead(merge(l1,l2));
        list.showAll();
    }
}
