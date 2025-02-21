# https://leetcode.com/problems/find-unique-binary-string

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        self.n = len(nums)
        self.nums = set(nums)
        path = []
        ret = self.step(path)
        return ret

    def step(self, path):
        if len(path) == self.n:
            b = "".join(path)
            if b not in self.nums:
                return b
            return None

        path.append("0")
        a = self.step(path)
        path.pop()
        if a: return a

        path.append("1")
        b = self.step(path)
        path.pop()
        return b

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["01","10"], ["11",  "00"]),
        (["111","011","001"], ["101", "000", "010", "100", "110"]),
    ]
    for (nums, solutions) in tests:
        result = sol.findDifferentBinaryString(nums)
        assert result in solutions, \
            f"result {result} not in solutions {solutions}"
    print("✅ All tests passed")

