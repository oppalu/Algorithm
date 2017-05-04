package Algorithm;

/**
 * Created by phoebegl on 2017/5/3.
 * 计算从1到n的整数中1出现的次数
 * 思路:每次去掉最高位做递归
 */
public class Count1 {

    public static int count(int n) {
        if(n <= 0)
            return 0;
        return countNumber(String.valueOf(n));
    }

    public static int countNumber(String num) {
        if(num == null || num.equals(""))
            return 0;
        int first = num.charAt(0)-'0';
        if(num.length()==1 && first==0)
            return 0;
        if(num.length()==1 && first>0)
            return 1;

        int numFirstDigit = 0;
        //如21345中第一位出现1的次数是10000(10^4)次,而11345则为1346次
        if(first>1)
            numFirstDigit=powerBase10(num.length()-1);
        else if(first==1)
            numFirstDigit=Integer.parseInt(num.substring(1))+1;

        //numOtherDigits是除了第一位之外出现1的个数,思路是每一位选定为1剩下的均可从0~9十个数字中选一个,排列组合
        //如1346~21345,有两段1346~11345与11346~21345,每段的每一位都有10^3个,所以为2(第一位)*4(后面4位)*10^3(排列组合情况)
        int numOtherDigits = first*(num.length()-1)*powerBase10(num.length()-2);
        //去掉高位做递归,如21345就是先算1346~21345的,然后递归算1~1345的
        int numRecursive=countNumber(num.substring(1));
        return numFirstDigit+numOtherDigits+numRecursive;
    }

    public static int powerBase10(int n) {
        int result = 1;
        for(int i=0;i<n;i++)
            result *= 10;
        return result;
    }

    public static void main(String[] args) {
        System.out.print(count(19));
    }
}
