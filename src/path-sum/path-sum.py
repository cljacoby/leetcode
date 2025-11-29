# https://leetcode.com/problems/path-sum

from TreeNode import TreeNode

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        return self.step(root, 0, target)
    
    def step(self, root, curr, target):
        if root == None:
            return False
        curr += root.val
        if (root.left == None
            and root.right == None
            and curr == target
        ):
            return True
        b = self.step(root.left, curr, target) \
            or self.step(root.right, curr, target)
        return b

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [5,4,8,11,None,13,4,7,2,None,None,None,None,None,1], 22, True
        ),
        (
            [1,2,3], 5, False
        ),
        (
            [], 0, False
        )
    ]
    for (nums, target, solution) in tests:
        tree = TreeNode.from_array(nums)
        if tree:
            tree.print_tree()
        result = sol.hasPathSum(tree, target)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

