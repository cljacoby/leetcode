# https://leetcode.com/problems/subtree-of-another-tree

from TreeNode import TreeNode

class Solution(object):
    def same(self, a, b):
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        if a.val != b.val:
            return False
        left = self.same(a.left, b.left)
        right = self.same(a.right, b.right)
        return left and right

    def isSubtree(self, root, sub_root):
        """
        :type root: Optional[TreeNode]
        :type sub_root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None and sub_root == None:
            return True
        if root == None or sub_root == None:
            return False
        if self.same(root, sub_root):
            return True
        return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [3,4,5,1,2],
            [4,1,2],
            True,
        ),
        (
            [3,4,5,1,2,None,None,None,None,0],
            [4,1,2],
            False,
        ),
    ]
    for (a, b, solution) in tests:
        print("--------------------------")

        root = TreeNode.from_array(a)
        print("root:")
        root.print_tree()

        sub_root = TreeNode.from_array(b)
        print("sub_root:")
        sub_root.print_tree()

        result = sol.isSubtree(root, sub_root)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

