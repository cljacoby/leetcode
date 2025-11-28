# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

from TreeNode import TreeNode

# Initial solution. Uses a BFS traversal with preorder
# ordering, and push nodes to a stack. After finsihing
# BFS, the nodes are popped from the stack, and built into
# a linked-list (using TreeNodes) in reverse order.
class Solution1(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        self.preorder(root, stack)
        print(f"stack = {stack}")
        tip = None
        while len(stack) > 0:
            node = stack.pop()
            node.left = None
            node.right = tip
            tip = node
        return tip

    def preorder(self, root, stack):
        if root == None:
            return
        stack.append(root)
        self.preorder(root.left, stack)
        self.preorder(root.right, stack)
        
# I think O(n^2) runtime? It seems like it has to be more than O(n)
# because we're repeating recursions everyime we call step(). Achieves
# the followup goal of solving the problem in O(n) space.
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.step(root)
        return root

    def tip(self, root):
        if not root:
            return None
        return self.tip(root.right) or root

    def step(self, root):
        if root == None:
            return
        self.step(root.left)
        self.step(root.right)
        if root.left:
            left, right = root.left, root.right
            tip = self.tip(root.left)
            root.right = left
            tip.right = right
            root.left = None

# ChatGPT's solution which is O(1) extra space while still being O(n)
# runtime.
class Solution(object):
    def flatten(self, root):
        curr = root
        while curr:
            if curr.left:
                # find rightmost node of left subtree
                pred = curr.left
                while pred.right:
                    pred = pred.right

                # rewire pointers
                pred.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,5,3,4,None,6],
        ),
        (
            [1,None,2,None,None,3],
        )
    ]
    for (nums,) in tests:
        root = TreeNode.from_array(nums)
        print("--- before ---")
        root.print_tree()
        print("--- after ---")
        sol.flatten(root)
        root.print_tree()
        print("------------------------------")
