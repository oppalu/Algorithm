package Algorithm;

import DataStructure.MyLinkedList.MyList;

import java.util.Stack;

/**
 * Created by phoebegl on 2017/5/3.
 * 实现具有min函数(找栈中最小元素的值)的栈
 * 思路:引入一个辅助栈,每次压入当前栈中的最小值(如栈中先后压入3、4,则辅助栈中为3、3)
 */
public class MinStack {

    private static Stack<Integer> data = new Stack<>();
    private static Stack<Integer> help = new Stack<>();

    public static void push(int value) {
        data.push(value);
        if(help.isEmpty())
            help.push(value);
        else {
            if(help.peek() >= value)
                help.push(value);
            else
                help.push(help.peek());
        }
    }

    public static int pop() {
        if(data.isEmpty() || help.isEmpty()) {
            System.out.println("栈中没有数据");
            return -1;
        }
        help.pop();
        return data.pop();
    }

    public static int getMin() {
        if(data.isEmpty() || help.isEmpty()) {
            System.out.println("栈中没有数据");
            return -1;
        }
        return help.peek();
    }

    public static void main(String[] args) {
        push(3);
        push(4);
        System.out.println(getMin());
        push(2);
        pop();
        System.out.println(getMin());
        push(0);
        System.out.println(getMin());
    }
}
