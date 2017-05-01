package DataStructure.Sort.ExchangeSort;

/**
 * Created by phoebegl on 2017/5/1.
 * 冒泡排序:稳定
 * 分析:最好的是有序比较n-1次移动0次,最差的比较n(n-1)/2次,移动3n(n-1)/2次,即O(n^2)
 */
public class BubbleSort {

    public static void sort(int[] list) {
        int temp;
        for(int i=0;i<list.length;i++){
            for(int j=i+1;j<list.length;j++) {
                if(list[i] > list[j]) {
                    temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        }
    }
}
