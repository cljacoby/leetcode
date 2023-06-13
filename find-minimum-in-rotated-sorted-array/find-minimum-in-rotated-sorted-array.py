# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array


'''
Need to find where the cut-off is.
It can either land in the middle of the left half,
the right half, or directly in the middle. We want to bisect
on whichever half has the cut-off.

If we've already passed the cut-off, we want to bisect on
the smaller half. I.e. basically just ordinary binary search.

[2, 3, 4, | 5, 6, 0, 1]

[6, 0, 1, | 2, 3, 4, 5]

[0, 1, 2, | 3, 4, 5, 6]
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.bisect(nums)

    def bisect(self, nums):
        print(f"nums = {nums}")
        length = len(nums)
        if length == 1:
            return nums[0]
        mid = length // 2
        left, right = nums[:mid], nums[mid:]
        print(f"left = {left}, right = {right}")
        if right[0] > right[-1]:
            return self.bisect(right)
        elif left[0] > left[-1]:
            return self.bisect(left)
        elif left[-1] > right[0]:
            return self.bisect(right)
        else:
            return self.bisect(left)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11),
    ]
    for (nums, solution) in tests:
        print("************************************")
        result = sol.findMin(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

