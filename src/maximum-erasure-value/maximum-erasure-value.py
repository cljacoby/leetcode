# https://leetcode.com/problems/maximum-erasure-value

from collections import deque

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        window = deque([])
        tot = 0
        mx = float('-inf')
        for num in nums:
            while num in seen:
                out = window.popleft()
                seen.remove(out)
                tot -= out
            seen.add(num)
            window.append(num)
            tot += num
            mx = max(mx, tot)
        return mx

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([4,2,4,5,6], 17),
        ([5,2,1,2,5,2,1,2,5], 8),
    ]
    for (arr, solution) in tests:
        result = sol.maximumUniqueSubarray(arr)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

