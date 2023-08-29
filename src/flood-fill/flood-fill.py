# https://leetcode.com/problems/flood-fill

'''
Key Insights:
    - Overall straight-forward BFS problem
    - Found at that 4 * q.append() saves a lot of memory in comparison
      to q.extend([...]). This is kind of expected not having to
      allocate for an ad-hoc list argument
    - Also found that a m*n array of booleans is more memory effecient
      than a set using a 2-tuple of the (x,y) coordinates. This also
      kind of makes sense, although was not as immediately obvious in my
      head. Also wonder if this changes at some point based on scale of
      m*n
    - Actually the leetcode percentiles are deceptive, the tuple vs. 2d
      array memory difference is very slight. It just manifests in a big
      percentile difference on Leetcode; however, these percentiles
      alsop appear pretty inconsistent run-to-run.
'''

from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        q = deque([(sr, sc)])
        visited = [[False for i in range(cols)] for j in range(rows)]
        og_color = image[sr][sc]
        while len(q) > 0:
            (x, y) = q.pop()
            if (x < 0
                or y < 0
                or x >= rows
                or y >= cols
                or visited[x][y]
            ):
                continue
            visited[x][y] = True
            if image[x][y] == og_color:
                image[x][y] = color
                q.append((x + 1, y))
                q.append((x - 1, y))
                q.append((x, y + 1))
                q.append((x, y - 1))
        return image


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,1,1],[1,1,0],[1,0,1]],
            (1,1),
            2,
            [[2,2,2],[2,2,0],[2,0,1]],
        )
    ]
    for (image, (sr,sc), color, solution) in tests:
        result = sol.floodFill(image, sr, sc, color)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")
