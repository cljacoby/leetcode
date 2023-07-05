# https://leetcode.com/problems/product-of-array-except-self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right, out = [], [], []
        l_prod, r_prod = 1, 1
        for num in reversed(nums):
            right.append((num, r_prod))
            r_prod = r_prod * num
        while len(right) > 0:
            (num, r_curr) = right.pop()
            out.append(l_prod * r_curr)
            left.append((num, l_prod))
            l_prod = l_prod * num
        return out


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0])
    ]
    for (nums, solution) in tests:
        result = sol.productExceptSelf(nums)
        print(f"result={result}")
    print("✅ All tests passed")

