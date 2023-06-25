# https://leetcode.com/problems/kth-smallest-element-in-a-bst

from TreeNode import TreeNode

# Traverse tree using in-order recursion (left -> self -> right) and
# add all node values to a list. Then simply index for the desired k
# value.
class _Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.sorted_nums = list()
        self.step(root)
        return self.sorted_nums[k-1]

    def step(self, root):
        if root == None:
            return
        self.step(root.left)
        self.sorted_nums.append(root.val)
        self.step(root.right)

# Basically same as last, except instead of keeping a list of all
# values, only keep a shared variable k. Decrement k on every node
# visit. When it reaches 0, return that node's value. Should use less
# memory.
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.step(root)
        return self.res

    def step(self, root):
        if root == None or self.res != None:
            return
        self.step(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.step(root.right)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3,1,4,None,2], 1, 1),
        ([5,3,6,2,4,None,None,1], 3, 3),
    ]
    for (nums, k, solution) in tests:
        print("***********************************")
        root = TreeNode.from_array(nums)
        root.print_tree()
        result = sol.kthSmallest(root, k)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

