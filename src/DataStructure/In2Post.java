package DataStructure;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * Created by phoebegl on 2017/4/29.
 * 中缀表达式转后缀
 */
public class In2Post {

    private static Stack<Character> stack = new Stack<>();

    public static int getPriority(char operator) {
        if(operator == '+' || operator == '-')
            return 2;
        else if(operator == '*' || operator == '/' || operator == '%')
            return 3;
        else if(operator == '(')
            return 1;
        else if (operator == '#')
            return 0;
        return -1;
    }

    public static boolean compare(char opt1,char opt2) {
        return getPriority(opt1) > getPriority(opt2) ? true : false;
    }

    /**
     * 转为后缀表达式:
     * 1、如果是"("直接压入stack栈。
     * 2、如果是")"，依次从stack栈弹出运算符加到数组newExpressionStrs的末尾，知道遇到"("；
     * 3、如果是非括号，比较扫描到的运算符，和stack栈顶的运算符。如果扫描到的运算符优先级高于栈顶运算符则，把运算符压入栈。
     * 否则的话，就依次把栈中运算符弹出加到数组newExpressionStrs的末尾，直到遇到优先级低于扫描到的运算符或栈空，并且把扫描到的运算符压入栈中。就这样依次扫描，知道结束为止。如果扫描结束，栈中还有元素，则依次弹出加到数组newExpressionStrs的末尾，就得到了后缀表达式。
     */
    public static void transfer(String s) {
        stack.push('#');
        for(int i=0;i<s.length();i++) {
            char temp = s.charAt(i);
            if((temp>='a'&&temp<='z') || (temp>='A'&&temp<='Z') || (temp>='0'&&temp<='9')) {
                System.out.print(temp);
            } else if(temp == '('){
                stack.push(temp);
            } else if(temp == ')') {
                while(!stack.isEmpty()) {
                    char c = stack.peek();
                    if(c != '(') {
                        System.out.print(stack.pop());
                    } else {
                        stack.pop();
                        break;
                    }
                }
            } else {
                char c = stack.peek();
                if(compare(temp,c))
                    stack.push(temp);
                else {
                    while(!stack.isEmpty()) {
                        char tmp = stack.peek();
                        if(!compare(temp,tmp))
                            System.out.print(stack.pop());
                        else {
                            stack.pop();
                            break;
                        }
                    }
                }
            }
        }
        while(!stack.isEmpty()) {
            System.out.print(stack.pop());
        }
        System.out.println();
    }

    public static void main(String[] args) {
        transfer("3+(6-4/2)*5");
    }
}
