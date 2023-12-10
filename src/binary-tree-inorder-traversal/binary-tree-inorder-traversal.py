# https://leetcode.com/problems/binary-tree-inorder-traversal

from TreeNode import TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        self.step(root, vals)
        return vals

    def step(self, node, vals):
        if node == None:
            return
        self.step(node.left, vals)
        vals.append(node.val)
        self.step(node.right, vals)
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,None,2,None,None,3,None], [1,3,2]),
        ([1], [1]),
    ]
    for (arr, solution) in tests:
        tree = TreeNode.from_array(arr)
        result = sol.inorderTraversal(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

