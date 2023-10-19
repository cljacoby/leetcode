# https://leetcode.com/problems/lru-cache

class 2DListNode(object):
    def __init__(self, key=None, val=None, prev=None, nxt=None)
    self.key = key
    self.val = val
    self.prev = prev
    self.next = nxt

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keys = dict()
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.length = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.head = None:
            node = 2DListNode(value)
            self.head = self.tail = node
        else:
            node = 2DListNode(value, next=self.head)
            self.head = node
        self.length += 1
        if self.length > self.capacity:
            old_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del old_tail
            self.length -= 1

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    sol = Solution()
    tests = []
    for test in tests:
        # sol.method(...)
        print(f"test={test}")
        # assert
    print("✅ All tests passed")

