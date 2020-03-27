from typing import List, Set, Dict, Tuple, Optional

"""
# Notes
* A queen can attack the king horizontally if:
* The y-coordinate of the king and the queen are equal
* There are no other queens whose y-coordinate meets these criteria:
  * y-queen < y-other < y-king
  * y-king < y-other < y-queen
* Basically the other queen cant be in the way
* The same relationship is true for vertical and horizontal

# Improvements
* Refactor horizontal and vertical attack-checking logic to share code
* Create separate class Board, and init in solution
* Create the x_lookup and y_lookup during init of Board

"""

class DiagonalIter(object):
    def __init__(self, king):

        self.mini = 0
        self.maxi = 7

        self.finish_pos = False
        self.finish_neg = False

        self.king = king
        self.last = king

    def __iter__(self):
        return self

    def in_range(self, point):
        x, y = point[0], point[1]
        return (x >= self.mini
                and x <= self.maxi
                and y >= self.mini
                and y <= self.maxi)

    def next_positive(self):
        return (self.last[0] + 1, self.last[1] + 1)

    def next_negative(self):
        return (self.last[0] - 1, self.last[1] - 1)
    
    def __next__(self):
        if not self.finish_pos:
            _next = self.next_positive()
            if self.in_range(_next):
                self.last = _next
                return _next
            else:
                self.finish_pos = True

        if not self.finish_neg:
            _next = self.next_negative()
            if self.in_range(_next):
                self.last = _next
                return _next
            else:
                self.finish_neg = True
        
        return

class Solution:

    def get_x_and_y_lookups(self, queens):
        
        y_lookup: Dict[int, Dict[int, bool]] = dict()
        x_lookup: Dict[int, Dict[int, bool]] = dict()
        
        for queen in queens:
            x, y = queen[0], queen[1]
            if x not in x_lookup:
                x_lookup[x] = { y: True } 
            else:
                x_lookup[x][y] = True
            if y not in y_lookup:
                y_lookup[y] = { x: True } 
            else:
                y_lookup[y][x] = True

        return x_lookup, y_lookup

    # def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
    def queensAttacktheKing(
            self,
            queens: List[Tuple[int, int]],
            king: Tuple[int, int]
        ) -> List[Tuple[int, int]]:

        attackers: List[Tuple[int, int]] = []

        x_lookup, y_lookup = self.get_x_and_y_lookups(queens)
        print(f"x_lookup = {x_lookup}")
        print(f"y_lookup = {y_lookup}")

        for queen in queens:

            print(f"queen = {queen}")
            # check vertical attack
            if king[0] == queen[0]:
                y_mini = min(queen[1], king[1])
                y_maxi = max(queen[1], king[1])
                # Check if pieces are vetically adjacent, in which case its a valid attack
                if y_maxi - y_mini == 1:
                    attackers.append(queen)
                    continue
                # Check range of intermediate  spaces for an obstruction to vertical attack 
                y_opts = range(y_mini + 1, y_maxi)
                y_valid_atk = True
                for y_opt in y_opts:
                    if y_opt in y_lookup and queen[0] in y_lookup[y_opt]:
                        y_valid_atk = False
                        break
                if y_valid_atk:
                    attackers.append(queen)
                    continue

            # check horizontal attack
            if king[1] == queen[1]:
                x_mini = min(queen[0], king[0])
                x_maxi = max(queen[0], king[0])
                # Check if pieces are horizontally adjacent, in which case its a valid attack
                if x_maxi - x_mini == 1:
                    attackers.append(queen)
                    continue
                # Check range of intermediate  spaces for an obstruction to horizontal attack 
                x_opts = range(x_mini + 1, x_maxi)
                x_valid_atk = True
                for x_opt in x_opts:
                    if x_opt in x_lookup and queen[1] in x_lookup[x_opt]:
                        x_valid_atk = False
                        break
                if x_valid_atk:
                    attackers.append(queen)
                    continue

            # check diagonal attack
            mini, maxi = 0, 8
            pos_line = zip(range(king[0], maxi), range(king[1], mini))



        return attackers



if __name__ == "__main__":

    d = DiagonalIter((2,1))


    sol = Solution()
    queens = [
        (0,1),
        (1,0),
        (4,0),
        (0,4),
        (3,3),
        (2,4),
    ]
    king = (0,0)
    result = sol.queensAttacktheKing(queens, king)
    print(f"result = {result}")
    # [[0,1],[1,0],[3,3]]

