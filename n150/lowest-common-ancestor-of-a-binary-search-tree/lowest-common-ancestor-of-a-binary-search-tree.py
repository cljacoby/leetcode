# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

'''
Key Insights:
    - Pretty intuitive and got it first submission
    - Time: ~15 minutes
'''

from TreeNode import TreeNode

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        assert p.val != q.val, "p and q are equal"
        return self.step(root, p, q)

    def step(self, root, p, q):
        if root == None:
            assert False, "missed finding p or q"

        if p.val < root.val:
            if q.val < root.val:
                return self.step(root.left, p, q)
            elif q.val >= root.val:
                return root

        if p.val > root.val:
            if q.val > root.val:
                return self.step(root.right, p, q)
            if q.val <= root.val:
                return root

        if p.val == root.val:
            return root

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([6,2,8,0,4,7,9,None,None,3,5], 2, 8, 6),
        ([6,2,8,0,4,7,9,None,None,3,5], 2, 4, 2),
    ]
    for (nums, p, q, solution) in tests:
        p = TreeNode(p)
        q = TreeNode(q)
        solution = TreeNode(solution)
        tree = TreeNode.from_array(nums)
        result = sol.lowestCommonAncestor(tree, p, q)
        assert result.val == solution.val, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

