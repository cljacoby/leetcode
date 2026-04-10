# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution(object):
    NUM_TO_CHARS = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z'],
    }

    def step(self, digits, pre, i, solutions):
        if len(pre) == len(digits):
            solutions.append("".join(pre))
            return
        dig = int(digits[i]) 
        for ch in self.NUM_TO_CHARS[dig]:
            pre.append(ch)
            self.step(digits, pre, i + 1, solutions)
            pre.pop()


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pre = []
        i = 0
        solutions = []
        self.step(digits, pre, i, solutions)
        return solutions
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            "23",
            ["ad","ae","af","bd","be","bf","cd","ce","cf"],
        ),
        (
            "2",
            ["a","b","c"],
        ),
    ]
    for (digits, solution) in tests:
        result = sol.letterCombinations(digits)
        assert result == solution, \
            f"result {result} == solution {solution}"
    print("✅ All tests passed")

