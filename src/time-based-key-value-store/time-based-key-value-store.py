# https://leetcode.com/problems/time-based-key-value-store

'''
Didn't read the instructions carefully, and missed the bullet point at
the bottom which stipulates values will be added with timestamps in
strictly increasing order.

So adding the heap of timestamped data is basically overkill. This
solution is still correct, and in fact has the advantage of still
working even if data is inserted in an unsorted order.

But as is it's really slow in leetcode cuz it does a bunch of extra
work.
'''

from heapq import heappush

class TimeMap(object):

    def __init__(self):
        self.store = dict()

    def bisect(self, series, i, j, target):
        print(f"bisect {{ series={series}, i={i}, j={j}, target={target} }}")
        if series[i] == target or series[j] == target:
            return target
        if j - i == 0:
            return series[j]
        if j - i == 1:
            if series[j] <= target:
                return series[j]
            return series[i]
        mid = (i + j) // 2
        if target <= series[mid]:
            return self.bisect(series, i, mid, target)
        else:
            return self.bisect(series, mid, j, target)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = { 'kv': dict(), 'series': [] }
        self.store[key]['kv'][timestamp] = value
        heappush(self.store[key]['series'], timestamp)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if (
            key not in self.store
            or timestamp < self.store[key]['series'][0]
        ):
            return ""
        if timestamp in self.store[key]['kv']:
            return self.store[key]['kv'][timestamp]
        series = self.store[key]['series']
        closest = self.bisect(series, 0, len(series) - 1, timestamp)
        return self.store[key]['kv'][closest]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == "__main__":
    tm = TimeMap()
    ops = [
        ("set", ("foo", "bar", 1), None),
        ("get", ("foo", 1), "bar"),
        ("get", ("foo", 3), "bar"),
        ("set", ("foo", "bar2", 4), None),
        ("get", ("foo", 4), "bar2"),
        ("get", ("foo", 5), "bar2"),
        ("get", ("foo", 3), "bar"),
        ("get", ("foo", 1), "bar"),
    ]
    for (func, args, ret) in ops:
        method = getattr(tm, func)
        out = method(*args)
        if ret != None:
            assert out == ret, \
                f"out {out} != ret {ret}"
    print("✅ All tests passed")

