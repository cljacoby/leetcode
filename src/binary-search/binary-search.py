# https://leetcode.com/problems/binary-search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bisect(nums, 0, len(nums) - 1, target)

    def bisect(self, nums, i, j, target):
        if j < i:
            return -1
        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            return self.bisect(nums, i, mid - 1, target)
        return self.bisect(nums, mid + 1, j, target)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-1,0,3,5,9,12], 9, 4),
        ([-1,0,3,5,9,12], 2, -1),
    ]
    for (nums, target, solution) in tests:
        result = sol.search(nums, target)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

