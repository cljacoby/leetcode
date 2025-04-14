# https://leetcode.com/problems/count-symmetric-integers

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        out = 0
        for x in range(low, high + 1):
            digits = [int(c) for c in str(x)]
            size = len(digits)
            if size % 2 != 0:
                continue
            mid = size // 2
            a = sum(digits[:mid])
            b = sum(digits[mid:])
            if a == b:
                out += 1
        return out

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (1, 100, len([11, 22, 33, 44, 55, 66, 77, 88, 99])),
        (1200, 1230, len([1203, 1212, 1221, 1230])),
    ]
    for (low, high, solution) in tests:
        result = sol.countSymmetricIntegers(low, high)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

