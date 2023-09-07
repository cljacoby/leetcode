# https://leetcode.com/problems/plus-one

from collections import deque

# More 'data-structurey' solution. Use a bonafide stack, and push
# and pop operations from the stack.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = deque(digits)
        ln = len(digits)
        stack = [ln - 1]
        while len(stack) > 0:
            idx = stack.pop()
            if idx == -1:
                digits.appendleft(1)
                break
            res = digits[idx] + 1
            if res == 10:
                digits[idx] = 0
                stack.append(idx - 1)
            else:
                digits[idx] = res
        return digits 

# Faster, less-memory use solution.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1
        while True:
            if idx == -1:
                digits.insert(0, 1)
                return digits
            res = digits[idx] + 1 
            if res < 10:
                digits[idx] = res
                return digits
            digits[idx] = 0
            idx -= 1

# Just code golf at this point 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1
        while True:
            if idx == -1:
                digits.insert(0, 1)
                return digits
            digits[idx] = (digits[idx] + 1) % 10
            if digits[idx] != 0:
                return digits
            idx -= 1

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3],
            [1,2,4]
        ),
        (
            [4,3,2,1],
            [4,3,2,2]
        ),
        (
            [9],
            [1,0]
        ),
    ]
    for (digits, solution) in tests:
        result = sol.plusOne(digits)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

