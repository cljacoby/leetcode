# https://leetcode.com/problems/binary-search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(0, len(nums), nums, target)

    def binary_search(self, i, j, nums, target):
        if i == j:
            return -1
        if i + 1 == j:
            out = i if nums[i] == target else -1
            return out
        m = (j - i) // 2
        mid = i + m
        if target < nums[mid]:
            return self.binary_search(i, mid, nums, target)
        return self.binary_search(mid, j, nums, target)
        

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

