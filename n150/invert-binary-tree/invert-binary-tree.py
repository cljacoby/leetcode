# https://leetcode.com/problems/invert-binary-tree

from TreeNode import TreeNode

class Solution(object):
    def step(self, node):
        if node == None:
            return
        self.step(node.left)
        self.step(node.right)
        node.left, node.right = node.right, node.left

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.step(root)
        return root
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [4,2,7,1,3,6,9],
            [4,7,2,9,6,3,1],
        ),
    ]
    for (nums, solution) in tests:
        print("-----------------------------------")
        tree = TreeNode.from_array(nums)
        print("tree:")
        tree.print_tree()
        solution = TreeNode.from_array(solution)
        solution.print_tree()
        print("solution:")
        result = sol.invertTree(tree)
        print("result:")
        result.print_tree()
    print("✅ All tests passed")

