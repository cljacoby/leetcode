# https://leetcode.com/problems/three-consecutive-odds

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for i in arr:
            if i % 2 > 0:
                count +=1
            else:
                count = 0
            if count == 3:
                return True
        return False
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,6,4,1], False),
        ([1,2,34,3,4,5,7,23,12], True),
    ]
    for (arr, solution) in tests:
        result = sol.threeConsecutiveOdds(arr)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

