# https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        digits.pop()
        digits = self.plusOne(digits)
        digits.append(0)
        return digits

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
    ]
    for (digits, solution) in tests:
        result = sol.plusOne(digits)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

