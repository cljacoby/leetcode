# https://leetcode.com/problems/evaluate-boolean-binary-tree

from TreeNode import TreeNode

class Solution(object):
    def evaluateTree(self, node):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.step(node)
    
    def step(self, node):
        if node == None:
            return False
        if node.val == 0 or node.val == 1:
            return node.val == 1
        elif node.val == 2:
            return self.step(node.left) or self.step(node.right)
        elif node.val == 3:
            return self.step(node.left) and self.step(node.right)
        assert False, "unreachable"

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [2,1,3,None,None,0,1],
            True
        ),
        (
            [0],
            False
        ),
        (
            [3,3,2,0,0,3,2,None,None,None,None,1,3,1,1,None,None,2,1,None,None,None,None,1,1,None,None,None,None,None,None],
            False
        )
    ]
    for (arr, solution) in tests:
        tree = TreeNode.from_array(arr)
        tree.print_tree()
        result = sol.evaluateTree(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

