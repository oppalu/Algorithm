package DataStructure.Sort.InsertSort;

/**
 * Created by phoebegl on 2017/5/1.
 * 直接插入排序(稳定)
 * 分析:
 * ①最好的情况是n个对象已有序,此时比较总次数为n-1【O(n)】,移动次数为2*(n-1)【O(n)】
 * ②最坏的情况是n个对象逆序,比较为n(n-1)/2【O(n^2)】,移动为2*(n-1)+(1+2+...+n-1)【O(n^2)】
 * ③一般情况下比较为O(n^2),移动为O(n^2)
 */
public class InsertSort {

    public static void sort(int[] list) {
        int i;
        for(int j = 1;j<list.length;j++) {
            int tmp = list[j];
            for(i = j;i>0&&tmp<list[i-1];i--)
                list[i] = list[i-1];
            list[i] = tmp;
        }
    }
}
