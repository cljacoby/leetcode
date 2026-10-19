# https://leetcode.com/problems/search-in-rotated-sorted-array

'''
Notes:
    - Duration: ~22 minutes
    - Intuition was correct. Implement a regular-old binary search, then
      partition the list by the condition `x[i] > x[i + 1]`. Run binary
      search on each side of the partition, and adjust the final index
      accordingly if the value was found on the right partition side
    - Spent a little extra time debugging because I just brain farted
      and added an erroneous `-1` to the `j` argument of the
      binary_search() calls on each partition
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find partition point where `x[i] > x[i+1]`, if it exists, then
        # partition into left and right halves
        partition = 0
        for i in range(len(nums) - 1):
            j = i + 1
            if nums[i] > nums[j]:
                partition = j
                break
        left, right = nums[:partition], nums[partition:]

        # run binary search on each partition, if it appears
        # the partition could contain the target value, based on the
        # sorted ordering. adjust final return idx if target was found
        # on the right partition.
        if (len(left) > 0
                and target >= left[0]
                and target <= left[-1]
        ):
            return self.binary_search(0, len(left), left, target)
        if (len(right) > 0
                and target >= right[0]
                and target <= right[-1]
        ):
            idx = self.binary_search(0, len(right), right, target)
            return idx if idx == -1 else idx + len(left)
        return -1

    def binary_search(self, i, j, nums, target):
        if i == j:
            return -1
        if j - i == 1:
            idx = i if nums[i] == target else -1
            return idx
        m = (j - i) // 2
        mid = i + m
        if target < nums[mid]:
            return self.binary_search(i, mid, nums, target)
        return self.binary_search(mid, j, nums, target)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([0,1,2,4,5,6,7,], 4, 3),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 9, -1),
        ([1,3], 3, 1),
    ]
    for (nums, target, solution) in tests:
        print("-------------------------------------------")
        result = sol.search(nums, target)
        print(f"nums={nums}, target={target}, solution={solution}, result={result}")
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

