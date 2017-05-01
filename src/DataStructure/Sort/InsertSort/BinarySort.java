package DataStructure.Sort.InsertSort;

/**
 * Created by phoebegl on 2017/5/1.
 * 二分法插入排序:稳定
 * O(n*log2n)
 */
public class BinarySort {

    public static void sort(int[] list,int left,int right) {
        int low,middle,high;
        int temp;
        for(int i = left+1;i<right;i++) {
            temp = list[i];
            low = left;
            high = i-1;
            while(low <= high) {
                middle = (low + high) / 2;
                if (list[i] < list[middle])
                    high = middle - 1;
                else
                    low = middle + 1;
            }

            for (int j = i-1;j>=low;j--)
                list[j+1] = list[j];
            list[low] = temp;
        }
    }
}
