# https://leetcode.com/problems/subtree-of-another-tree

from TreeNode import TreeNode

class Solution(object):
    def isSubtree(self, tree, subtree):
        if not tree:
            return False
        if self.sameTree(tree, subtree):
            return True
        return self.isSubtree(tree.left, subtree) or \
                self.isSubtree(tree.right, subtree)

    def sameTree(self, t1, t2):
        if t1 and t2:
            return t1.val == t2.val and \
                    self.sameTree(t1.left, t2.left) and \
                    self.sameTree(t1.right, t2.right)
        return bool(t1) == bool(t2)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3,4,5,1,2,None,None,None,None,0], [4,1,2], False),
        ([3,4,5,1,2], [4,1,2], True),
        ([1,1], [1], True),
        ([3,4,5,1,None,2], [3,1,2], False),
    ]
    for (_tree, _subtree, solution) in tests:
        print("****************************")
        tree = TreeNode.from_array(_tree)
        subtree = TreeNode.from_array(_subtree)
        tree.print_tree()
        subtree.print_tree()
        result = sol.isSubtree(tree, subtree)
        assert result == solution, \
                f"result {result} != solution {solution}, _tree={_tree}, _subtree={_subtree}"
    print("✅ All tests passed")

