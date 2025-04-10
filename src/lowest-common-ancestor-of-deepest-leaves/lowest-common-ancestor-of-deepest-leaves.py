# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves

from TreeNode import TreeNode

"""
Perform a DFS and track the tree depth by adding 1 in each
stack frame. From each stack frame, return the node of the substree
with greater depth. If the depths are equal, return the parent node.
"""

class Solution(object):
    def lcaDeepestLeaves(self, root):
        return self.step(root)[1]

    def step(self, root):
        if root == None:
            return (0, None)
        l = self.step(root.left)
        r = self.step(root.right)
        if l[0] > r[0]:
            return (l[0] + 1, l[1])
        elif r[0] > l[0]:
            return (r[0] + 1, r[1])
        else:
            return (l[0] + 1, root)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3,5,1,6,2,0,8,None,None,7,4], [2,7,4]),
    ]
    for (arr, solution) in tests:
        tree = TreeNode.from_array(arr)
        print("tree")
        tree.print_tree()
        result = sol.lcaDeepestLeaves(tree)
        print("result")
        print(result)

