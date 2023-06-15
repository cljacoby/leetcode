# https://leetcode.com/problems/longest-substring-without-repeating-characters

from collections import deque

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        substr = deque()
        peak = 0
        for char in s:
            while char in seen:
                out = substr.popleft()
                seen.remove(out)
            seen.add(char)
            substr.append(char)
            peak = max(peak, len(substr))
        return peak

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("bbbbb", 1),
    ]
    for (s, solution) in tests:
        result = sol.lengthOfLongestSubstring(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

