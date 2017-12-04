#!/usr/bin/env python3

# Rules while building values while going...
# West: Go North when x > abs(y)
# North: Go East when y >= x
# East: Go South when abs(x) >= y
# South: Go West when y <= x
#
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...

class MapBuilder(object):
    West = 1
    North = 2
    East = 3
    South = 4

    # Neighbors or any item, as coordinate difference
    Neighbors = [
        (0, 1), (0, -1),
        (1, 0), (1, 1), (1, -1),
        (-1, 0), (-1, 1), (-1, -1),
    ]

    def __init__(self):
        self.dir = MapBuilder.West
        self.coor = (0,0)
        self.map = {self.coor: 1}

    def _next(self):
        if self.dir == MapBuilder.West:
            # West: Go North when x > abs(y)
            self.coor = (self.coor[0] + 1, self.coor[1])
            if self.coor[0] > abs(self.coor[1]): self.dir = MapBuilder.North
        elif self.dir == MapBuilder.North:
            # North: Go East when y >= x
            self.coor = (self.coor[0], self.coor[1] + 1)
            if self.coor[1] >= self.coor[0]: self.dir = MapBuilder.East
        elif self.dir == MapBuilder.East:
            # East: Go South when abs(x) >= y
            self.coor = (self.coor[0] - 1, self.coor[1])
            if abs(self.coor[0]) >= self.coor[1]: self.dir = MapBuilder.South
        elif self.dir == MapBuilder.South:
            # South: Go West when y <= x
            self.coor = (self.coor[0], self.coor[1] - 1)
            if self.coor[1] <= self.coor[0]: self.dir = MapBuilder.West

        value = self._getvalue()
        self.map[self.coor] = value
        return value

    def _getvalue(self):
        value = 0
        for i, j in MapBuilder.Neighbors:
            neigh = (self.coor[0] + i, self.coor[1] + j)
            if neigh in self.map:
                value += self.map[neigh]
        return value

    def run(self, number):
        """Find the first map value higher than number"""

        # Build map until we find next digit
        while True:
            value = self._next()
            #print(self.coor, value)
            if value > number:
                return value

print(MapBuilder().run(325489))

