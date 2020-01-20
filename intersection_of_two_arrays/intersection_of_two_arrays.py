import unittest as ut
from types import SimpleNamespace as Ns


class Solution:

    # NOTE: MyPy style function signature supplied by leetcode is causing problems
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        s_nums1 = set(nums1)
        s_nums2 = set(nums2)
        return list(s_nums1 & s_nums2)

class TestSolution(ut.TestCase):
    def cases(self):
        return [
            Ns(input=([1, 2, 2, 1], [2, 2]), output=[2]),
            Ns(input=([4, 9, 5], [9, 4, 9, 8, 4]), output=[9, 4]),
        ]

    def test_cases(self):
        method = "intersection"
        sol = Solution()
        for case in self.cases():
            result = getattr(sol, method)(*case.input)
            print(f"input={case.input}, output={case.output}, result={result}")
            self.assertEqual(result, case.output)

if __name__ == "__main__":
    ut.main()
