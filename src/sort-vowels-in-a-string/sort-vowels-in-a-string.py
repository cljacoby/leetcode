# https://leetcode.com/problems/sort-vowels-in-a-string

from heapq import heappush, heappop
from collections import deque

class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set([
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U',
        ])
        idx = deque()
        v = []
        s = [i for i in s]
        for i, char in enumerate(s):
            if char in vowels:
                idx.append(i)
                heappush(v, char)
        while len(v) > 0 and len(idx) > 0:
            assert len(v) == len(idx), "Queue length mismatch"
            i = idx.popleft()
            char = heappop(v)
            s[i] = char
        return "".join(s)

# No heap or deque. Just use regular list and reverse sort before
# second loop.
class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set([
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U',
        ])
        idx = []
        v = []
        s = [i for i in s]
        for i, char in enumerate(s):
            if char in vowels:
                idx.append(i)
                v.append(char)
        v.sort(reverse=True)
        idx = list(reversed(idx))
        while len(v) > 0 and len(idx) > 0:
            assert len(v) == len(idx), "Queue length mismatch"
            i = idx.pop()
            char = v.pop()
            s[i] = char
        return "".join(s)
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("lEetcOde", "lEOtcede"),
    ]
    for (s, solution) in tests:
        result = sol.sortVowels(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

