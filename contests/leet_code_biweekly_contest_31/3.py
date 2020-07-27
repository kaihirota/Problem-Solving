from collections import Counter
class Solution:
    # def numSplits(self, s: str) -> int:
        # counter = 0
        # for i in range(1, len(s)):
        #     lset, rset = set(s[:i]), set(s[i:])
        #     if len(lset) == len(rset):
        #         counter += 1
        # return counter
    def numSplits(self, s: str) -> int:
        arr = [0] * len(s)
        letters_seen = set()
        n_letters = 0
        for idx, char in enumerate(s):
            if char not in letters_seen:
                letters_seen.add(char)
                n_letters += 1
            arr[idx] = n_letters

        print(arr, n_letters)
        split_num = n_letters // 2 + 1
        ret = arr.count(split_num)
        if ret == len(s):
            ret -= 1
        print(ret)
        return ret


# assert Solution().numSplits(s="aacaba") == 2
# assert Solution().numSplits(s="abcd") == 1
# assert Solution().numSplits(s="aaaaa") == 4
# assert Solution().numSplits(s="acbadbaada") == 2
Solution().numSplits(s="ababbbbbbb")
