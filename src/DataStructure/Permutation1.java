package DataStructure;

import java.util.Scanner;

/**
 * Created by phoebegl on 2017/4/17.
 * public void permute( String str );
 * private void permute( char [ ] str, int low, int high )
 * 第一个是驱动程序,调用第二个显示str中字符的全排列
 */
public class Permutation1 {

    public static void main(String[] args) {
        Permutation1 permutation = new Permutation1();
        System.out.print("Enter the string:");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        permutation.permute(input);
    }

    public void permute(String str) {
        char[] chars = str.toCharArray();
        permute(chars,0,chars.length-1);
    }

    public void permute(char[] list,int low,int high) {
        int i;
        if(low == high) {
            for(i=0;i<=high;i++)
                System.out.print(list[i]);
            System.out.println();
        } else {
            for(i=low;i<=high;i++) {
                swap(list,low,i);
                permute(list,low+1,high);
                swap(list,low,i);
            }
        }
    }

    private void swap(char[] list,int a,int b) {
        char c = list[a];
        list[a]=list[b];
        list[b]=c;
    }
}
