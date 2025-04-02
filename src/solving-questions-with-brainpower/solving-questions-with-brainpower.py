# https://leetcode.com/problems/solving-questions-with-brainpower

'''
Summary:
    1d array dynamic programming approach. Key is to iterate over array
    backwards to fill in results which exceed the array bounds, before
    getting to results which add to previous results.

Detailed:
    - Use a 1d array dynamic programming approach
    - Iterate over the array backwards
    - For each tuple, add `skip` to the current `index` and see if this
      index is within the array.
    - If out of bounds, update dp[i] to simply equal the current points
    - If in bounds, update dp[i] to the sum of the current question's
      points, plus the dp slot corresponding to index `skip + i + 11
'''

class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        sz = len(questions)
        dp = [0] * sz
        mx = 0
        for j in range(sz):
            i = sz - j - 1
            points, skip = questions[i]
            prev = i + skip + 1
            if prev >= sz:
                dp[i] = max(mx, points)
            else:
                dp[i] = max(mx, dp[prev] + points)
            mx = max(dp[i], mx)
        return mx


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[3,2],[4,3],[4,4],[2,5]], 5),
        ([[1,1],[2,2],[3,3],[4,4],[5,5]], 7),
        ([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]], 157),
    ]
    for (questions, solution) in tests:
        result = sol.mostPoints(questions)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

