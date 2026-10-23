# https://leetcode.com/problems/pacific-atlantic-water-flow

'''
Notes:
    - In an actual interview setting, I would have wasted too much time
      on BadSolution, and probably would have failed on this question
    - The right intuition was framing the question around a set
      intersect, and building two sets of coordinates which could reach
      the atlantic and pacific respectively
    - The part I missed was how to avoid cycling. This is where I put in
      the bitmask that led to BadSolution. Instead the right idea is to
      invert the problem, and instead of trying to move down cells
      values (mirroring falling water) you should move up cell values
      starting from the grid boundaries. You keep two different visited
      sets, and the top and left grid boundaries use the `pacific` set,
      while the right and bottom grid boundaries use the `atlantic` set.
    - Then you do a simple intersection at the end to get the solution
'''

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.heights = heights
        self.n = len(self.heights)
        self.m = len(self.heights[0])

        pacific = set()
        atlantic = set()

        for i in range(self.n):
            self.step(i, 0, -1, pacific)
            self.step(i, self.m - 1, -1, atlantic)
        for j in range(self.m):
            self.step(0, j, -1, pacific)
            self.step(self.n - 1, j, -1, atlantic)

        intersect = atlantic & pacific
        return list(intersect)


    def step(self, i, j, prev, visited):
        if i < 0 or j < 0 or i >= self.n or j >= self.m or (i,j) in visited:
            return
        curr = self.heights[i][j]
        if curr < prev:
            return
        visited.add((i, j))
        self.step(i + 1, j, curr, visited)
        self.step(i - 1, j, curr, visited)
        self.step(i, j + 1, curr, visited)
        self.step(i, j - 1, curr, visited)

'''
Notes on BadSolution:
    - I originally was thinking along the lines of solving the problem
      using a set intersect solution of paths which reach pacific vs
      paths that reach atlantic
    - Somewhere along the way I thought I'd use a bitmask instead to
      propogate results up the stack, and then traverse the `board` at
      the end, observing which positions have a bitmask value of 3
    - This technically works, but the runtime complexity is exponential,
      so it fails on non-small inputs
    - The bitmask works as follows
        - pacific:   i=1, bin=00000001
        - atlantic:  i=2, bin=00000010
        - both:      i=3, bin=00000011
    - I probably should have known things would go awry when I thought a
      bitmask was the right fit for the problem
'''

class BadSolution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # constants
        self.n = len(heights)
        self.m = len(heights[0])
        self.heights = heights
        self.board = [[0 for j in range(self.m)] for i in range(self.n)]
        solution = []
        
        # pre-seed boundary results
        for j in range(self.m):
            self.board[0][j] = 1
            self.board[-1][j] = 2
        for i in range(self.n):
            self.board[i][0] = 1
            self.board[i][-1] = 2

        for i, row in enumerate(self.heights):
            for j, val in enumerate(row):
                self.step(i, j, set(), pow(10, 5) + 1)

        print(f"final board, board={self.board}")

        for i, row in enumerate(self.heights):
            for j, val in enumerate(row):
                if self.board[i][j] == 3:
                    solution.append([i, j])
        return solution

    def step(self, i, j, path, prev):
        # print(f"pre. i={i}, j={j}, path={path}, prev={prev}, board={self.board}")
        if i < 0 or j < 0:
            # atlantic
            return 1
        if i >= self.n or j >= self.m:
            # pacific
            return 2
        curr = self.heights[i][j]
        if (i,j) in path or curr > prev:
            return 0
        # if self.board[i][j] != 0:
        #     return self.board[i][j]
        path.add((i,j))
        mask = 0
        a = b = c = d = 0
        if mask != 3: a = self.step(i + 1, j, path, curr)
        if mask != 3: b = self.step(i - 1, j, path, curr)
        if mask != 3: c = self.step(i, j + 1, path, curr)
        if mask != 3: d = self.step(i, j - 1, path, curr)
        mask = a | b | c | d
        path.remove((i, j))
        self.board[i][j] |= mask
        # print(f"mask={mask}, a={a}, b={b}, c={c}, d={d}")
        # print(f"post. i={i}, j={j}, path={path}, prev={prev}, board={self.board}")
        return self.board[i][j]


def cmp(arr):
    return set([(pair[0], pair[1]) for pair in arr])

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
            [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]],
        ),
        (
            [[1]],
            [[0,0]],
        ),
        (
            [[10,10,10],[10,1,10],[10,10,10]],
            [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]],
        ),
    ]
    for (heights, solution) in tests:
        result = sol.pacificAtlantic(heights)
        result = cmp(result)
        solution = cmp(solution)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

