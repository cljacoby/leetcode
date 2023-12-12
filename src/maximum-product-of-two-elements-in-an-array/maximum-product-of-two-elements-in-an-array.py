# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = [0, 0]
        for i, num in enumerate(nums):
            if num > mx[0]:
                tmp = mx[0]
                mx[0] = num
                if tmp > mx[1]:
                    mx[1] = tmp
            elif num > mx[1]:
                mx[1] = num
        return (mx[0] - 1) * (mx[1] - 1)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, 4, 5, 2], 12),
        ([1, 5, 4, 5], 16),
        ([3, 7], 12),
    ]
    for (arr, solution) in tests:
        result = sol.maxProduct(arr)
        assert result == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")
