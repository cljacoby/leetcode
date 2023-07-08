# https://leetcode.com/problems/minimum-window-substring

'''
Key Insights:
    1) Did pretty good on this. Felt like a medium+ instead of a hard.
      Or maybe the practice is just working.

    2) On first attempt, I messed up setting the
      initial value of `size` to low. I set it to 1000, but input size
      could be 10^5. Basically did all the tricky programming correct, and
      goofed on an assumption.

    3) This is basically a harder version of
      'longest-substring-without-repeating-characters', but the premise of
      the solition is the same. Instead of combinining the properties of a
      set and a deque, you combine the properties of a dict and a dequeu
      (although I used Counter instead of dict for slight conveniance).
'''

import json
from operator import itemgetter
from collections import deque
from collections import Counter

class Solution(object):

    def valid_win(self, ds, dt):
        for key in dt:
            if key not in ds \
            or ds[key] < dt[key]:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dt = Counter(t)
        ds = Counter()
        q = deque([])
        size = pow(10, 5) + 1
        res = ""
        for char in s:
            if char not in dt and len(ds) == 0:
                continue
            q.append(char)
            if char in dt:
                ds[char] += 1
                while ds[char] >= dt[char]:
                    if q[0] in dt and ds[q[0]] <= dt[q[0]]:
                        break
                    out = q.popleft()
                    ds[out] -= 1
            if self.valid_win(ds, dt):
                if len(q) < size:
                    size = len(q)
                    res = "".join([c for c in q])
        return res

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        itemgetter('s', 't', 'solution')(json.load(open("test1.json")))
    ]
    for (s, t, solution) in tests:
        result = sol.minWindow(s, t)
        assert result == solution, \
            f"result '{result}' != solution '{solution}'"
    print("✅ All tests passed")

