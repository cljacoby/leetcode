# https://leetcode.com/problems/design-hashmap

import json
from ListNode import ListNode

class MyHashMap(object):

    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.arr = [None for i in range(self.capacity)]

    def _get_node(self, key):
        h = hash(key)
        idx = h % self.capacity
        node = self.arr[idx]
        return (h, idx, node)

    def put(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        (h, idx, node) = self._get_node(key)
        if node == None:
            self.arr[idx] = ListNode((key,val))
            return
        while node.val[0] != key and node.next != None:
            node = node.next
        if node.val[0] == key:
            node.val = (key,val)
        else:
            node.next = ListNode((key,val))
   

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        (h, idx, node) = self._get_node(key)
        if node == None:
            return -1
        while node.val[0] != key and node.next != None:
            node = node.next
        if node.val[0] != key:
            return -1
        return node.val[1]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        (h, idx, node) = self._get_node(key)
        if node == None:
            return
        prev = None
        while node.val[0] != key and node.next != None:
            prev = node
            node = node.next
        if node.val[0] == key:
            if prev != None:
                prev.next = node.next
            else:
                self.arr[idx] = node.next

if __name__ == "__main__":
    hmap = MyHashMap()
    tests = json.load(open("tests.json"))
    for t in tests:
        method, args, ret = t["method"], t["args"], t["ret"]
        func = getattr(hmap, method)
        out = func(*args)
        assert out == ret, \
            f"out {out} != ret {ret}"
    print("✅ All tests passed")
