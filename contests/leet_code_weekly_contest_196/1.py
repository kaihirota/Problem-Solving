class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = []
        for i in range(1, len(arr)):
            diff += abs(arr[i] - arr[i-1]),
        if len(set(diff)) == 1:
            return True
        else:
            return False
