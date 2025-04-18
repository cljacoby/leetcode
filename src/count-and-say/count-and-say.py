# https://leetcode.com/problems/count-and-say

# recursive
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        prev = None
        count = 0
        out = ""
        for ch in s:
            if prev == None:
                prev = ch
                count += 1
            elif prev == ch:
                count += 1
            else:
                out += f"{count}{prev}"
                prev = ch
                count = 1
        out += f"{count}{ch}"
        return out

# iterative
class Solution1(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        assert n >= 1 and n <= 30, "n not in range [1,30]"
        rle = [None] * n
        rle[0] = "1"
        for i in range(1, n):
            s = rle[i - 1]
            prev = None
            count = 0
            res = ""
            for ch in s:
                if prev == None:
                    prev = ch
                    count += 1
                elif prev == ch:
                    count += 1
                else:
                    res += f"{count}{prev}"
                    prev = ch
                    count = 1
            res += f"{count}{ch}"
            rle[i] = res
        return rle[n - 1]

if __name__ == "__main__":
    solvers = [Solution(), Solution1()]
    tests = [
        (4, "1211"),
        (10, "13211311123113112211"),
    ]
    for (n, solution) in tests:
        for sol in solvers:
            result = sol.countAndSay(n)
            assert result == solution, \
                f"result {result} != solution {solution}"
    print("✅ All tests passed")

