# https://leetcode.com/problems/binary-tree-maximum-path-sum

'''
Key Insights;
    1.) Suprisingly simple for being labelled 'Hard'
    2.) Main crux of the problem is figuring out how to store the
    running maximum, vs. returning the largest maximum through the
    current path
    3.) A path doesn't need to run to leaf, and can terminate in the
    middle of the tree.
'''

from TreeNode import TreeNode

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = float('-inf')
        out = self.step(root)
        return self.max

    def step(self, node):
        if node == None:
            return 0
        left = self.step(node.left)
        right = self.step(node.right)
        out = max(
            left + node.val,
            right + node.val,
            node.val,
        )
        self.max = max(
            out,
            left + right + node.val,
            self.max
        )
        return out

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3], 6),
        ([-10,9,20,None,None,15,7], 42),
        ([2,-1], 2),
        ([2,-1,-2], 2),
    ]
    for (nums, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.maxPathSum(tree)
        assert solution == result, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

