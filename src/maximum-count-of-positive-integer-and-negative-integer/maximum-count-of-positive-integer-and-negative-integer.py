# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        partition = self.binary_search(nums, 0, size)
        neg = partition
        while partition < size and nums[partition] == 0:
            partition += 1
        pos = size - partition
        return max(pos, neg)

    def binary_search(self, nums, i, j):
        "partition is first non-negative number"
        if i >= j:
            return i
        mid = (j - i) // 2 + i
        if nums[mid] < 0:
            return self.binary_search(nums, mid + 1, j)
        return self.binary_search(nums, i, mid)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-2,-1,-1,1,2,3], 3),
        ([-3,-2,-1,0,0,1,2], 3),
        ([5,20,66,1314], 4),
        ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0)
    ]
    for (nums, solution) in tests:
        result = sol.maximumCount(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

