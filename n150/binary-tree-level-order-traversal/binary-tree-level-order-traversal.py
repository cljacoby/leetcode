# https://leetcode.com/problems/binary-tree-level-order-traversal

from TreeNode import TreeNode
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        r, q = deque([]), deque([])
        levels = []
        if root != None: 
            r.append(root)
        while len(r) > 0 or len(q) > 0:
            while len(r) > 0:
                node = r.popleft()
                q.append(node)
            level = []
            while len(q) > 0:
                node = q.popleft()
                if node.left:
                    r.append(node.left)
                if node.right:
                    r.append(node.right)
                level.append(node.val)
            levels.append(level)
        return levels

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [3,9,20,None,None,15,7],
            [[3],[9,20],[15,7]],
        ),
        (
            [1],
            [[1]],
        ),
        (
            [],
            [],
        )
    ]
    for (nums, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.levelOrder(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

