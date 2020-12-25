"""
1344. Angle Between Hands of a Clock
https://leetcode.com/problems/angle-between-hands-of-a-clock/
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # convert to angles
        offset = minutes / 60 * 30
        minutes *= 6
        hour = (30 * hour + offset) % 360
        return min(abs(minutes - hour), 360 - abs(minutes - hour))


Solution().angleClock(hour = 12, minutes = 30) == 180
Solution().angleClock(hour = 3, minutes = 30) == 75
Solution().angleClock(hour = 3, minutes = 15) == 7.5
Solution().angleClock(hour = 4, minutes = 50) == 155
Solution().angleClock(hour = 12, minutes = 0) == 0
Solution().angleClock(hour = 1, minutes = 57) == 76.5
