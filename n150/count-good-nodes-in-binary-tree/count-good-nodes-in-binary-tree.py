# https://leetcode.com/problems/count-good-nodes-in-binary-tree

from TreeNode import TreeNode

class Solution(object):
    def step(self, root, mx):
        if root == None:
            return 0
        a = self.step(root.left, max(mx, root.val))
        b = self.step(root.right, max(mx, root.val))
        c = 1 if root.val >= mx else 0
        return a + b + c


    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.step(root, -1 * (pow(10, 4) + 1))
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [3,1,4,3,None,1,5],
            4,
        ),
        (
            [3,3,None,4,2],
            3,
        ),
        (
            [1],
            1,
        ),
        (
            [-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3],
            5,
        ),
    ]
    for (nums, solution) in tests:
        print("------------------------------------------")
        root = TreeNode.from_array(nums)
        root.print_tree()
        result = sol.goodNodes(root)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

