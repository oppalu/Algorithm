package Algorithm;

/**
 * Created by phoebegl on 2017/4/27.
 * 二维数组每行每列从左到右从上到下递增,输入一个二维数组和整数判断是否含有
 */
public class matrix {

    public static void main(String[] args) {
        int[][] matrix = {{1,2,8,9},{2,4,9,12},{4,7,10,13},{6,8,11,15}};
        System.out.println(find(matrix,matrix.length,matrix[0].length,17));
    }

    //思路:从右上角开始,如果大则删掉对应的列,如果小删掉所在的行
    static boolean find(int[][] matrix,int row,int column,int number) {
        if(matrix != null && row > 0 && column > 0 ) {
            int r = 0;
            int c = column -1;
            while (r<row && c >= 0) {
                int temp = matrix[r][c];
                System.out.println(matrix[r][c]);
                if(temp == number) {
                    return true;
                } else if (temp < number) {
                    r++;
                } else {
                    c--;
                }
            }
        }
        return false;
    }
}
