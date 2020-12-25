// 953. Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        int n = words.length;
        for (int i=0; i < n-1; i++) {
            String word1 = words[i];
            String word2 = words[i+1];
            int word1Length = word1.length(); 
            int word2Length = word2.length();
            int wordLength = Math.min(word1Length, word2Length);
            int j = 0;
            while (j < wordLength) {
                int idx1 = order.indexOf(word1.charAt(j));
                int idx2 = order.indexOf(word2.charAt(j));
                if (idx1 == idx2) j++;
                else if (idx1 < idx2) break;
                else if (idx1 > idx2) return false;
            }
            if ((j == wordLength) && (word1Length <= word2Length)) continue;
            else if ((j == wordLength) && (word1Length > word2Length)) return false;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        String[] words = {"apple", "app"};
        assert new Solution().isAlienSorted(words, "abcdefghijklmnopqrstuvwxyz") == false;
    }
}