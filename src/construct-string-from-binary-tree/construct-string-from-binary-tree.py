# https://leetcode.com/problems/construct-string-from-binary-tree

from TreeNode import TreeNode

class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        buf = []
        self.step(root, buf)
        return "".join(buf)
    
    def step(self, node, buf):
        if node == None:
            return
        buf.append(str(node.val))
        if node.left == None and node.right == None:
            return
        
        buf.append("(")
        self.step(node.left, buf)
        buf.append(")")
        
        if node.right != None:
            buf.append("(")
            self.step(node.right, buf)
            buf.append(")")

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3,4], "1(2(4))(3)"),
        ([1,2,3,None,4], "1(2()(4))(3)"),
    ]
    for (arr, solution) in tests:
        tree = TreeNode.from_array(arr)
        result = sol.tree2str(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

