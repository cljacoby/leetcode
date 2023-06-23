# https://leetcode.com/problems/validate-binary-search-tree

from TreeNode import TreeNode


# Original solution. Wrote without referencing solutions. Kinda ugly but
# gets the job done. I think there's doubling up on logic, and only
# either the integer comparisons, or the boolean return types should be
# neccessary, but right now leaning on both.
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res, _, _ = self.min_max_tree(root)
        return res

    def min_max_tree(self, node):
        if node == None:
            assert False, "Should not get here"
        mini = node.val
        maxi = node.val
        lres = True
        rres = True
        if node.left:
            res, _, b = self.min_max_tree(node.left)
            # mini = min(a, mini)
            maxi = max(b, maxi)
            lres = res and b < node.val
        if node.right:
            res, a, _ = self.min_max_tree(node.right)
            mini = min(a, mini)
            # maxi = max(b, maxi)
            rres = res and a > node.val 
        return (lres and rres, mini, maxi)

# Referenced accepted solutions for this one. Overall cleaned
# implementation, although interestingly slower than the first solution.
# Key observation for ergonomic solution is that you want to go
# top-down, passing upper_lim and lower_lim down the hierarcy. This in
# contrast to bottom-up, where you try and return up the recursion the
# max and min values of the sub-tree.
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.step(root, float('-inf'), float('inf'))

    def step(self, node, lower_lim, upper_lim):
        if node == None:
            return True
        if node.val <= lower_lim or node.val >= upper_lim:
            return False
        return self.step(node.left, lower_lim, node.val) \
                and self.step(node.right, node.val, upper_lim)
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([5,1,4,None,None,3,6], False),
        ([2,1,3], True),
        ([0], True),
    ]
    for (nums, solution) in tests:
        print("****************************")
        root = TreeNode.from_array(nums)
        root.print_tree()
        result = sol.isValidBST(root)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

