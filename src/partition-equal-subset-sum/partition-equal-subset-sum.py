# https://leetcode.com/problems/partition-equal-subset-sum

"""
First we observe the two partition the array into two halves, the
overall sum must be evenly disible by two. Base check.

We take the sum and divide by two to get the target sum of each
partition. Then, we initialize a `dp` array to size of `target + 1`,
with all values initialized to false. Our `dp` array will track at each
index `i` whether the subset sum of `i` is acheivable. We set dp[0]
equal to True, since it's always possible to achieve a subset sum of
zero using an empty set (which is technically a subset).

At the we return dp[target], i.e. whether it was possible to achieve a
subset sum equal to the target, i.e. half the total sum.

"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tot = sum(nums)
        if tot % 2 != 0:
            return False
        target = tot // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for currSum in range(target, num - 1, -1):
                print(f"num={num}, currSum={currSum}, dp={dp}")
                dp[currSum] = dp[currSum] or dp[currSum - num]
        return dp[target]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
    ]
    for (nums, solution) in tests:
        result = sol.canPartition(nums)
        assert result == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")
