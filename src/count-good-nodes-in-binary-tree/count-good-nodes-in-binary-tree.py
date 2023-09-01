# https://leetcode.com/problems/count-good-nodes-in-binary-tree

from collections import deque
from TreeNode import TreeNode

# First solution. DFS + recursion. Use dict to represent current path to node.
# We really only need the maximum value, so this is slightly memory ineffecient.
class Solution(object):
    MIN_VAL = -1 * pow(10, 4)
    
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        path = dict()
        self.step(root, path)
        return self.count

    def step(self, node, path):
        if node == None:
            return
        if node.val >= max(path, default=self.MIN_VAL):
            self.count += 1
        if node.val not in path:
            path[node.val] = 0
        path[node.val] += 1
        self.step(node.left, path)
        self.step(node.right, path)
        path[node.val] -= 1
        if path[node.val] == 0:
            del path[node.val]

# Improvement over first solution. Instead of keeping a dict of the
# entire path, just keep the maximum value.
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.step(root, float('-inf'))
        return self.count

    def step(self, node, mx):
        if node == None:
            return
        if node.val >= mx:
            self.count += 1
        mx = max(mx, node.val)
        self.step(node.left, mx)
        self.step(node.right, mx)

# BFS + iterative with queue.
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque([(root, root.val)])
        count = 0
        while len(q) > 0:
            (node, mx) = q.popleft()
            if node.val >= mx:
                count += 1
            mx = max(mx, node.val)
            if node.left != None:
                q.append((node.left, mx))
            if node.right != None:
                q.append((node.right, mx))
        return count

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ( [3,1,4,3,None,1,5], 4, ),
        ( [3,3,None,4,2], 3, ),
        ( [1], 1, )
    ]
    for (nums, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.goodNodes(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

