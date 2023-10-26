# https://leetcode.com/problems/find-largest-value-in-each-tree-row

from TreeNode import TreeNode
from collections import deque

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rows = []
        if root == None:
            return rows
        rowmax = float('-inf')
        q1 = deque([root])
        q2 = deque([])
        while len(q1) > 0:
            while len(q1) > 0:
                q2.append(q1.pop())
            if len(q2) > 0:
                rows.append(rowmax)
                while len(q2) > 0:
                    node = q2.pop()
                    if node.val > rows[-1]:
                        rows[-1] = node.val
                    if node.left != None:
                        q1.append(node.left)
                    if node.right != None:
                        q1.append(node.right)
        return rows
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ( [1,3,2,5,3,None,9], [1,3,9] ),
        ( [1,2,3], [1,3] ),
    ]
    for (nums, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.largestValues(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

