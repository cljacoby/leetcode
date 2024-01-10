# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected

from TreeNode import TreeNode
from collections import deque

# Kinda gross, lengthy BFS solution.

class Solution(object):
    def init_parent_lookup(self, root):
        plookup = dict()
        q = deque([root])
        while len(q) > 0:
            node = q.pop()
            if node.left:
                plookup[node.left.val] = node
                q.append(node.left)
            if node.right:
                plookup[node.right.val] = node
                q.append(node.right)
        return plookup

    def origin(self, root, start, plookup):
        if root.val == start:
            return root
        left = plookup[start].left
        if left and left.val == start:
            return left
        right = plookup[start].right
        if right and right.val == start:
            return right
        assert False, f"Failed to locate node with value {start}"

    def infect(self, node, pending, plookup, visited):
        visited.add(node.val)
        if node.left and node.left.val not in visited:
            pending.append(node.left)
        if node.right and node.right.val not in visited:
            pending.append(node.right)
        if plookup.get(node.val) and plookup[node.val].val not in visited:
            p = plookup[node.val]
            pending.append(p)

    def amountOfTime(self, root, start):
        plookup = self.init_parent_lookup(root)
        visited = set()
        origin = self.origin(root, start, plookup)
        tick = 0
        ready, pending = deque(), deque()
        self.infect(origin, pending, plookup, visited)
        while len(ready) > 0 or len(pending) > 0:
            while len(ready) > 0:
                node = ready.popleft()
                self.infect(node, pending, plookup, visited)
            if len(pending) > 0:
                while len(pending) > 0:
                    node = pending.popleft()
                    visited.add(node.val)
                    ready.append(node)
                tick += 1
        return tick

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,5,3,None,4,10,6,None,None,9,2], 3, 4),
        ([1], 1, 0),
    ]
    for (nums, start, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.amountOfTime(tree, start)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

