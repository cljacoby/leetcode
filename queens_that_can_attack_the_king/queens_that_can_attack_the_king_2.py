"""
# Notes

## Picture
_,_,_,_,_,_,_,_
_,Q,_,_,_,_,_,_
_,_,_,_,_,_,_,_
_,_,_,_,_,_,_,_
_,_,_,_,_,_,_,_
_,_,K,_,_,_,_,_
_,_,_,_,_,_,_,_
_,_,_,_,_,_,_,_

## Assumptions
* Board size is 8x8; index range is [0,7]
"""


class Diaganol:
    mini = 0
    maxi = 7

    def __init__(self, coord, m):
        if not self.in_range(*coord):
            raise Exception("Initial coordiante off the board")
        self.coord = coord
        self.m = m
        x, y = coord[0], coord[1]
        self.b = y - m * x
        self.min_coord = self.find_min_coord()
        self.max_coord = self.find_max_coord()

    def fx(self, x):
        return self.m * x + self.b

    def fy(self, y):
        return (y - self.b) / float(self.m)

    def in_range(self, x, y):
        return x <= self.maxi and y <= self.maxi and x >= self.mini and y >= self.mini

    def find_min_coord(self):
        return self._find_min_max_coord("_")

    def find_max_coord(self):
        return self._find_min_max_coord("+")

    def _find_min_max_coord(self, op):
        if op == "+":
           next_x = lambda x: x + 1
        elif op == "_":
            next_x = lambda x: x - 1
        else:
            raise Exception("Operation must be one of { '+', '_' }")

        x, y = self.coord[0], self.coord[1]
        last_x, last_y = x, y
        while self.in_range(x, y):
            last_x, last_y = x, y
            x = next_x(x) 
            y = self.fx(x)
        return (last_x, last_y)

    def __iter__(self):
        return self

    def __repr__(self):
        return f"Diaganol {{ min: {self.min_coord}, max: {self.max_coord} }}"

    def __str__(self):
        return self.__repr__()



class Solution:
    def queensAttacktheKing(self, queens, king):
        atk_positions = []
        atk_positions.extend([(x, king[1]) for x in range(0, 7) if x != king[0]])
        atk_positions.extend([(king[0], y) for y in range(0, 7) if y != king[1]])
        print(f"atk_positions = {atk_positions}")


if __name__ == "__main__":
    d_pos = Diaganol((5,2), 1)
    print(f"d_pos = {d_pos}")

    d_neg = Diaganol((5,2), -1)
    print(f"d_neg = {d_neg}")

    sol = Solution()
    queens = [(0, 1), (1, 0), (4, 0), (0, 4), (3, 3), (2, 4)]
    king = (0, 0)
    result = sol.queensAttacktheKing(queens, king)
    print(f"result = {result}")
