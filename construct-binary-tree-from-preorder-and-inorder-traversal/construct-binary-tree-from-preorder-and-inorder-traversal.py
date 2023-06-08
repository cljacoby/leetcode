# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from TreeNode import TreeNode

class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            p_val = preorder.pop(0)
            i_idx = inorder.index(p_val)
            i_val = inorder[i_idx]
            root = TreeNode(i_val)
            print(f"p_val={p_val}, i_val={i_val} i_idx={i_idx}")
            root.left = self._build_tree(preorder, inorder[:i_idx])
            root.right = self._build_tree(preorder, inorder[i_idx+1:])
            return root

    def _print_inorder(self, root):
        if root.left:
            self._print_inorder(root.left)
        print(root.val)
        if root.right:
            self._print_inorder(root.right)

    def _print_preorder(self, root):
        print(root.val)
        if root.left:
            self._print_preorder(root.left)
        if root.right:
            self._print_preorder(root.right)
        

if __name__ == "__main__":
    n0 = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n3 = TreeNode(15)
    n4 = TreeNode(7)

    n0.left = n1
    n0.right = n2
    n2.left = n3
    n2.right = n4

    sol = Solution()
    tests = [
        ([3,9,20,15,7], [9,3,15,20,7]),
    ]
    for (preorder, inorder) in tests:
        # print("*************")
        # sol._print_inorder(root)
        # print("*************")
        # sol._print_preorder(root)

        tree = sol.buildTree(preorder, inorder)

        # print(f"test={test}")
        # assert
    # print("✅ All tests passed")

