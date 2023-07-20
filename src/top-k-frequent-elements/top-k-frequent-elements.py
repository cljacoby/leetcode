# https://leetcode.com/problems/top-k-frequent-elements

from collections import defaultdict
import heapq

# Kind of cheater solution using simple hashmap of frequencies, sort the
# hashmap, and the return the K first entries. I think your supposed to
# use a heap; however, the time complexity of the heap solution is
# O(NlogN) and a sort algorithm like quicksort will also give O(NlogN).
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        x = sorted(freq.items(), key=lambda p: p[1], reverse=True)
        x = map(lambda p: p[0], x)
        x = list(x)
        return x[0:k]

# Wow heaps are sweet.
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = defaultdict(int)
        # Reverse sign to use python's in-build minheap, even though we
        # really need a max heap
        for num in nums:
            freq[num] -= 1
        heap = []
        for (num, count) in freq.items():
            heapq.heappush(heap, (count, num))
        out = []
        for _ in range(k):
            out.append(heapq.heappop(heap)[1])
        return out

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([-1, -1], 1, [-1])
    ]
    for (nums, k, solution) in tests:
        result = sol.topKFrequent(nums, k)
        assert result == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")
