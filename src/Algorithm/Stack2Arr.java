package Algorithm;

import java.util.Stack;

/**
 * Created by phoebegl on 2017/5/2.
 * 用两个栈实现队列,完成在队列尾部插入节点和头部删除节点
 * 思想:用两个栈,s2为空则s1的全部一个个弹出压入s2,否则弹出s2的栈顶,压入的话压入到s1
 */
public class Stack2Arr {

    private static Stack<String> s1 = new Stack<>();
    private static Stack<String> s2 = new Stack<>();

    public static void append(String element) {
        s1.push(element);
    }

    public static String delete() {
        if(s2.isEmpty()) {
            while(!s1.isEmpty()) {
                String temp = s1.pop();
                s2.push(temp);
            }
        }

        if(s2.isEmpty()) {
            System.out.println("队列中没有元素");
            return null;
        }

        return s2.pop();
    }

    public static void main(String[] args) {
        Stack2Arr.append("a");
        Stack2Arr.append("b");
        Stack2Arr.append("c");
        Stack2Arr.append("d");
        Stack2Arr.append("e");
        Stack2Arr.append("f");

        String temp = Stack2Arr.delete();
        while(temp != null) {
            System.out.println(temp);
            temp = Stack2Arr.delete();
        }
    }
}
