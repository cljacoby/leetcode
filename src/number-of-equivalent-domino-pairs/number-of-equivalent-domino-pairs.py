# https://leetcode.com/problems/number-of-equivalent-domino-pairs

'''
Iterate over all dominos, and for each domino, create an entry
in a counter HashMap. The key is the domino values in ascending
sorted order.

Then, either at the end or during the main loop, increment a total
value of the number of pairs which are rotatably equivalent dominos.
'''

from math import factorial
class Solution(object):
    def ncr(self, n, r):
        x = factorial(n) / (factorial(r) * factorial(n - r))
        return int(x)

    def numEquivDominoPairs(self, dominos):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        counts = dict()
        for dom in dominos:
            if dom[0] < dom[1]:
                s = f"{dom[0]}-{dom[1]}"
            else:
                s = f"{dom[1]}-{dom[0]}"
            if s not in counts:
                counts[s] = 0
            counts[s] += 1
        tot = 0
        for dom, count in counts.items():
            if count <= 1:
                continue
            tot += self.ncr(count, 2)
        return tot

class Solution1(object):
    def numEquivDominoPairs(self, dominos):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        counts = dict()
        tot = 0
        for dom in dominos:
            if dom[0] < dom[1]:
                s = f"{dom[0]}-{dom[1]}"
            else:
                s = f"{dom[1]}-{dom[0]}"
            if s not in counts:
                counts[s] = 0
            tot += counts[s]
            counts[s] += 1
        return tot

class Solution2(object):
    def numEquivDominoPairs(self, dominos):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        counts = [0] * 100
        tot = 0
        for dom in dominos:
            if dom[0] > dom[1]:
                key = dom[0] * 10 + dom[1]
            else:
                key = dom[1] * 10 + dom[0]
            tot += counts[key]
            counts[key] += 1
        return tot


if __name__ == "__main__":
    sols = [Solution(), Solution1(), Solution2()]
    tests = [
        ([[1,2],[2,1],[3,4],[5,6]], 1),
        ([[1,2],[1,2],[1,1],[1,2],[2,2]], 3),
    ]
    for sol in sols:
        for (dominos, solution) in tests:
            result = sol.numEquivDominoPairs(dominos)
            assert result == solution, \
                f"result {result} != solution {solution}"
    print("✅ All tests passed")

