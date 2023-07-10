# https://leetcode.com/problems/serialize-and-deserialize-binary-tree

'''
Key Insights:
    1.) Kind of annoying that LeetCode's typical format for array
    encoding of a tree throws of this question by adding a bunch of
    nulls to the end. Basically you can't use the same BFS
    deserialization.
    2.) Basically comes down to choosing how you want to format your
    tree in terms of pre-order, in-order, or post-order. Seems like
    pre-order is the easiest.
    3.) Referenced an online solution, and used closures in python. Kind
    of different than my regular coding style, but actually turned out
    kind of nice. Reminded me of how easy closures are in JS.
'''

from TreeNode import TreeNode
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []

        def build(root):
            if root == None:
                arr.append("null")
            else:
                val = str(root.val)
                arr.append(val)
                build(root.left)
                build(root.right)

        build(root)
        return "[" + ",".join(arr) + "]"


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.strip("[]").split(",")
        q = deque(arr)

        def build():
            if len(q) == 0:
                return None
            val = q.popleft()
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == "__main__":
    codec = Codec()
    tests = [
        "[1,2,3,null,null,4,5,6,7,null,null,null,null,null,null]"
    ]
    for serialized in tests:
        tree = codec.deserialize(serialized)
        result = codec.serialize(tree)
        assert result == serialized, \
            f"result {result} != serialized {serialized}"
    print("✅ All tests passed")

