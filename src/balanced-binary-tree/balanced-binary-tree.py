# https://leetcode.com/problems/balanced-binary-tree

from TreeNode import TreeNode

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        ret = self.step(root)
        return ret[0]

    def step(self, root):
        if root == None:
            return (True, 0)
        left = self.step(root.left)
        right = self.step(root.right)
        if left[0] == False or right[0] == False:
            return (False, -1)
        if abs(left[1] - right[1]) > 1:
            return (False, -1)
        depth = max(left[1], right[1]) + 1
        return (True, depth)

        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3,9,20,None,None,15,7], True),
        ([1,2,2,3,3,None,None,4,4], False),
        # ([], True),
    ]
    for (num, solution) in tests:
        print("-------------------------")
        tree = TreeNode.from_array(num)
        tree.print_tree()
        result = sol.isBalanced(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

