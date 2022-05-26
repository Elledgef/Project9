# Author: Faith
# Grithub_username: Elledgef
# Date: 5/25
# Description: This code takes a point object as an argument and returns the distance

class point:
    def __init__(self,x,y):
        self._y_coord = y
        self._x_coord = x
    def get_y_coord(self):
        return self._y_coord
    def get_x_coord(self):
        return self._x_coord

    def distance(self):
        y = (self._y_coord - self.get_y_coord()) * (self._y_coord - self.get_y_coord())
        x = (self._x_coord - self.get_x_coord()) * (self._x_coord - self.get_x_coord())
        return (x+y)**0.5
    class LineSegment:
        def  __int__(self,endpoint1,endpoint2):
            self._endpoint_1 = endpoint1
            self._endpoint_2 = endpoint2
        def length(self):
            return self._endpoint_1.distance

        def slope(self):
            y = (self._endpoint_2.get_y_coord())-(self._endpoint_1.get_y_coord())
            x = (self._endpoint_2.get_x_coord())-(self._endpoint_1.get_x_coord())
            return x/y
        def parallel(self,line_segment_2):
            if self.slope == line_segment_2.slope:
                return True
            else:
                return False







