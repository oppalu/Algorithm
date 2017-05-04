package Algorithm;

/**
 * Created by phoebegl on 2017/5/4.
 * 求n个筛子点数和s的所有可能的值出现的概率
 * 每次多一个筛子,和为n的应为上一次循环n-1~n-6此时的总和
 */
public class Probability {

    public static void getP(int n) {
        if(n<1)
            return;
        int[][] probability = new int[2][6*n+1];

        for(int i=0;i<6*n+1;i++) {
            probability[0][i] = 0;
            probability[1][i] = 0;
        }

        int flag = 0;   //前后两次计算分别在0和1之间切换进行,flag标记当前的结果存在哪个里
        //初始化第一次均为1
        for(int i=1;i<=6;i++)
            probability[flag][i]=1;

        for(int j=2;j<=n;j++) {
            for(int i=0;i<j;i++)
                probability[1-flag][i]=0;   //n次和的最小值为n
            for(int i=j;i<=6*n;i++) {
                probability[1-flag][i]=0;   //先初始化
                for (int k=1;k<=i && k<=6;k++)
                    probability[1-flag][i]+=probability[flag][i-k];
            }
            flag = 1-flag;
        }

        double total = Math.pow(6,n);
        for(int i=n;i<=6*n;i++) {
            System.out.println(i+" : "+probability[flag][i]/total);
        }
    }

    public static void main(String[] args) {
        getP(2);
    }
}
