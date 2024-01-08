# https://leetcode.com/problems/range-sum-of-bst

from TreeNode import TreeNode
from collections import deque

# Iterative + BFS
class Solution(object):
    def rangeSumBST(self, root, low, high):
        tot = 0
        q = deque([root])
        while len(q) > 0:
            node = q.popleft()
            if low <= node.val <= high:
                tot += node.val
            if node.left and node.val > low:
                q.append(node.left)
            if node.right and node.val < high:
                q.append(node.right)
        return tot

# Recurisve + DFS
class Solution(object):
    def rangeSumBST(self, node, low, high):
        tot = 0
        if node.left and node.val > low:
            tot += self.rangeSumBST(node.left, low, high)
        if node.right and node.val < high:
            tot += self.rangeSumBST(node.right, low, high)
        if low <= node.val <= high:
            tot += node.val
        return tot

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([10, 5, 15, 3, 7, None, 18], 7, 15, 32),
        ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23),
    ]
    for (nums, low, high, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.rangeSumBST(tree, low, high)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")
