# https://leetcode.com/problems/binary-tree-level-order-traversal-ii

from TreeNode import TreeNode
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q_curr = deque([])
        q_next = deque([])
        out = deque([])
        if root != None:
            q_next.append(root)
        while len(q_curr) > 0 or len(q_next) > 0:
            out.appendleft([])
            while len(q_next) > 0:
                q_curr.append(q_next.popleft())
            while len(q_curr) > 0:
                node = q_curr.popleft()
                out[0].append(node.val)
                if node.left:
                    q_next.append(node.left)
                if node.right:
                    q_next.append(node.right)
        return list(out)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [3,9,20,None,None,15,7],
            [[15,7],[9,20],[3]]
        )
    ]
    for (nums, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.levelOrderBottom(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

