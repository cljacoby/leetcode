"""
Edge Cases:
    - Empty Array
    - Duplicate numbers at different indices
    - Positivites, neagtives
    - Last loop increment when using slice logic

Notes:
    _ As minor performance improvemnt, you could skip last iteration of i loop
"""


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        for i, el_i in enumerate(nums):
            for j, el_j in enumerate(nums[i + 1 :], start=i + 1):
                if el_i + el_j == target:
                    return [i, j]
        else:
            raise Exception("No pair of elements adding to target")

    def twoSum2(self, nums, target):
        d = dict()
        for i, el in enumerate(nums):
            diff = target - el
            if diff in d:
                return [i, d[diff]]
            d[el] = i


if __name__ == "__main__":
    solution = Solution()
    tests = [([2, 7, 11, 15], 9), ([3, 2, 4], 6)]
    for nums, target in tests:
        # result = solution.twoSum(nums, target)
        result = solution.twoSum2(nums, target)
        print(
            (f"nums = `{nums}`,\n" f"target = `{target}`,\n" f"result = `{result}`\n")
        )
