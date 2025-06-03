# https://leetcode.com/problems/matchsticks-to-square

'''
Sort the original matchsticks in descending order (big -> small), and 
then recursively attempt to put these in 1 of 4 buckets. Make a decision
to put a matchstick in a bucket and then recurse. We reach a call
depth equal to length of the length of matchsticks (meaning we put all
the matchsticks in buckets), check if all the sides are of equal length,
and if so return. Otherwise, backtrack and try the remaining decisions
putting matches into different buckets.

I'm lazy and did not get memoization to work, but in theory it should be
sorting the sides array at each call to step(), creating a hashmap key
from the current value of `n` and the sides values, and check if we've
already computed this before.
'''

class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        self.m = sorted(matchsticks, reverse=True)
        self.n = len(self.m)
        self.cache = dict()
        tot = sum(self.m)
        if tot % 4 != 0:
            return False
        self.avglen = tot // 4
        sides = [0] * 4
        return self.step(0, sides)

    def step(self, n, sides):
        if n == self.n:
            return all(s == self.avglen for s in sides)
        sides.sort(reverse=True)
        for i in range(4):
            if sides[i] + self.m[n] > self.avglen:
                continue
            sides[i] += self.m[n]
            if self.step(n + 1, sides):
               return True
            sides[i] -= self.m[n] 
        return False 

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,1,2,2,2], True),
        ([3,3,3,3,4], False),
        ([10,6,5,5,5,3,3,3,2,2,2,2], True),
        ([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511], False),
        ([5,5,5,5,16,4,4,4,4,4,3,3,3,3,4], False),
    ]
    for (matchsticks, solution) in tests:
        result = sol.makesquare(matchsticks)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

