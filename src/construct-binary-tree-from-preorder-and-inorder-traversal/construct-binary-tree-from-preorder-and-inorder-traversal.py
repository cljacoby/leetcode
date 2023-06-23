# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-inorder-traversal

from TreeNode import TreeNode


# Needed some help from other submissions to come up with this.
# Will retry from scratch by myself
class Solution1(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            p_val = preorder.pop(0)
            i_idx = inorder.index(p_val)
            i_val = inorder[i_idx]
            root = TreeNode(i_val)
            print(f"p_val={p_val}, i_val={i_val} i_idx={i_idx}")
            root.left = self.buildTree(preorder, inorder[:i_idx])
            root.right = self.buildTree(preorder, inorder[i_idx+1:])
            return root

# Was able to implement this mostly myself, think I have a handle on how
# to solve this now. This solution is slightly better by looking up
# indices from the hashmap, and using a deque to pop from the front
import collections
class Solution(object):
    def buildTree(self, preorder, inorder):
        self.preorder = collections.deque(preorder)
        self.inorder = inorder
        self.inorder_idx_map = { v:k for (k,v) in enumerate(self.inorder) }
        self.last = len(self.inorder) - 1
        return self._build_tree(0, self.last)

    def _build_tree(self, left, right):
        if left > right:
            return None
        val = self.preorder.popleft()
        idx = self.inorder_idx_map[val]
        root = TreeNode(val)
        root.left = self._build_tree(left, idx-1)
        root.right = self._build_tree(idx+1, right) 
        return root

# Validation utlitiy

def print_inorder(root):
    if root.left:
        print_inorder(root.left)
    print(root.val)
    if root.right:
        print_inorder(root.right)

def print_preorder(root):
    print(root.val)
    if root.left:
        print_preorder(root.left)
    if root.right:
        print_preorder(root.right)
        

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
        tree = sol.buildTree(preorder, inorder)
        print("***** inorder *****")
        print_inorder(tree)
        print("***** preorder *****")
        print_preorder(tree)
    # print("✅ All tests passed")

