# https://leetcode.com/problems/design-a-food-rating-system

from heapq import heappush, heapify
from collections import defaultdict

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.cuis_heaps = defaultdict(list)
        self.food_cuis_map = dict()
        self.food_rating_map = dict()

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_cuis_map[f] = c
            self.food_rating_map[f] = -r
            heappush(self.cuis_heaps[c], (-r, f))

    def changeRating(self, f, nr):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        self.food_rating_map[f] = -nr
        c = self.food_cuis_map[f]
        heappush(self.cuis_heaps[c], (-nr, f))

    def highestRated(self, c):
        """
        :type cuisine: str
        :rtype: str
        """
        # Front of each heapq is the highest rated food for each
        # cuisine. Compare this value to the rating in foot_rating_map,
        # which will be the most recently set value. If they are not
        # equal, we should pop the front heapq element off, as it's a
        # stale value. We comb out all stale values, and return the
        # higest rated food which is in synch with the rating in
        # food_rating_map.
        def front(c):
            return self.cuis_heaps[c][0]
        while self.food_rating_map[front(c)[1]] != front(c)[0]:
            heappop(self.cuis_heaps[c])
        return front(c)[1]

if __name__ == "__main__":
    fr = FoodRatings(
            ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
            ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
            [9, 12, 8, 15, 14, 7],
    )
    ops = [
        ( "highestRated",     ["korean"],         "kimchi", ), 
        ( "highestRated",     ["japanese"],       "ramen",  ), 
        ( "changeRating",     ["sushi", 16],      None,     ), 
        ( "highestRated",     ["japanese"],       "sushi",  ), 
        ( "changeRating",     ["ramen", 16],      None,     ), 
        ( "highestRated",     ["japanese"],       "ramen",  ), 
    ]
    for (func, args, ret) in ops:
        method = getattr(fr, func)
        out = method(*args)
        assert out == ret, \
            (f"Method {func} with args {args} returned {out},"
                f"not expected {ret}")
        print(f"Success. method={func}, args={args}, out={out}, ret={ret}")
    print("✅ All tests passed")

