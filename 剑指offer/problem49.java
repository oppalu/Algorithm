// 将一个字符串转换成一个整数 
// 数值为0或者字符串不是一个合法的数值则返回0。
// 考虑带+-号，非法输入，输入为NULL,输入为“”,边界值测试


public class problem49 {
    public int StrToInt(String str) {

        if(str == null || str.length() == 0) {
            return 0;
        }

        int digit = 0;
        int symbol = 1;
        int start = 0;

        if(str.charAt(0) == '+') {
            start = 1;
        } 
        if(str.charAt(0) == '-') {
            symbol = -1;
            start = 1;
        }

        int result = 0;
        for(int i=str.length()-1; i>=start; i--) {
            if(str.charAt(i) >= '9' || str.charAt(i) <= '0') {
                return 0;
            }
            int operator = symbol * (str.charAt(i)-'0') * (int)Math.pow(10, digit);

            if((symbol == 1 && result>Integer.MAX_VALUE-operator) || (symbol == -1 && result<Integer.MIN_VALUE-operator)) {
                return 0;
            }

            result += operator;
            digit += 1;
        }

        return result;
    }

    public static void main(String[] args) {
        int result = new problem49().StrToInt("-2147483648");
        System.out.println(result);
    }
}