# https://leetcode.com/problems/count-days-without-meetings

class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        i, j = 0, 1
        end = len(meetings)
        meetings = sorted(meetings, key=lambda x: x[0])
        while j < end:
            if meetings[j][0] <= meetings[i][1]:
                meetings[i][1] = max(meetings[j][1], meetings[i][1])
                meetings[j] = None
                j += 1
            else:
                i = j
                j = i + 1
        for m in meetings:
            if m != None:
                days -= m[1] - m[0] + 1
        return days
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (10, [[5,7],[1,3],[9,10]], 2),
        (5, [[2,4],[1,3]], 1),
        (10, [[2,2]], 9),
        (57, [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]], 1)
    ]
    for (days, meetings, solution) in tests:
        result = sol.countDays(days, meetings)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

