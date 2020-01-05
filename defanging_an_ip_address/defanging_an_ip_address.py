from types import SimpleNamespace as Ns
import unittest as ut

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

class TestSolution(ut.TestCase):
    
    def cases(self):
        return [
            Ns(input="", output=""),
            Ns(input=".", output="[.]"),
            Ns(input="1.1.1.1", output="1[.]1[.]1[.]1"),
            Ns(input="255.100.50.0", output="255[.]100[.]50[.]0"),
            Ns(input="255_100_50_0", output="255_100_50_0"),
        ]

    def test_cases(self):
        sol = Solution()
        for case in self.cases():
            result = sol.defangIPaddr(case.input)
            self.assertEqual(result, case.output)

if __name__ == "__main__":
    ut.main()
