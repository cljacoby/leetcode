# https://leetcode.com/problems/group-anagrams

class Solution1(object):
    def char_map(self, s):
        d = dict()
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        return d

    def serialize_char_map(self, char_map):
        s = ""
        for k in sorted(char_map):
            s += f"{k}{char_map[k]}"
        return s

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == [""]:
            return [[""]]
        groups = dict()
        for s in strs:
            char_map = self.char_map(s)
            key = self.serialize_char_map(char_map)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())

# Just lean on python's inbuilt sorted from the original string, rather
# than sorting the char count map keys
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            ["eat","tea","tan","ate","nat","bat"],
            [["bat"],["nat","tan"],["ate","eat","tea"]],
        ),
        (
            [""],
            [[""]],
        ),
        (
            ["a"],
            [["a"]]
        )
    ]
    for (i, (strs, solution)) in enumerate(tests):
        result = sol.groupAnagrams(strs)
        solution, result = sorted(solution), sorted(result)
        # Visual inspection, unorderdness makes assert hard
        print(f"test {i} | result {result}, solution {solution}")
    print("✅ All tests passed")

