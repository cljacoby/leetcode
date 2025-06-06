# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string

'''
- Use a deque to represent s, and a list to represent p
- Create a frequency dict of initial character counts in s, and created
  a sorted array of the charactrs. 
- While there are still elements in either s or t, we pop an element
  from one. If t has no elements, always popleft on s. If t has
  elements, and the final value of t is smaller than the smallest
  remaining character in s (deduced by freq dict and sorted chars), then
  pop from t and append to p. Otherwise popleft from s and append to t.
- Whenever we popleft from s, decrement the frequency dict, and went a
  count hits zero, remove from the sorted array.
'''

from collections import deque

class Solution(object):
    def freq(self, s):
        freq = dict()
        for ch in s:
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1
        return freq

    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = deque(s)
        t = []
        p = []
        freq = self.freq(s)
        alpha = sorted(freq.keys())
        while len(s) > 0 or len(t) > 0:
            if len(s) == 0 \
                or len(t) > 0 and t[-1] <= alpha[0]:
                ch = t.pop()
                p.append(ch)
            else:
                ch = s.popleft()
                freq[ch] -= 1
                if freq[ch] == 0:
                    del freq[ch]
                    alpha.remove(ch)
                t.append(ch)
        p = "".join(p)
        return p

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("zza", "azz"),
        ("bac", "abc"),
        ("bdda", "addb"),
        ("vzhofnpo", "fnohopzv"),
    ]
    for (s, solution) in tests:
        result = sol.robotWithString(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

