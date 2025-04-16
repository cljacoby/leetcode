# https://leetcode.com/problems/count-the-number-of-good-subarrays

'''
two-pointers / sliding-window problem.

- Start by growing the right side of the window unti either
  we have a window good count >= k, or we reach the array end
- If we get a good count >= k, start shrinking the left side of the
  array. For every element we can pop off the left side, if the good
  count remains >= k, increment the return count
- The key is recognizing that any good sub-array found within the middle
  of the array can have all remaining numbers rightward of the window
  appended on and still be a good array. Therefore, when we increment
  count, we increment it as `count += n - right`
'''


class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        g = 0
        count = 0
        d = dict()
        left = 0
        right = -1
        while left < n:
            while g < k and right + 1 < n:
                right += 1
                num = nums[right]
                if num not in d:
                    d[num] = 1
                else:
                    g += d[num]
                    d[num] += 1
            if g >= k:
                count += n - right
            num = nums[left]
            d[num] -= 1
            g -= d[num]
            left += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,1,1,1,1], 10, 1),
        ([3,1,4,3,2,2,4], 2, 4),
        ([2,1,3,1,2,2,3,3,2,2,1,1,1,3,1], 11, 21),
    ]
    for (nums, k, solution) in tests:
        result = sol.countGood(nums, k)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

