# https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self._search(nums, target, 0, len(nums) - 1)

    def _search(self, nums, target, i, j):
        if i > j:
            return -1
        if i == j:
            return i
        mid = (i + j ) // 2
        print(f"nums={nums}, target={target}, i={i}, mid={mid}, j={j}")
        if (target >= nums[i] and target < nums[mid]) \
        or (target < nums[i] and nums[i] > nums[mid]):
            return self._search(nums, target, i, mid)

        elif (target >= nums[mid] and taget < nums[j]) \
        or (target < nums[mid] and nums[mid] > nums[j]):
            return self._search(nums, target, mid, j)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 7, 3),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
    ]
    for (nums, target, solution) in tests:
        result = sol.search(nums, target)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

