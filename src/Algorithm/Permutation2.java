package Algorithm;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Created by phoebegl on 2017/4/17.
 * 排列组合的递归算法
 * 找出从自然数 1, 2, ..., n 中任取r个数的所有组合, 编一个递归算法.
 */
public class Permutation2 {

    private static ArrayList<Integer> numbers;
    private static int count=-1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter total number n:");
        int n = scanner.nextInt();
        System.out.print("Enter r:");
        int r = scanner.nextInt();
        init(n);
        List<Integer> iL = new ArrayList<>();
        perm("",iL ,  r);
    }

    private static void init(int n) {
        numbers = new ArrayList<>();
        for(int i=0;i<n;i++)
            numbers.add(i+1);
    }

    public static void perm(String s, List<Integer> iL, int r) {
        if(r == 0) {
            System.out.println(s);
            return;
        }
        List<Integer> iL2;
        for(int i = 0; i < numbers.size(); i++) {
            iL2 = new ArrayList<>();
            iL2.addAll(iL);
            if(!iL.contains(i)) {
                String str = s + numbers.get(i);
                iL2.add(i);
                perm(str, iL2, r-1);
            }
        }
    }

}
