# https://leetcode.com/problems/min-cost-climbing-stairs


'''
Notes:
    - A dynamic programming problem I can actually intuit
    - I made one misake on the first iteration, which was not accounting
      for the problem allowing to start at the zero-th stair or the first
      stair. I had to correct `return dp[0]` into `return min(dp[0], dp[1])`
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        sz = len(cost)
        dp = [0 for i in range(sz)]
        for i in range(sz - 1, -1, -1):
            a = cost[i] if i + 1 >= sz else cost[i] + dp[i + 1]
            b = cost[i] if i + 2 >= sz else cost[i] + dp[i + 2]
            dp[i] = min(a, b)
        return min(dp[0], dp[1])        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,100,1,1,1,100,1,1,100,1],
            6,
        ),
        (
            [10,15,20],
            15,
        ),
    ]
    for (cost, solution) in tests:
        result = sol.minCostClimbingStairs(cost)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

