# https://leetcode.com/problems/insert-delete-getrandom-o1

'''
One of those problems where you have to recognize the little trick,
and then it's pretty easy. Kind of a fun little gimmick. Swap the
intermediate element to pop with the last element in the list so we
can pop from end for constant time.
'''

import random

class RandomizedSet(object):

    def __init__(self):
        self.vals = list()
        self.indexmap = dict()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.indexmap:
            return False
        idx = len(self.vals)
        self.vals.append(val)
        self.indexmap[val] = idx
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.indexmap:
            return False
        # Swap element to delete with last element, and then
        # pop from end rather than pop from middle (O(1) vs O(N)).
        idx = self.indexmap[val]
        self.vals[-1], self.vals[idx] = self.vals[idx], self.vals[-1]
        self.indexmap[self.vals[idx]] = idx
        self.vals.pop()
        del self.indexmap[val]
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        idx = random.randint(0, len(self.vals) - 1)
        return self.vals[idx]

if __name__ == "__main__":
    randset = RandomizedSet()
    ops = [
        ("insert",      (1,),   True),
        ("remove",      (2,),   False),
        ("insert",      (2,),   True),
        ("getRandom",   (),     "rand"),
        ("remove",      (1,),   True),
        ("insert",      (2,),   False),
        ("getRandom",   (),     2),
    ]
    for (method, args, out) in ops:
        method = getattr(randset, method)
        ret = method(*args)
        if out != "rand":
            assert out == ret, \
                f"out {out} != ret {ret}"
    print("✅ All tests passed")

