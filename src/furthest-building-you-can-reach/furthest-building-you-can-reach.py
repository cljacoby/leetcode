# https://leetcode.com/problems/furthest-building-you-can-reach

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        jumps = [heights[h] - heights[h - 1] for h in range(1, len(heights))]
        jumps.sort(reverse=True)
        # print(f"jumps = {jumps}")
        curr = (0, heights[0])
        for i,h in enumerate(heights[1:], start=1):
            # print(f"i={i}, h={h}, ladders={ladders}, bricks={bricks}, jumps={jumps}")
            diff = h - curr[1]
            if diff <= 0:
                curr = (i,h)
            elif diff in jumps[0:ladders] \
            or (ladders > 0 and diff >= bricks):
                ladders -= 1
                curr = (i,h)
            elif bricks >= diff:
                bricks -= diff
                curr = (i,h)
            else:
                return curr[0]
        return curr[0]

            

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([14, 3, 19, 3], 17, 0, 3),
        ([4,12,2,7,3,18,20,3,19], 10, 2, 7),
        ([14,3,19,3], 17, 0, 3),
        ([1,5,1,2,3,4,10000], 4, 1, 5),
    ]
    for heights, bricks, ladders, solution in tests:
        result = sol.furthestBuilding(heights, bricks, ladders)
        assert result == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")
