# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

from TreeNode import TreeNode

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        (mn, mx, diff) = self.step(root, root.val, root.val)
        return diff

    def step(self, node, mx, mn):
        if node == None:
            return (mx, mn, 0) 
        v = node.val
        mn = min(mn, v)
        mx = max(mx, v)
        (lmn, lmx, l) = self.step(node.left, mn, mx)
        (rmn, rmx, r) = self.step(node.right, mn, mx)
        diff = max(
            l, abs(v - lmn), abs(v - lmx),
            r, abs(v - rmn), abs(v - rmx),
        )
        return (min(v, lmn, rmn), max(v, lmx, rmx), diff) 

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([8,3,10,1,6,None,14,None,None,4,7,None,None,13], 7),
        ([1,None,2,None,None,None,0,None,None,None,None,None,None,3], 3),
    ]
    for (nums, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.maxAncestorDiff(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

