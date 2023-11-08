# https://leetcode.com/problems/seat-reservation-manager

from heapq import heappush, heappop

class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.open = []
        for i in range(1, self.n + 1):
            heappush(self.open, i)

    def reserve(self):
        """
        :rtype: int
        """
        assert len(self.open) > 0, \
            "No more open seats"
        seat = heappop(self.open)
        return seat

    def unreserve(self, seat):
        """
        :type seatNumber: int
        :rtype: None
        """
        heappush(self.open, seat)

if __name__ == "__main__":
    seat_manager = SeatManager(5)
    tests = [
        ("reserve",      [],       1,    ), 
        ("reserve",      [],       2,    ), 
        ("unreserve",    [2],      None, ), 
        ("reserve",      [],       2,    ), 
        ("reserve",      [],       3,    ), 
        ("reserve",      [],       4,    ), 
        ("reserve",      [],       5,    ), 
        ("unreserve",    [5],      None, ), 
    ]
    for (method, args, ret) in tests:
        func = getattr(seat_manager, method)
        out = func(*args)
        print(f"method={method}, args={args}, ret={ret}, out={out}")
        assert out == ret, \
            f"out {out} != ret {ret}"
    print("✅ All tests passed")

