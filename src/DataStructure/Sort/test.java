package DataStructure.Sort;

import DataStructure.Sort.ExchangeSort.BubbleSort;
import DataStructure.Sort.ExchangeSort.QuickSort;
import DataStructure.Sort.InsertSort.BinarySort;

/**
 * Created by phoebegl on 2017/5/1.
 */
public class test {

    public static void main(String[] args) {
        int[] a = {3,1,6,8,2,9,5,7,4};

        QuickSort.sort(a,0,a.length-1);

        for(int i = 0;i<a.length;i++)
            System.out.print(a[i]+" ");
    }
}

