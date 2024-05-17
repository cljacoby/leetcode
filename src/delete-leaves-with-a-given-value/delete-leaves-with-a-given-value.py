# https://leetcode.com/problems/delete-leaves-with-a-given-value

from TreeNode import TreeNode

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        dummy = TreeNode(val=target, left=root, right=None)
        self.rm(dummy, target)
        return dummy.left

    def rm(self, node, target):
        if node.left and self.rm(node.left, target):
            node.left = None
        if node.right and self.rm(node.right, target):
            node.right = None
        return node.left == None \
                and node.right == None \
                and node.val == target

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3,2,None,2,4],
            2,
            [1,None,3,None,None,None,4],
        ),
        (
            [1,3,3,3,2],
            3,
            [1,3,None,None,2],
        )
    ]
    for (start, delete, end) in tests:
        print("**********************")
        tree = TreeNode.from_array(start)
        solution = TreeNode.from_array(end)
        result = sol.removeLeafNodes(tree, delete)
        print("====== tree ======")
        tree.print_tree()
        print("====== result ======")
        result.print_tree()
        print("====== solution ======")
        solution.print_tree()
