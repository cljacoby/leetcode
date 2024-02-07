# https://leetcode.com/problems/sort-characters-by-frequency

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = dict()
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        pairs = [(k,v) for k,v in
                sorted(freq.items(), key=lambda pair: pair[1],
                    reverse=True)]
        s = ""
        for (ch, count) in pairs:
            s += ch * count
        return s
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("cccaaa", "cccaaa"),
        ("Aabb", "bbAa"),
    ]
    for (s, solution) in tests:
        result = sol.frequencySort(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

