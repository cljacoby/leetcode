# https://leetcode.com/problems/binary-trees-with-factors

class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        self.factors = set(arr)
        self.solution = [] 
        for f in self.factors:
            self.step(f, [])
        return self.solution

    def step(self, prod, path):
        if prod == 1:
            self.solution.append(path.copy())
        if prod == 0 or prod not in self.factors:
            return
        for f in self.factors:
            path.append(f)
            q = prod // f
            self.step(q, path)
            path.pop()



if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [2,4],
            [[2], [4], [4, 2, 2]],
            # 3,
        ),
        (
            [2,4,5,10],
            [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2],
            # 7,
        )
    ]
    for (arr, solution) in tests:
        result = sol.numFactoredBinaryTrees(arr)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

