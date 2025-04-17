# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array

'''
- Use a dictionary to keep a map of an array element value to all
  indices of that value 
- Iterate over each (index, element) in the array, and see whether this
  element has been observed at previous indices
- For each earlier index, test whether the product of the two indices is
  evenly divisble by k, and if so increment count
- Return the final count
'''

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        idx = dict()
        count = 0
        for i, num in enumerate(nums):
            if num in idx:
                for j in idx[num]:
                    if (i * j) % k == 0:
                        count += 1
            else:
                idx[num] = []
            idx[num].append(i)
        return count

# Slightly compacted syntax using defaultdict
from collections import defaultdict
class Solution1(object):
        idx = defaultdict(list)
        count = 0
        for i, num in enumerate(nums):
            for j in idx[num]:
                if (i * j) % k == 0:
                    count += 1
            idx[num].append(i)
        return count

if __name__ == "__main__":
    sol = Solution()
    solvers = [Solution(), Solution1()]
    tests = [
        ([3,1,2,2,2,1,3], 2, 4),
        ([1,2,3,4], 1, 0),
    ]
    for (nums, k, solution) in tests:
        for sol in solvers:
            result = sol.countPairs(nums, k)
            assert result == solution, \
                f"result {result} != solution {solution}"
    print("✅ All tests passed")

