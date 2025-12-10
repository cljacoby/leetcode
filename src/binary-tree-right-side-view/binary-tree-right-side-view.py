# https://leetcode.com/problems/binary-tree-right-side-view

from TreeNode import TreeNode
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        q1 = deque([])
        q2 = deque([]) 
        out = []
        if root:
            q1.append(root)
        while len(q1) > 0:
            q1, q2 = q2, q1
            right = None
            while len(q2) > 0:
                node = q2.popleft()
                right = node.val
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            out.append(right)
        return out
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3,None,5,None,4],
            [1,3,4],
        ),
        (
            [1,2,3,4,None,None,None,5],
            [1,3,4,5],
        ),
        (
            [1,None,3],
            [1,3],
        )
    ]
    for (nums, solution) in tests:
        print("-------------------------")
        tree = TreeNode.from_array(nums)
        tree.print_tree()
        result = sol.rightSideView(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")
 
