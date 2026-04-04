# https://leetcode.com/problems/diameter-of-binary-tree

from TreeNode import TreeNode

class Solution(object):
    def __init__(self):
        self.mx = -1

    def step(self, root):
        if root == None:
            return 0
        a = self.step(root.left)
        b = self.step(root.right)
        self.mx = max(self.mx, a + b)
        return max(a, b) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.step(root)
        return self.mx

if __name__ == "__main__":
    tests = [
        (
            [1,2,3,4,5],
            3,
        ),
        (
            [1,2],
            1,
        )
    ]
    for (nums, solution) in tests:
        print("------------------------")
        sol = Solution()
        tree = TreeNode.from_array(nums)
        tree.print_tree()
        result = sol.diameterOfBinaryTree(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

