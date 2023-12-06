# https://leetcode.com/problems/count-of-matches-in-tournament

class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        teams = n
        matches = 0
        while teams > 1:
            if teams % 2 == 0:
                matches += teams // 2
                teams //= 2
            else:
                matches += (teams - 1) // 2
                teams = 1 + (teams - 1) // 2
        return matches
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (7,6),
        (14,13),
    ]
    for (teams, matches) in tests:
        result = sol.numberOfMatches(teams)
        assert matches == result, \
            f"result {result} != matches {matches}"
    print("✅ All tests passed")

