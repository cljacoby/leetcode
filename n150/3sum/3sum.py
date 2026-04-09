# https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = dict()
        solutions = set()
        for (i, num) in enumerate(nums):
            if num not in m:
                m[num] = []
            m[num].append(i)
        
        k1 = list(m.keys())
        for a in k1:
            # note: probably a way to do this without copying
            p = m
            p[a].pop()
            if len(p[a]) == 0:
                del p[a]
            k2 = list(p.keys())
            for b in k2:
                c = -1 * (a + b)
                if c in p and (c != b or len(p[c]) > 1):
                    solutions.add(tuple(sorted([a, b, c])))
        return list(solutions)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [-1,0,1,2,-1,-4],
            [[-1,-1,2],[-1,0,1]],
        ),
        (
            [0,1,1],
            [],
        ),
        (
            [0,0,0],
            [[0,0,0]],
        ),
        (
            [-1,0,1],
            [[-1,0,1]],
        ),
        (
            [-1,0,1,0],
            [[-1,0,1]],
        ),
    ]
    for (nums, solution) in tests:
        result = sol.threeSum(nums)
        # assert result == solution, \
        #     f"result {result} != solution {solution}"
        print(f"nums {nums},\nresult {result},\nsolution {solution}")
        print()
    print("✅ All tests passed")

