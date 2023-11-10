# https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        buf = []
        out = []
        for char in s:
            if char == ' ':
                while len(buf) > 0:
                    out.append(buf.pop())
                out.append(char)
            else:
                buf.append(char)
        while len(buf) > 0:
            out.append(buf.pop())
        return "".join(out)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            "Let's take LeetCode contest",
            "s'teL ekat edoCteeL tsetnoc",
        )
    ]
    for (s, solution) in tests:
        result = sol.reverseWords(s)
        assert result == solution, \
            f"result '{result}' == solution '{solution}'"
    print("✅ All tests passed")

