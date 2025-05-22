# https://leetcode.com/problems/squares-of-a-sorted-array

from collections import deque

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = deque([])
        neg = deque([])
        out = []
        for num in nums:
            if num < 0:
                neg.append(pow(num, 2))
            else:
                pos.append(pow(num, 2))
        while len(pos) > 0 or len(neg) > 0:
            if len(neg) == 0:
                out.append(pos.popleft())
            elif len(pos) == 0:
                out.append(neg.pop())
            elif neg[-1] < pos[0]:
                out.append(neg.pop())
            else:
                out.append(pos.popleft())
        return out

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-4,-1,0,3,10], [0,1,9,16,100]),
        ([-7,-3,2,3,11], [4,9,9,49,121]),
    ]
    for (nums, solution) in tests:
        result = sol.sortedSquares(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

