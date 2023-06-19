# https://leetcode.com/problems/3sum

import json

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.solutions = list()
        for i in range(len(nums)):
            self.step(nums, list(), 0, i)
        return self.solutions

    def step(self, nums, path, target, idx):
        num = nums[idx]
        path.append(num)
        t = target + num
        # print(f"path={path}, num={num}, idx={idx}, t={t}")
        if len(path) == 3:
            if t == 0:
                s = sorted(path[:])
                if s not in self.solutions:
                    self.solutions.append(s)
        else:
            for i in range(idx + 1, len(nums)):
                self.step(nums, path, t, i) 
        path.pop()

if __name__ == "__main__":
    sol = Solution()
    tests = [
        # ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        # ([3,0,-2,-1,1,2], [[-2,-1,3],[-2,0,2],[-1,0,1]])
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        (json.load(open("test1.json")), [0,1,2]),
    ]
    for (nums, solution) in tests:
        print("********************")
        print(f"nums={nums}")
        result = sol.threeSum(nums)
        assert sorted(result) == sorted(solution), \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

