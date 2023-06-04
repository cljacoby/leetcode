# https://leetcode.com/problems/number-of-1-bits

# Slow implementation, but wanted to do the full decimal->binary
# coversion for fun
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        for i in range(32):
            digits.append(n // pow(2, i) % 2)
        digits = reversed(digits)
        count = len([i for i in digits if i == 1])
        return count
        
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (11, 3),
        (128, 1),
        (4294967293, 31),
    ]
    for (num, solution) in tests:
        result = sol.hammingWeight(num)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

