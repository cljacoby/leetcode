# https://leetcode.com/problems/unique-length-3-palindromic-subsequences

'''
Had to reference others solutions on this one. I had the right idea of
building the index map. Where I went wrong was trying to iterate over
the first half of characters up to a midpoint testing each for a
palindrome.

The key insight was recognizing any 3 length palindrome will be specific
to characters with a count >= 2. Therefore, we can take all of these
instances, take the first and last index, slice the string, and count
the unique characters occuring within. Summing these together yields the
answer.
'''

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        idxmap = dict()
        for i, char in enumerate(s):
            if char not in idxmap:
                idxmap[char] = [i]
            else:
                idxmap[char].append(i)
        count = 0
        for char, idx in idxmap.items():
            if len(idx) < 2:
                continue
            start = idx[0]
            end = idx[-1]
            sliced = s[start+1:end]
            uniques = set(sliced)
            count += len(uniques)
        return count

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("aabca", 3),
        ("bbcbaba", 4),
        ("aywvhbwycmbttdmogwlfosfizqlndfipffbqfxwbgrfdyomuuecllmsrzckiwgelkhgylwobz", 326),
        (open("test1.txt").read(), 676)
    ]
    for (s, solution) in tests:
        result = sol.countPalindromicSubsequence(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

