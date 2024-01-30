import random

class RandomizedCollection(object):

    def __init__(self):
        self.values = list()
        self.indexmap = dict()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        idx = len(self.values)
        exists = val in self.indexmap
        if not exists:
            self.indexmap[val] = set()
        self.indexmap[val].add(idx)
        self.values.append(val)
        return not exists


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.indexmap:
            return False
        last_idx = len(self.values) - 1
        last = self.values[last_idx]
        last_set = self.indexmap[last]

        rm_set = self.indexmap[val]
        rm_idx = next(iter(rm_set))

        if last == val:
            rm_set.remove(last_idx)
        else:
            # Update index hashsets
            rm_set.remove(rm_idx)
            last_set.remove(last_idx)
            last_set.add(rm_idx)
            # swap-remove
            self.values[last_idx], self.values[rm_idx] = \
                    self.values[rm_idx], self.values[last_idx]

        self.values.pop()
        if len(rm_set) == 0:
            del self.indexmap[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        idx = random.randint(0, len(self.values) - 1)
        return self.values[idx]


if __name__ == "__main__":
    randset = RandomizedCollection()
    ops = [
        ("insert",      (1,),   True),
        ("insert",      (1,),   False),
        ("remove",      (2,),   False),
        ("insert",      (2,),   True),
        ("getRandom",   (),     "rand"),
        ("remove",      (1,),   True),
        ("remove",      (1,),   True),
        ("remove",      (1,),   False),
        ("getRandom",   (),     2),
    ]
    for (method, args, out) in ops:
        method = getattr(randset, method)
        ret = method(*args)
        if out != "rand":
            assert out == ret, \
                f"out {out} != ret {ret}"
    print("✅ All tests passed")

