package Algorithm;

import java.util.*;

/**
 * Created by phoebegl on 2017/5/3.
 * 在字符串中找出第一个只出现1次的字符
 * 注意HashMap无序,put会改变顺序。所以用LinkedHashMap
 */
public class OnlyOneTime {

    private static LinkedHashMap<String,Integer> result = new LinkedHashMap<>();
    public static String find(String s) {
        for(int i=0;i<s.length();i++) {
            String temp = s.charAt(i)+"";
            if(result.containsKey(temp))
                result.put(temp,result.get(temp)+1);
            else
                result.put(temp,1);
        }

        for(String key : result.keySet()) {
            if(result.get(key) == 1)
                return key;
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(find("abaccdeff"));
    }
}
