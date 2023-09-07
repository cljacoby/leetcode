# https://leetcode.com/problems/swim-in-rising-water

'''
Key Insights:
    - First try pass a leetcode hard. Don't know if I've done that before.
      Based off leetcode's numbers, code seems mid-ish w.r.t runtime. 
      Seems to use a lot of memory. If I didn't declare tuple literals
      all over the place, that would probably help.
    - MinHeap as priority queue is like cheatcodes activated for some of
      these hard problems. I should probably assimilate how to write one
      from scratch for full understanding.
'''

from heapq import heappush, heappop

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        grid = grid
        rows = len(grid)
        cols = len(grid[0])
        fin = (rows - 1, cols - 1)
        t = 0
        visited = set()
        heap = [(grid[0][0], (0,0))]
        while len(heap) > 0:
            if heap[0][0] > t:
                t += 1
                continue
            (h, (x, y)) = heappop(heap)
            if (x,y) == fin: 
                return t
            visited.add((x,y))
            for (ver, hor) in dirs:
                i = x + ver
                j = y + hor
                if (
                    i >= 0
                    and j >= 0
                    and i < rows
                    and j < cols
                    and (i,j) not in visited
                ):
                    heappush(heap, (grid[i][j], (i,j)))

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [0,1,2,3,4],
                [24,23,22,21,5],
                [12,13,14,15,16],
                [11,17,18,19,20],
                [10,9,8,7,6]
            ],
            16
        ),
        (
            [
                [0,2],
                [1,3]
            ],
            3
        ),
    ]
    for (grid, solution) in tests:
        result = sol.swimInWater(grid)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

