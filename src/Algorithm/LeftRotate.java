package Algorithm;

/**
 * Created by phoebegl on 2017/5/4.
 * 字符串左旋(前面的n个字符移到最后)
 * 思路:先分别翻转前后两个部分,在翻转整个字符串
 */
public class LeftRotate {

    public static String reverse(String s) {
        String result="";
        for(int i=s.length()-1;i>=0;i--) {
            result+=s.charAt(i);
        }
        return result;
    }

    public static String leftRotate(String s,int n) {
        String first = s.substring(0,n);
        String second = s.substring(n);
        String temp = reverse(first)+reverse(second);
        return reverse(temp);
    }

    public static void main(String[] args) {
        System.out.print(leftRotate("abcdefg",2));
    }
}
