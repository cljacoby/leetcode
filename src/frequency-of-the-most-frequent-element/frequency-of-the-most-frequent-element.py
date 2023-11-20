# https://leetcode.com/problems/frequency-of-the-most-frequent-element

'''
Needed to reference solutions on this one. Key insight is mentally
reframing this as a sliding window problem. Input array is sorted
to start. Then items are held in the window based on the following
invariant:

    window[-1] * len(window) - sum(window) <= k

What this is asserting is that the product of the last window element
times the length of the window should be greater than the window's sum
by at least `k`. This is because we can distribute `k` incrementations
across the window to make all elements equal to the last element, which
is always the largest because of the initial sort. If this invariant
breaks, then we deque elements from the left side until the invariant is
held again.

Then calculating the maximum frequency is as simple as taking the
maximum window size over the iteration through `nums`.
'''

# Solution using deque.
from collections import deque
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        window = deque()
        mx = total = 0
        for x in nums:
            window.append(x)
            total += x
            while window[-1] * len(window) - total > k:
                total -= window.popleft()
            mx = max(mx, len(window))
        return mx

# Solution using 2 pointers
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = mx = total = 0
        for right in range(len(nums)):
            total += nums[right]
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            mx = max(mx, right - left + 1)
        return mx

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 4], 5, 3),
        ([1, 4, 8, 13], 5, 2),
        ([
            9940,9995,9944,9937,9941,9952,9907,9952,
            9987,9964,9940,9914,9941,9933,9912,
            9934,9980,9907,9980,9944,9910,9997
        ], 7925, 22),
    ]
    for (nums, k, solution) in tests:
        result = sol.maxFrequency(nums, k)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")
