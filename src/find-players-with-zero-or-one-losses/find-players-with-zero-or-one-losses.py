# https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution(object):
    def init_score(self, score, players):
        for p in players:
            if p not in score:
                score[p] = [0, 0]

    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        score = dict()
        for (w, l) in matches:
            self.init_score(score, [w, l])
            score[w][0] += 1
            score[l][1] += 1
        a, b = [], []
        for key, (w, l) in score.items():
            if l == 0:
                a.append(key)
            elif l == 1:
                b.append(key)
        a.sort()
        b.sort()
        return [a, b]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]],
            [[1,2,10],[4,5,7,8]],
        ),
        (
            [[2,3],[1,3],[5,4],[6,4]],
            [[1,2,5,6],[]],
        ),
    ]
    for (matches, solution) in tests:
        result = sol.findWinners(matches)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

