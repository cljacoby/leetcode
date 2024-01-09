# https://leetcode.com/problems/leaf-similar-trees

from TreeNode import TreeNode

class Solution(object):
    def leaf_array(self, node, arr):
        if node == None:
            return
        self.leaf_array(node.left, arr)
        if node.left == None and node.right == None:
            arr.append(node.val)
        self.leaf_array(node.right, arr)


    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        arr1, arr2 = [], []
        self.leaf_array(root1, arr1)
        self.leaf_array(root2, arr2)
        return arr1 == arr2
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [3,5,1,6,2,9,8,None,None,7,4],
            [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8],
            True
        ),
        (
            [1,2,3],
            [1,3,2],
            False
        )
    ]
    for (arr1, arr2, solution) in tests:
        tree1 = TreeNode.from_array(arr1)
        tree2 = TreeNode.from_array(arr2)
        result = sol.leafSimilar(tree1, tree2)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

