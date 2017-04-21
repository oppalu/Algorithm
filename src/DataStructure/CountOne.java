package DataStructure;

import java.util.Scanner;

/**
 * Created by phoebegl on 2017/4/20.
 * 递归方法返回N的二进制表示中1的个数
 */
public class CountOne {

    public static int count(int n) {
        if(n<2)
            return n;
        return n%2 +count(n/2);
    }

    public static void main(String[] args) {
        System.out.print("Enter the number:");
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        System.out.println(count(num));
    }
}
