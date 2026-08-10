# https://leetcode.com/problems/balanced-binary-tree

from TreeNode import TreeNode

class Solution(object):
    def step(self, root):
        if root == None:
            return 0
        left = self.step(root.left)
        if left == -1:
            return left
        right = self.step(root.right)
        if right == -1:
            return right
        if abs(left - right) > 1:
            return -1
        depth = max(left, right) + 1
        return depth


    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.step(root) != -1
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [3,9,20,None,None,15,7],
            True,
        ),
        (
            [1,2,2,3,3,None,None,4,4],
            False,
        ),
        (
             [],
             True,
        ),
    ]
    for (nums, solution) in tests:
        print("-------------------------------------------------")
        tree = TreeNode.from_array(nums)
        print("tree:")
        tree.print_tree() if tree else print(tree)
        result = sol.isBalanced(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

