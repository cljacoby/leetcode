# https://leetcode.com/problems/count-hills-and-valleys-in-an-array

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dedup = [nums[0]]
        count = 0
        for i in range(1, length):
            if nums[i] == nums[i - 1]:
                continue
            dedup.append(nums[i])
        for i in range(1, len(dedup) - 1):
            left, mid, right = dedup[i - 1], dedup[i], dedup[i + 1]
            if left < mid and mid > right:
                count += 1
            elif left > mid and mid < right:
                count += 1
        return count

            
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,4,1,1,6,5], 3),
        ([6,6,5,5,4,1], 0)
    ]
    for (nums, solution) in tests:
        result = sol.countHillValley(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

