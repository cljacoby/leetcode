# https://leetcode.com/problems/valid-palindrome

'''
Notes:
    - Problem is easy enough, altough I made a couple silly mistakes,
      probably because I assumed it was easy and didn't pay attention
    - Made a bounds checking mistake when `s` after running clean()
      was only length 0 or length 1. Added a check
    - Initially I did `set(string.ascii_lowercase)`, mentally equating
      that to alphanumeric which is wrong. Should have paid closer
      attention.
'''

class Solution(object):
    def alphanumeric(self):
        s = set()
        for i in range(ord('a'), ord('z') + 1):
            s.add(chr(i))
        for i in range(ord('0'), ord('9') + 1):
            s.add(chr(i))
        return s

    def clean(self, s):
        alphanumeric = self.alphanumeric()
        s = s.lower()
        s = "".join([ch for ch in s if ch in alphanumeric])
        return s

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.clean(s)
        if len(s) == 0 or len(s) == 1:
            return True
        i, j = 0, len(s) - 1
        while s[i] == s[j] and i <= j:
            i += 1
            j -= 1
        return j < i

        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("a", True),
        ("0P", False),
    ]
    for (s, solution) in tests:
        result = sol.isPalindrome(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

