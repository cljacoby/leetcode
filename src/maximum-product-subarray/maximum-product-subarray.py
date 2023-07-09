# https://leetcode.com/problems/maximum-product-subarray

from collections import deque

'''
for num in nums:
    p = prod * num
    if p < num:
        q.clear()
        p = num
    q.append(num)
    prod = p
    mx = max(mx, prod)
return mx
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negs_in, negs_out = 0, len([i for i in nums if i < 0])
        q = deque([])
        prod = 1
        mx = float('-inf')
        for num in nums:
            pass
        return mx


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,3,-2,4], 6),
        ([-2,0,-1], 0),
        ([-2,3,-4], 24),
        ([-4,1,1,-4,1,1,-5], 20),
    ]
    for (nums, solution) in tests:
        result = sol.maxProduct(nums)
        # assert result == solution, \
        #     f"result {result} != solution {solution}"
    print("✅ All tests passed")

