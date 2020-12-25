// 387. First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/
import java.util.HashMap;

class Solution {
  public int firstUniqChar(String s) {
    HashMap<Character, Integer> occ = new HashMap<>();
    Character c;
    int x;
    for (int i = 0; i < s.length(); i++) {
      c = s.charAt(i);

      if (occ.containsKey(c)) {
        x = occ.get(c);
        occ.replace(c, x + 1);
      } else {
        occ.put(c, 1);
      }
    }

    for (int i = 0; i < s.length(); i++) {
      c = s.charAt(i);
      if (occ.get(c) == 1) return i;
    }
    return -1;
  }
}

public class Main {
  public static void main(String[] args) {
    String arr1 = "loveleetcode";

    int ret = new Solution().firstUniqChar(arr1);
    System.out.println(ret);
  }
}