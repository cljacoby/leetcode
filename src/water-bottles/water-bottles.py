# https://leetcode.com/problems/water-bottles

import math

class Solution(object):
    def numWaterBottles(self, bottls, exchange):
        """
        :type bottls: int
        :type exchange: int
        :rtype: int
        """
        full = bottls
        empty = 0
        drank = 0
        while full > 0:
            drank += full
            empty += full
            full = 0
            ex = int(math.floor(empty / exchange))
            full, empty = full + ex, empty - (ex * exchange)
        return drank

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (9, 3, 13),
        (15, 4, 19),
    ]
    for (bottles, exchange, solution) in tests:
        result = sol.numWaterBottles(bottles, exchange)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

