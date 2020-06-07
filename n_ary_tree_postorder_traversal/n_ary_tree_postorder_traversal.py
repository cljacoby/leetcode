# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    # def postorder(self, root: 'Node') -> List[int]:
    def postorder(self, root): 
        arr = []
        if root != None:
            self.postorder_recr(root, arr)
        return arr

    def postorder_recr(self, root, arr):
        if root.children != None:
            for child in root.children:
                self.postorder_recr(child, arr)
        arr.append(root.val)
    
    def preorder(self, root): 
        arr = []
        if root != None:
            self.preorder_recr(root, arr)
        return arr

    def preorder_recr(self, root, arr):
        arr.append(root.val)
        if root.children != None:
            for child in root.children:
                self.preorder_recr(child, arr)

    def postorder_iter(self, root):
        pass


if __name__ == "__main__":
    sol = Solution()

    """
             1
          /  |  \ 
        2    3    4
      /  \ 
    5     6
    """

    root = Node(1, [
         Node(2, [
             Node(5),
             Node(6),
         ]),
         Node(3),
         Node(4),
    ])


    result = sol.postorder(root)
    print(f"result = {result}")



    root2 = None
    result = sol.postorder(root2)
    print(f"result = {result}")

