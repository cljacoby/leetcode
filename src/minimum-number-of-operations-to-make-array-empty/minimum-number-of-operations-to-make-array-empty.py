# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty

'''
This felt like sort of a 'gotcha' question, or maybe the math just
didn't stick out to me.

I first tried to do this with iterative+bfs, and recursive+dfs. However,
these got either Time/Memory limit exceeded, so I had to reference the
solutions.

The trick is to recognize that the number of operations to compose
any given count (except 1) from 2 and 3 will be equal to the floor
division of the count by 3, plus 1 if there is any remainder. Or
basically for each num:

    ops += count // 3
    if counts % 3 > 0:
        ops += 1
'''

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        ops = 0
        for count in freq.values():
            if count == 1:
                return -1
            ops += count // 3
            if count % 3 > 0:
                ops += 1
        return ops


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 3, 3, 2, 2, 4, 2, 3, 4], 4),
        ([2, 1, 2, 2, 3, 3], -1),
    ]
    for (nums, solution) in tests:
        result = sol.minOperations(nums)
        assert result == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")
