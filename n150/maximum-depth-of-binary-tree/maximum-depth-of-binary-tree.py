# https://leetcode.com/problems/maximum-depth-of-binary-tree

from TreeNode import TreeNode

class Solution(object):

    def step(self, node):
        if node == None:
            return 0
        a = self.step(node.left)
        b = self.step(node.right)
        return 1 + max(a, b)
    
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.step(root)
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [3,9,20,None,None,15,7],
            3,
        ),
        (
            [1,None,2],
            2
        ),
    ]
    for (nums, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.maxDepth(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

