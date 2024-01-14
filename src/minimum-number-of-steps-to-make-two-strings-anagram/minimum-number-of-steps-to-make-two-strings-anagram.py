# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

# First attempt. Eventaully got it without referencing solutions, but
# wasn't pretty.
class Solution(object):
    def char_freq(self, word):
        count = dict()
        for char in word:
            count[char] = count.get(char, 0) + 1
        return count

    def under_over(self, s, t, smap, tmap):
        under, over = list(), list()
        for char in set(s + t):
            if char not in smap:
                over.extend([char for _ in range(tmap[char])])
            elif char not in tmap:
                under.extend([char for _ in range(smap[char])])
            elif tmap[char] < smap[char]:
                under.extend([char for _ in range(smap[char] - tmap[char])])
            elif tmap[char] > smap[char]:
                over.extend([char for _ in range(tmap[char] - smap[char])])
        return under, over

    def minSteps(self, s, t):
        smap = self.char_freq(s)
        tmap = self.char_freq(t)
        ops = 0
        under, over = self.under_over(s, t, smap, tmap)
        while len(over) > 0:
            o = over.pop()
            if len(under) > 0:
                u = under.pop()
                tmap[u] = tmap.get(u, 0) + 1
            tmap[o] -= 1
            if tmap[o] == 0:
                del tmap[o]
            ops += 1
        while len(under) > 0:
            u = under.pop()
            tmap[u] = tmap.get(u, 0) + 1
            ops += 1
        return ops


# Leetcoderific style solution. Used 26 length fixed arrays, and take
# the ASCII digit for each character. Subtract the ASCII digit for 'a'
# to make the ASCII offset start at array index zero. This also only
# works because the problem states lowercase only, although upper case
# could be supported with simple changes.
#
# Interestingly according to Leetcode this solution and the first
# solution have about the same runtime performance.
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sc = [0] * 26
        tc = [0] * 26
        steps = 0
        for c in s:
            sc[ord(c) - ord('a')] += 1
        for c in t:
            tc[ord(c) - ord('a')] += 1
        for i in range(0, 26):
            steps += abs(sc[i] - tc[i])
        return steps // 2
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("bab", "aba", 1),
        ("leetcode", "practice", 5),
    ]
    for (s, t, solution) in tests:
        result = sol.minSteps(s, t)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

