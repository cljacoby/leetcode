# https://leetcode.com/problems/lexicographically-smallest-equivalent-string

'''

Solution 1:
    - Create a 2d array, where top level array element
      is a list of lexographically equivalent characters in sorted
      order.
    - Create a dictionary of characters to the index in the 2d array of
      the corresponding lexo group
    - Sometimes lexo groups will need to be merged. In this case, copy
      all the elements of one group into the other group, and clear the
      group which didn't recieve the copied aggregation. Loop through
      the characters dictionary and update any effected indices to the
      aggregrated group's index
    - Loop over the characters of baseStr, see if the character
      corresponds to a lexo group, and if so take th first array element
      which is the smallest lexographically equivalent character

Solution2:
    - Use a UnionFind data structure, with 26 integer values
      corresponding to the ascii_lowercase elements.
    - Zip iterate over s1 and s2, and union all the characters
    - Loop over baseStr and for each character do a UnionFind to get the
      lexographically smallest equivalent

'''

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        lexo = []
        chars = dict()
        for a, b in zip(s1, s2):
            if a not in chars and b not in chars:
                lexo.append(sorted([a, b]))
                chars[a] = len(lexo) - 1
                chars[b] = len(lexo) - 1
            elif b not in chars:
                idx = chars[a]
                group = lexo[idx]
                group.append(b)
                group.sort()
                chars[b] = idx
            elif a not in chars:
                idx = chars[b]
                group = lexo[idx]
                group.append(a)
                group.sort()
                chars[a] = idx
            elif chars[a] != chars[b]:
                mx = max(chars[a], chars[b])
                mn = min(chars[a], chars[b])
                group = lexo[mx]
                lexo[mx].extend(lexo[mn])
                group.extend(lexo[mn])
                group.sort()
                for c in chars:
                    if chars[c] == mn:
                        chars[c] = mx
                lexo[mn].clear() 
        out = ""
        for char in baseStr:
            if char not in chars:
                out += char
            else:
                idx = chars[char]
                group = lexo[idx]
                newchar = group[0]
                out += newchar
        return out

class UnionFind(object):
    def __init__(self, cap):
        self.root = [i for i in range(cap)]

    def find(self, x):
        # path compression. update indices so that each idnex in the
        # chain points to the true root
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def _find(self, x):
        # no path compression
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            # note: already unioned
            return
        if x > y:
            self.root[x] = y
        else:
            self.root[y] = x

    def __repr__(self):
        s = f"UnionFind {{ root: {self.root} }}"
        return s

from string import ascii_lowercase

class Solution1(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        uf = UnionFind(len(ascii_lowercase))
        for a, b in zip(s1, s2):
            x = ord(a) - ord('a')
            y = ord(b) - ord('a')
            uf.union(x, y)
        print(uf)
        out = ""
        for ch in baseStr:
            idx = uf.find(ord(ch) - ord('a'))
            newch = ascii_lowercase[idx]
            out += newch
        return out


if __name__ == "__main__":
    sol = Solution1()
    tests = [
        ("parker", "morris", "parser", "makkek"),
        ("hello", "world",  "hold", "hdld"),
        ("leetcode", "programs", "sourcecode", "aauaaaaada"),
        (
            "aabbbabbbbbabbbbaabaabbaaabbbabaababaaaabbbbbabbaa",
            "aabbaabbbabaababaabaababbbababbbaaaabbbbbabbbaabaa",
            "buqpqxmnajphtisernebttymtrydomxnwonfhfjlzzrfhosjct",
            "auqpqxmnajphtiserneattymtrydomxnwonfhfjlzzrfhosjct"
        )
    ]
    for (s1, s2, baseStr, solution) in tests:
        result = sol.smallestEquivalentString(s1, s2, baseStr)
        assert result == solution, \
                f"result {result} != solution {solution}"
    print("✅ All tests passed")

