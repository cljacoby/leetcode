# https://leetcode.com/problems/validate-binary-search-tree

from TreeNode import TreeNode

class Solution(object):
    def step(self, root):
        left = right = root.val

        if root.left:
            (quit, lmin, lmax) = self.step(root.left)
            if quit or lmax >= root.val:
                return (True, None, None)
            left = lmin

        if root.right:
            (quit, rmin, rmax) = self.step(root.right)
            if quit or rmin <= root.val:
                return (True, None, None)
            right = rmax
        
        return (False, left, right)




    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return False
        (quit, _l, _r) = self.step(root)
        return not quit
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [2,1,3],
            True
        ),
        (
            [5,1,4,None,None,3,6],
            False,
        ),
        (
            [5,1,7,None,None,6,8],
            True,
        ),
    ]
    for (nums, solution) in tests:
        print("------------------------------------------------")
        tree = TreeNode.from_array(nums)
        tree.print_tree()
        result = sol.isValidBST(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

