# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree

'''
- Build a tree as a dict from `edges`, inserting both start->end and end->start
- Perform a DFS on the tree
- At each node, assess whether this node has an apple, or leads to a
  node which has an apple
- Add 2 for every node encountered which has an apple, and collect the
  total traversal length by adding result of each dfs() call
'''

class Solution(object):
    def minTime(self, n, edges, has_apple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        tree = self.build_tree(edges)
        return max(0, self.dfs(has_apple, tree, 0, -1) - 2, 0)

    def build_tree(self, edges):
        tree = dict()
        for (start, end) in edges:
            if start not in tree:
                tree[start] = []
            tree[start].append(end)
            if end not in tree:
                tree[end] = []
            tree[end].append(start)
        return tree

    def dfs(self, has_apple, tree, node, parent):
        res = 0
        if node not in tree:
            return res
        for child in tree[node]:
            if child != parent:
                res += self.dfs(has_apple, tree, child, node)
        # if this node has an apple, or leads to a node which has an
        # apple, add 2 to the traversal count to enter and exit this
        # node during traversal
        if res > 0 or has_apple[node]:
            res += 2
        return res



if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, False, True, False],
            6,
        ),
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, True, False, True, True, False],
            8,
        ),
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            [False, False, False, False, False, False, False],
            0,
        ),
    ]
    for (n, edges, has_apple, solution) in tests:
        result = sol.minTime(n, edges, has_apple)
        assert result == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")
